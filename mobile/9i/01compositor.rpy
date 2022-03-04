python early in compositor:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    """Image compositor module. Provides functionality to automatically
    create images from combinations of parts, and replaces the default
    image lookup to lazily load these composited images as needed,
    instead of requiring them to all be created at once during startup.

    This way, the bookkeeping overhead for the images increases only
    with their usage, not with the number of total combinations, which
    quickly becomes unsustainable (300MB+ image index in StP techdemo,
    plus heavily lengthened startup time).
    """

    class Composite(object):
        """Composite image index. Stores info about the composite's
        parts.
        """
        def __init__(self, path, position_props_by_part={}, transform=None):
            """Initialize a composite index from files under the given
            path. Images for parts will be constructed with any supplied
            per-part position properties given. A transform may be
            provided to apply to displayables this composite creates.
            """
            from collections import OrderedDict
            import itertools
            import re
            
            path = path.rstrip('/')
            
            image_regex = re.compile(
                r'^'
                + path
                + r'/([A-Za-z][A-Za-z0-9]*)/([A-Za-z_][A-Za-z0-9_]*)\.((?:png)|(?:jpg)|(?:tiff?))$')
            
            matches = itertools.ifilter(
                bool,
                (image_regex.match(path)
                    for path in sorted(renpy.list_files())))
            matches_by_part = itertools.groupby(
                matches,
                lambda match: match.group(1))
            
            self.parts = OrderedDict(
                (part_name, None)
                for part_name in position_props_by_part
                if part_name != 'etc')
            self.overlays = OrderedDict()
            self.transform = transform
            
            
            for part_name, matches_for_part in matches_by_part:
                if part_name not in position_props_by_part: continue
                
                
                if part_name != 'etc':
                    self.parts[part_name] = CompositePart(
                        ((match.group(2), match.group(0))
                            for match in matches_for_part),
                        **position_props_by_part.get(part_name, {}))
                else:
                    self.overlays = CompositePart(
                        ((match.group(2), match.group(0))
                            for match in matches_for_part),
                        **position_props_by_part.get(part_name, {}))
            
            self.base_part = next(iter(self.parts))
            self.expr_parts = list(self.parts)[1:]
        
        def __getitem__(self, attrs):
            """Creates a displayable for the given attribute combo.
            """
            from renpy.defaultstore import At, Fixed
            from renpy.display.im import Image
            from renpy.display.layout import Flatten
            
            if len(attrs) < len(self.parts): raise KeyError(attrs)
            
            attrs_iter = iter(attrs)
            
            
            
            main_attrs = zip(self.parts, attrs_iter)
            main_disps = [
                self.parts[part][attr]
                for part, attr in main_attrs
            ]
            overlay_disps = [
                self.overlays[attr]
                for attr in attrs_iter
            ]
            
            
            composited = Flatten(
                Fixed(
                    *(main_disps + overlay_disps),
                    xfit=True,
                    yfit=True))
            if self.transform is not None:
                return At(composited, self.transform)
            else:
                return composited
        
        def __contains__(self, attrs):
            """Checks whether the given combination of attributes is a
            valid combination for this composite.
            """
            return (
                
                
                len(attrs) >= len(self.parts)
                
                and all(
                    attr in part
                    for part, attr in zip(self.parts.itervalues(), attrs))
                
                
                and all(
                    overlay_attr in self.overlays
                    for overlay_attr in attrs[len(self.parts):]))
        
        def __iter__(self):
            """Generates all possible attribute combinations for this
            composite.
            """
            import itertools
            
            
            
            main_part_combos = itertools.product(*self.parts.itervalues())
            
            overlay_part_combos = list(
                itertools.chain.from_iterable(
                    itertools.combinations(
                        self.overlays.itervalues(),
                        length)
                    for length in xrange(1, len(self.overlays) + 1)))
            
            for combo in main_part_combos:
                yield combo
                for overlay_combo in overlay_part_combos:
                    yield combo + overlay_combo

    def CompositePart(pair_iter, **position_properties):
        """Creates a map of attrs to displayables for a composite part.
        Provide an iterable of `(attr, path)` tuples, and optionally
        position properties to apply to the displayables as keyword
        arguments.
        """
        from collections import OrderedDict
        from renpy.display.im import Image
        
        part = OrderedDict(
            (attr, Image(path, **position_properties))
            for attr, path in pair_iter)
        part.position_properties = position_properties
        return part

    class LazyImageMap(_dict):
        """A custom replacement for Ren'Py's image name to displayable
        mapping which lazily initializes displayables for composites.
        """
        def __init__(self, *args, **kwargs):
            super(LazyImageMap, self).__init__(self, *args, **kwargs)
            self.composites = _dict()
        
        def match_to_composite(self, image_name):
            """Match the given image name to the composite with the
            longest common prefix, and return the prefix. Returns
            `None` if the image name doesn't match any composites.
            """
            def recursive_match(prefix):
                attrs = image_name[len(prefix):]
                if len(prefix) >= len(image_name):
                    return None
                else:
                    submatch = recursive_match(image_name[:len(prefix) + 1])
                    return (
                        submatch
                        or (prefix
                            if (prefix in self.composites
                                and attrs in self.composites[prefix])
                            else None))
            return recursive_match(prefix=image_name[:1])
        
        def register_composite(self, prefix, composite):
            """Make the given composite available in the image map.
            """
            if prefix in self.composites: raise KeyError(prefix)
            
            self.composites[prefix] = composite
            image_attributes = renpy.display.image.image_attributes
            
            # image_attributes[prefix[0]] += list(
            #     prefix[1:] + attrs
            #     for attrs in iter(composite))
        
        def __contains__(self, image_name):
            return (
                super(LazyImageMap, self).__contains__(image_name)
                or self.match_to_composite(image_name) is not None)
        
        def __getitem__(self, image_name):
            
            if super(LazyImageMap, self).__contains__(image_name):
                return super(LazyImageMap, self).__getitem__(image_name)
            
            prefix = self.match_to_composite(image_name)
            if prefix is not None:
                attrs = image_name[len(prefix):]
                disp = self[image_name] = self.composites[prefix][attrs]
                return disp
            else:
                raise KeyError(image_name)
        
        def get(self, image_name, default=None):
            try:
                return self[image_name]
            except KeyError as e:
                return default
    renpy.display.image.images = LazyImageMap()


python early in compositor:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def parse_define_composite(lexer):
        from collections import OrderedDict
        
        parse = dict()
        
        prefix = parse['prefix'] = tuple(
            iter(
                renpy.partial(lexer.match, r'[A-Za-z0-9_][A-Za-z0-9-_]*'),
                None))
        if not prefix: lexer.require(lexer.word)
        lexer.require(':')
        lexer.expect_eol()
        
        block_lexer = lexer.subblock_lexer()
        
        block_lexer.advance()
        block_lexer.require('path')
        path = parse['path'] = block_lexer.require(
            block_lexer.simple_expression)
        block_lexer.expect_eol()
        
        parse['position_props'] = OrderedDict()
        
        while block_lexer.advance():
            if block_lexer.match('transform'):
                block_lexer.require(':')
                block_lexer.expect_eol()
                
                if 'transform' not in parse:
                    transform = parse['transform'] = renpy.atl.parse_atl(
                        block_lexer.subblock_lexer())
                else:
                    block_lexer.error(
                        'composite already has a transform block')
            elif block_lexer.match('position'):
                part_name = block_lexer.require(block_lexer.name)
                part_has_block = block_lexer.match(':')
                block_lexer.expect_eol()
                
                if part_name in parse['position_props']:
                    block_lexer.error(
                        'composite part already has a position block')
                
                props_for_part = parse['position_props'][part_name] = dict()
                
                if part_has_block:
                    prop_lexer = block_lexer.subblock_lexer()
                    while prop_lexer.advance():
                        prop_name = prop_lexer.require(prop_lexer.name)
                        prop_expr = prop_lexer.require(
                            prop_lexer.simple_expression)
                        props_for_part[prop_name] = prop_expr
            else:
                block_lexer.error(
                    'define composite statement only takes '
                    'transform/position subblocks')
        
        return parse

    def execute_define_composite(parse):
        from collections import OrderedDict
        from renpy.display.transform import ATLTransform
        from renpy.python import py_eval
        
        prefix = parse['prefix']
        path = py_eval(parse['path'])
        transform = None
        if 'transform' in parse:
            transform = ATLTransform(parse['transform'])
        position_props_by_part = OrderedDict(
            (
                part,
                {
                    prop: py_eval(expr, globals={}, locals=renpy.store.__dict__)
                    for prop, expr in props.iteritems()
                })
            for part, props in parse.get('position_props', {}).iteritems()
        )
        
        composite = Composite(
            path=path,
            position_props_by_part=position_props_by_part,
            transform=transform)
        renpy.display.image.images.register_composite(
            prefix=prefix,
            composite=composite)

    renpy.register_statement(
        'define composite',
        parse=parse_define_composite,
        execute=execute_define_composite,
        init=True,
        block=True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

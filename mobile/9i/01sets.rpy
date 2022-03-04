

python early in sets:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    """Sets (as in stageplay, not mathematics) group multiple images
    into a single unit, making it easier to set up and show complex
    scenes.

    Provides the `define set` statement, as well as `show` and `hide`
    equivalents which handle sets. Not to be confused with the `sets`
    module in the Python standard library.
    """


    registry = dict()

    class Set(object):
        """Sets are comprised of set pieces and an optional Python
        block. The Python is run when the set is shown; this is
        primarily for setting 3D layer depths.
        """
        def __init__(self, name, path, onshow_block, pieces):
            from renpy.python import py_compile
            from collections import OrderedDict
            
            self.name = name
            self.path = path
            self.onshow_bytecode = (py_compile(onshow_block, mode='exec')
                if onshow_block is not None
                else None)
            self.pieces = OrderedDict(
                (piece.name, piece)
                for piece in pieces)
        
        def __repr__(self):
            return '<Set {name} {pieces}>'.format(
                name=self.name,
                pieces=repr(_set(self.pieces)))
        
        def run_onshow(self):
            from renpy.python import py_exec_bytecode
            
            if self.onshow_bytecode is not None:
                py_exec_bytecode(self.onshow_bytecode)
        
        def show(self, attrs, args_by_piece={}):
            for name, piece in self.pieces.iteritems(): 
                if piece.optional and name not in args_by_piece: continue
                if not piece.showable: continue
                
                pattrs, at_list, atl = (
                    args_by_piece.get(name)
                    or (None, None, None))
                
                piece.show(
                    attrs=pattrs or attrs,
                    at_list=at_list,
                    atl=atl)
        
        def hide(self):
            for name, piece in self.pieces.iteritems():
                renpy.hide(name, layer=piece.layer)

    class SetPiece(object):
        """A set piece handles a single image tag as part of a set, and
        all transforms and other information associated with it.
        """
        def __init__(
            self,
            set_name,
            piece_name,
            path,
            layer='master',
            at_list=None,
            atl=None,
            optional=False,
            showif_expr=None):
            from renpy.display.transform import ATLTransform
            from renpy.python import py_compile
            self.set_name, self.piece_name = (set_name, piece_name)
            self.layer = layer
            self.at_list = at_list or list()
            self.transform = ATLTransform(atl) if atl is not None else None
            self.optional = optional
            self.showif_bytecode = (
                py_compile(showif_expr, mode='eval')
                if showif_expr
                else None)
            self.images = dict(
                SetPiece.generate_images(
                    path=path,
                    tag=self.name,
                    piece_name=piece_name))
        
        def __repr__(self):
            return '<SetPiece {name} onlayer {layer} {attrs}>'.format(
                name=self.name,
                layer=self.layer,
                attrs=repr(_set(' '.join(name[1:]) for name in self.images)))
        
        def show(self, attrs, at_list=None, atl=None):
            merged_at_list = list(self.at_list)
            if self.transform:
                merged_at_list.append(self.transform)
            if at_list:
                merged_at_list += at_list
            
            renpy.show(
                (self.name,) + SetPiece.match_closest_name(attrs, self.name),
                layer=self.layer,
                at_list=merged_at_list,
                atl=atl)
        
        @property
        def name(self):
            return self.set_name + '-' + self.piece_name
        
        @property
        def showable(self):
            from renpy.python import py_eval_bytecode
            return (
                py_eval_bytecode(self.showif_bytecode)
                if self.showif_bytecode
                else True)
        
        @staticmethod
        def match_closest_name(attrs, tag):
            if not attrs:
                return ()
            elif (tag, ) + attrs in renpy.display.image.images:
                return attrs
            else:
                return SetPiece.match_closest_name(attrs[:-1], tag)
        
        @staticmethod
        def generate_images(path, tag, piece_name):
            from renpy.display.im import Image
            from itertools import ifilter, imap
            import re
            
            file_re = re.compile(
                r'^'
                + path.rstrip('/')
                + r'/' + piece_name + r'( +[A-Za-z0-9-_ ]+)?\.(?:(?:jpg)|(?:png))$')
            
            for match in ifilter(bool, imap(file_re.match, renpy.list_files())):
                name = (tag,) + tuple((match.group(1) or '').strip().split())
                yield (name, Image(match.group(0)))
        
        def register_images(self):
            for name, displayable in self.images.iteritems():
                renpy.image(name, displayable)

    def parse_define_set(lexer):
        parse = object()
        parse.name = None
        parse.path = None
        parse.onshow_block = None
        parse.pieces = list()
        
        parse.name = lexer.require(lexer.image_name_component)
        lexer.require(':')
        lexer.expect_eol()
        
        block_lexer = lexer.subblock_lexer()
        while block_lexer.advance():
            if block_lexer.keyword('path'):
                if parse.path is not None:
                    block_lexer.error('path for set already specified')
                parse.path = block_lexer.require(block_lexer.string)
                block_lexer.expect_eol()
            elif block_lexer.keyword('python'):
                if parse.onshow_block is not None:
                    block_lexer.error('python block for set already specified')
                block_lexer.require(':')
                block_lexer.expect_eol()
                parse.onshow_block = block_lexer.python_block()
            elif block_lexer.keyword('piece'):
                parse.pieces.append(parse_define_set_piece(block_lexer))
            else:
                block_lexer.error('not recognized')
        
        
        
        
        
        return parse

    def parse_define_set_piece(lexer):
        parse = object()
        parse.name = None
        parse.layer = 'master'
        parse.at_list = None
        parse.atl = None
        parse.optional = False
        parse.showif_expr = None
        
        parse.name = lexer.require(lexer.image_name_component)
        while not lexer.eol():
            if lexer.keyword('onlayer'):
                parse.layer = lexer.require(lexer.name)
            elif lexer.keyword('at'):
                parse.at_list = renpy.parser.parse_simple_expression_list(lexer)
            elif lexer.match(':'):
                lexer.expect_eol()
                parse.atl = renpy.atl.parse_atl(lexer.subblock_lexer())
            elif lexer.keyword('optional'):
                parse.optional = True
            elif lexer.keyword('showif'):
                parse.showif_expr = lexer.require(lexer.simple_expression)
            else:
                lexer.error('not recognized')
        
        return parse

    def execute_define_set(parse):
        from renpy.python import py_eval
        
        pieces = [
            SetPiece(
                set_name=parse.name,
                piece_name=piece_parse.name,
                path=parse.path,
                layer=piece_parse.layer,
                at_list=(
                    map(py_eval, piece_parse.at_list)
                    if piece_parse.at_list
                    else None),
                atl=piece_parse.atl,
                optional=piece_parse.optional,
                showif_expr=piece_parse.showif_expr)
            for piece_parse in parse.pieces
        ]
        for piece in pieces:
            piece.register_images()
        registry[parse.name] = Set(
            name=parse.name,
            path=parse.path,
            onshow_block=parse.onshow_block,
            pieces=pieces)

    renpy.register_statement(
        'define set',
        parse=parse_define_set,
        execute=execute_define_set,
        init=True,
        block=True)

    def parse_show_set(lexer):
        parse = object()
        parse.name = lexer.require(lexer.image_name_component)
        parse.attrs = None
        parse.pieces = dict()
        
        if not lexer.keyword('expression'):
            parse.attrs = tuple(iter(lexer.image_name_component, None))
        else:
            parse.attrs = lexer.require(lexer.string)
        
        if not lexer.match(':'):
            lexer.expect_eol()
            return parse
        
        lexer.expect_block('show set statement')
        lexer.expect_eol()
        
        block_lexer = lexer.subblock_lexer()
        while block_lexer.advance():
            piece_name, piece_args = parse_show_set_piece(block_lexer)
            parse.pieces[piece_name] = piece_args
        
        return parse

    def parse_show_set_piece(lexer):
        from renpy.atl import parse_atl
        from renpy.parser import parse_simple_expression_list
        
        piece_name = lexer.require(lexer.image_name_component)
        piece_attrs = tuple(iter(lexer.image_name_component, None))
        piece_at_list = None
        piece_atl = None
        
        while not lexer.eol():
            if lexer.keyword('at'):
                if piece_at_list:
                    lexer.error('at specified multiple times')
                piece_at_list = parse_simple_expression_list(lexer)
            elif lexer.match(':'):
                lexer.expect_eol()
                piece_atl = parse_atl(lexer.subblock_lexer())
            else:
                lexer.error('not recognized')
        
        return (piece_name, (piece_attrs, piece_at_list, piece_atl))

    def execute_show_set(parse):
        
        if parse.name not in registry: return
        
        attrs = (
            parse.attrs
            if isinstance(parse.attrs, tuple)
            else tuple(renpy.substitute(parse.attrs, translate=False).split()))
        
        set_ = registry[parse.name]
        set_.run_onshow()
        set_.show(
            attrs=attrs,
            args_by_piece={
                set_.name + '-' + name: args
                for name, args in parse.pieces.iteritems()
            })

    def execute_scene_set(param):
        renpy.config.scene(None)
        execute_show_set(param)

    renpy.register_statement(
        'show set',
        parse=parse_show_set,
        execute=execute_show_set,
        block=False)

    renpy.register_statement(
        'show set block',
        parse=parse_show_set,
        execute=execute_show_set,
        block=True)

    renpy.register_statement(
        'scene set',
        parse=parse_show_set,
        execute=execute_scene_set,
        block=True)

    renpy.register_statement(
        'scene set only',
        parse=parse_show_set,
        execute=execute_scene_set,
        block=False)

    def parse_hide_set(lexer):
        return lexer.require(lexer.image_name_component)

    def execute_hide_set(parse):
        if parse.name not in registry: return
        registry[parse].hide()

    renpy.register_statement(
        'hide set',
        parse=parse_hide_set,
        execute=execute_hide_set)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

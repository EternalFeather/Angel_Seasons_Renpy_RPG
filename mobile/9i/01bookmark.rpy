



default _last_bookmark = None



python early:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def bookmark_parse(lexer):
        parse = object()
        
        
        
        
        parse.label = None
        
        
        parse.title = lexer.string()
        
        lexer.expect_eol()
        return parse

    def bookmark_execute(parse):
        if parse.label is None: return
        renpy.store._last_bookmark = parse.label

    renpy.register_statement(
        'bookmark',
        parse=bookmark_parse,
        execute=bookmark_execute)


init -999 python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def index_bookmarks():
        from collections import OrderedDict
        
        def get_location(node):
            
            
            filename = node.filename
            linenumber = node.linenumber
            if filename.startswith('/'):
                filename = 'game' + filename
            if filename.endswith('c'):
                filename = filename[:-1]
            return (filename, linenumber)
        
        
        
        all_labels = sorted((
            node
            for name, node in renpy.game.script.namemap.iteritems()
            if isinstance(name, basestring)),
            key=get_location)
        
        def iter_nodes(label):
            for node in label.block:
                if (isinstance(node, renpy.ast.UserStatement)
                    and node.get_name() == 'bookmark'):
                    yield node
                elif isinstance(node, renpy.ast.Init):
                    for subnode in iter_nodes(node):
                        yield subnode
        
        
        bookmarks = OrderedDict()
        for label in all_labels:
            bookmarks_in_label = list(iter_nodes(label))
            
            if not bookmarks_in_label: continue
            elif len(bookmarks_in_label) > 1:
                raise Exception('multiple bookmarks in label {name}'.format(
                    name=label.name))
            
            bookmark = bookmarks_in_label[0]
            
            
            
            
            
            name, parse = bookmark.parsed
            
            
            
            
            parse.label = label.name
            
            bookmarks[label.name] = parse
        
        return bookmarks

    bookmarks = index_bookmarks()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

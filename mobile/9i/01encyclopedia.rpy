python early in encyclopedia:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    """Encyclopedia module. Provides a standard way to write and show
    encyclopedia content with custom statements and actions.

    Usage:

    * Use the `encyclopedia section` and `encyclopedia article`
      statements to create content.
    * Define a section named `root`; it gets used as the "table of
        contents".
    * Define an `encyclopedia` screen to use as the UI. It should
      require no parameters, and have a variable named `open_article`
      for the name of the article to show, and a variable named
      `open_section` for the name of the section to show.
    """

    sections = dict()
    articles = dict()

    class Article(object):
        def __init__(self, id_, title, subtitle, text, images, access=None):
            self.id = id_
            self.title_by_translation = {None: title}
            self.subtitle_by_translation = {None: subtitle}
            self.text_by_translation = {None: text}
            self.images = images
            self.access = access or 'open'
        
        @property
        def title(self):
            return self.title_by_translation.get(
                renpy.game.preferences.language,
                self.title_by_translation[None])
        
        @property
        def subtitle(self):
            return self.subtitle_by_translation.get(
                renpy.game.preferences.language,
                self.subtitle_by_translation[None])
        
        @property
        def text(self):
            return self.text_by_translation.get(
                renpy.game.preferences.language,
                self.text_by_translation[None])
        
        @property
        def short_text(self):
            return self.text.split('{#break}')[0]
        
        @property
        def visible(self):
            from renpy.game import persistent
            return (self.access != 'hidden'
                or self.id in persistent.encyclopedia_article_unlocks)
        
        @property
        def unlocked(self):
            from renpy.game import persistent
            return (self.access == 'open'
                or self.id in persistent.encyclopedia_article_unlocks)

    class Section(object):
        def __init__(self, id_, title, nodes, access=None):
            self.id = id_
            self.title_by_translation = {None: title}
            self.raw_nodes = nodes
            self.access = access or 'open'
        
        @property
        def title(self):
            return self.title_by_translation.get(
                renpy.game.preferences.language,
                self.title_by_translation[None])
        
        @property
        def visible(self):
            from renpy.game import persistent
            return (self.access != 'hidden'
                or self.id in persistent.encyclopedia_section_unlocks)
        
        @property
        def unlocked(self):
            from renpy.game import persistent
            return (self.access == 'open'
                or self.id in persistent.encyclopedia_section_unlocks)
        
        @property
        def nodes(self):
            for type_, id_ in self.raw_nodes:
                if type_ == 'article':
                    yield articles[id_]
                elif type_ == 'section':
                    yield sections[id_]
                else:
                    raise Exception(
                        'unknown encyclopedia node type '
                        '"{type}" in "{raw_node}"'.format(
                            type=type_, raw_node=unicode((type_, id_))))
        
        @property
        def visible_nodes(self):
            return (node for node in self.nodes if node.visible)

    def ency_section_parse(lx, translating=False):
        params = dict()
        
        if translating:
            params['translation'] = lx.require(lx.word)
        
        params['id'] = lx.require(lx.word)
        lx.expect_block('encyclopedia section statement')
        lx.require(':')
        lx.expect_eol()
        
        sblx = lx.subblock_lexer()
        
        sblx.advance()
        sblx.require('title')
        params['title'] = sblx.require(sblx.string)
        sblx.expect_eol()
        
        
        
        
        if not translating:
            params['access'] = 'open'
            access_cp = sblx.checkpoint()
            sblx.advance()
            if sblx.keyword('unlock'):
                if sblx.keyword('locked'):
                    params['access'] = 'locked'
                elif sblx.keyword('hidden'):
                    params['access'] = 'hidden'
                sblx.expect_eol()
            else:
                sblx.revert(access_cp)
        
        
        
        if translating:
            return params
        
        params['nodes'] = nodes = list()
        while sblx.advance():
            if sblx.match('section'):
                nodes.append(('section', sblx.require(sblx.word)))
            elif sblx.match('article'):
                nodes.append(('article', sblx.require(sblx.word)))
            sblx.expect_eol()
        
        return params

    def ency_section_execute(params, translating=False):
        id_ = params['id']
        section = sections.get(id_)

        if translating:
            tl = params['translation']
            
            if section is None:
                section = sections[id_] = Section(
                    id_=id_,
                    title=None,
                    nodes=None)
            
            section.title_by_translation[tl] = params['title']
        elif section is None:
            section = sections[id_] = Section(
                id_=id_,
                title=params['title'],
                nodes=params['nodes'],
                access=params['access'])
        else:
            section.title_by_translation[None] = params['title']
            section.raw_nodes = params['nodes']
            section.access = params['access']

    renpy.register_statement(
        'encyclopedia section',
        parse=ency_section_parse,
        execute=ency_section_execute,
        block=True,
        init=True)

    renpy.register_statement(
        'translate encyclopedia section',
        parse=renpy.partial(ency_section_parse, translating=True),
        execute=renpy.partial(ency_section_execute, translating=True),
        block=True,
        init=True)

    def ency_article_parse(lx, translating=False):
        import re
        
        params = dict()
        
        if translating:
            params['translation'] = lx.require(lx.word)
        
        params['id'] = lx.require(lx.word)
        lx.expect_block('encyclopedia article statement')
        lx.require(':')
        lx.expect_eol()
        
        sblx = lx.subblock_lexer()
        
        sblx.advance()
        sblx.require('title')
        params['title'] = sblx.require(sblx.string)
        sblx.expect_eol()
        
        sblx.advance()
        sblx.require('subtitle')
        params['subtitle'] = sblx.require(sblx.string)
        sblx.expect_eol()
        
        sblx.advance()
        sblx.require('images')
        params['images'] = sblx.require(sblx.string)
        sblx.expect_eol()
        
        sblx.advance()
        if not translating:
            params['access'] = 'open'
            if sblx.keyword('unlock'):
                if sblx.keyword('locked'):
                    params['access'] = 'locked'
                elif sblx.keyword('hidden'):
                    params['access'] = 'hidden'
                sblx.expect_eol()
                sblx.advance()
        
        params['text'] = renpy.store.parse_multiline_string(sblx)
        
        return params

    def ency_article_execute(params, translating=False):
        from renpy.python import py_eval
        
        id_ = params['id']
        article = articles.get(id_)
        
        if translating:
            tl = params['translation']
            
            if article is None:
                article = articles[id_] = Article(
                    id_=id_,
                    title=None,
                    subtitle=None,
                    images=None,
                    text=None)
            
            article.title_by_translation[tl] = params['title']
            article.subtitle_by_translation[tl] = params['subtitle']
            article.text_by_translation[tl] = params['text']
            article.images = params['images']
        elif article is None:
            articles[params['id']] = Article(
                id_=id_,
                title=params['title'],
                subtitle=params['subtitle'],
                text=params['text'],
                images=params['images'],
                access=params['access'])
        else:
            article.title_by_translation[None] = params['title']
            article.subtitle_by_translation[None] = params['subtitle']
            article.text_by_translation[None] = params['text']
            article.images = params['images']
            article.access = params['access']

    renpy.register_statement(
        'encyclopedia article',
        parse=ency_article_parse,
        execute=ency_article_execute,
        block=True,
        init=True)

    renpy.register_statement(
        'translate encyclopedia article',
        parse=renpy.partial(ency_article_parse, translating=True),
        execute=renpy.partial(ency_article_execute, translating=True),
        block=True,
        init=True)




init python in encyclopedia:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    @renpy.pure
    class ShowArticle(renpy.ui.Action):
        def __init__(self, article):
            self.article = article
        
        def __call__(self):
            parent_section = next(
                (sn
                    for sn, section in sections.iteritems()
                    if articles.get(self.article) in section.nodes),
                None)
            
            screen = renpy.get_screen('encyclopedia')
            section = parent_section
            article = self.article
            
            if screen is None:
                renpy.run(
                    renpy.store.ShowMenu(
                        'encyclopedia',
                        section=section,
                        article=article,
                        standalone=True))
            else:
                scope = renpy.get_screen('encyclopedia').scope
                scope['open_section'] = section
                scope['open_article'] = article
                
                renpy.restart_interaction()
        
        def get_selected(self):
            screen = renpy.get_screen('encyclopedia')
            return (
                screen is not None
                and screen.scope.get('open_article') == self.article)
        
        def get_sensitive(self):
            return (self.article in articles
                and articles[self.article].unlocked)
        
        def predict(self):
            renpy.predict_screen('encyclopedia', root=self.root)

    @renpy.pure
    class ShowSection(renpy.ui.Action):
        def __init__(self, section):
            self.section = section
        
        def __call__(self):
            if self.section not in sections: return
            
            screen = renpy.get_screen('encyclopedia')
            section = self.section
            
            if screen is None:
                renpy.run(
                    renpy.store.ShowMenu(
                        'encyclopedia',
                        section=section,
                        standalone=True))
            else:  
                scope = renpy.get_screen('encyclopedia').scope
                scope['open_section'] = section
                
                renpy.restart_interaction()
        
        def get_selected(self):
            screen = renpy.get_screen('encyclopedia')
            return (
                screen is not None
                and screen.scope.get('open_section') == self.section)
        
        def predict(self):
            renpy.predict_screen('encyclopedia', root=self.root)



init 999:
    if not renpy.has_screen("encyclopedia"):
        screen encyclopedia():
            modal True

            default BACK_ACTION = Hide("encyclopedia")

            default open_article = None
            default open_section = None

            key "game_menu" action BACK_ACTION

            use _chrome(title="{#ency}Introduction", frame_style="ency_frame", back_action=BACK_ACTION, nested=True):




                fixed style_prefix "ency":
                    frame style_prefix "ency_index":
                        has viewport:
                            scrollbars "vertical"
                            mousewheel True

                        use encyclopedia_section(section="root")
                    if open_article is not None:
                        $ article = encyclopedia.articles[open_article]

                        frame style_prefix "ency_article":
                            has vbox
                            label article.title style_suffix "title_label"
                            label article.subtitle style_suffix "subtitle_label"
                            viewport:
                                scrollbars "vertical"
                                mousewheel True

                                text article.text

        screen encyclopedia_section(section):
            $ section_instance = encyclopedia.sections[section]

            vbox style_prefix "ency_index":
                for node in section_instance.visible_nodes:
                    if isinstance(node, encyclopedia.Section):
                        $ section_action = encyclopedia.ShowSection(node.id)

                        textbutton node.title style_suffix "section_button":
                            action section_action
                        if section_action.get_selected():
                            hbox:
                                vbox:
                                    for subnode in encyclopedia.sections[node.id].visible_nodes:
                                        textbutton subnode.title style_suffix "article_button":
                                            action encyclopedia.ShowArticle(subnode.id)
                    else:
                        textbutton node.title style_suffix "article_button":
                            action encyclopedia.ShowArticle(node.id)

        style ency_frame is _frame:
            xfill True
            yfill True
        style ency_fixed is _fixed
        style ency_index_frame is _frame:
            xpos scale(0)
            ypos scale(0)
            xsize scale(450)
            xmargin scale(18)
            ymargin scale(18)
            xpadding scale(48)
            ypadding scale(48)
            background Solid("#0000005f")
        style ency_index_viewport is _viewport
        style ency_index_side is _side:
            spacing scale(15)
        style ency_index_vscrollbar is _vscrollbar:
            unscrollable "insensitive"
        style ency_index_vbox is _vbox
        style ency_index_hbox is _hbox:
            xpos scale(45)
        style ency_index_button is _button:
            xfill True
        style ency_index_button_text is _button_text:
            xalign 0.0
        style ency_index_section_button is ency_index_button
        style ency_index_section_button_text is ency_index_button_text
        style ency_index_article_button is ency_index_button
        style ency_index_article_button_text is ency_index_button_text
        style ency_article_frame is _frame:
            xpos scale(450 + 18)
            ypos scale(0)
            xmaximum scale(1920 - 450 - 18 - 15)
            xmargin scale(18)
            ymargin scale(18)
            xpadding scale(48)
            ypadding scale(48)
            background Solid("#0000005f")
        style ency_article_vbox is _vbox:
            first_spacing scale(15)
            spacing scale(60)
        style ency_article_viewport is _viewport
        style ency_article_side is _side:
            spacing scale(15)
        style ency_article_vscrollbar is _vscrollbar:
            unscrollable "insensitive"
        style ency_article_title_label is _default
        style ency_article_title_label_text is _default:
            size scale(60)
        style ency_article_subtitle_label is _default
        style ency_article_subtitle_label_text is _default:
            size scale(27)
        style ency_article_text is _default:
            size scale(27)


# define persistent.encyclopedia_article_unlocks = set()
# define persistent.encyclopedia_section_unlocks = set()

init -999 python in encyclopedia:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    @renpy.pure
    def get_hyperlink_functions(style):
        return (
            renpy.partial(hyperlink_style, style=style),
            hyperlink_click,
            hyperlink_hover)

    @renpy.pure
    def hyperlink_style(a, style):
        return style

    def hyperlink_click(a):
        renpy.run(ShowArticle(article=a))

    def hyperlink_hover(a):
    #     if a is not None:
    #         renpy.show_screen(
    #             'encyclopedia_popup',
    #             article=a,
    #             _transient=True)
    #     else:
    #         renpy.hide_screen('encyclopedia_popup')
    #    renpy.restart_interaction()
        pass

    @renpy.pure
    class ArticleUnlockTracker(renpy.Displayable):
        def __init__(self, article):
            super(ArticleUnlockTracker, self).__init__()
            self.article = article
        
        def render(self, width, height, st, at):
            return renpy.Render(0, 0)
        
        def event(self, ev, x, y, st):
            from renpy.game import persistent
            persistent.encyclopedia_article_unlocks.add(self.article)
            persistent.encyclopedia_section_unlocks.update(
                section.id
                for section in sections.itervalues()
                if any(node.id == self.article for node in section.nodes))

    @renpy.pure
    def hyperlink_tag_handler(tag, param, content):
        return (
            [(renpy.TEXT_DISPLAYABLE, ArticleUnlockTracker(param))]
            + [(renpy.TEXT_TAG, 'a=' + param)]
            + content
            + [(renpy.TEXT_TAG, '/a')])

    renpy.config.custom_text_tags['encyclopedia'] = hyperlink_tag_handler
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

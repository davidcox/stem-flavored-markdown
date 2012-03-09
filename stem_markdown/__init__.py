from misaka import (Markdown, BaseRenderer, HtmlRenderer, SmartyPants,
    EXT_FENCED_CODE, EXT_TABLES, EXT_AUTOLINK, EXT_STRIKETHROUGH,
    EXT_SUPERSCRIPT, HTML_USE_XHTML,
    TABLE_ALIGN_L, TABLE_ALIGN_R, TABLE_ALIGN_C,
    TABLE_ALIGNMASK, TABLE_HEADER)

import yaml


class SfmHtmlRenderer(HtmlRenderer):

    def __init__(self, flags):
        HtmlRenderer.__init__(self, flags)
        self.doc_info = {}

    def preprocess(self, text):

        # action items:
        # 1. strip out stem-md comments (start with an unescaped "%" char)
        # 2. strip out yaml header info and parse it into self.doc_info

        # the YAML header ends with the first Markdown header element
        header_end = text.find('\n#')
        header = text[0:header_end]
        text = text[header_end:]

        d = yaml.load(header)
        self.doc_info.update(d)
        print(self.doc_info)

        # 2. process internal link markers ("[@marker]")
        # 3. add reference markers for section headers ("# Hello World" -> [hello-world]: ... )
        # 4. preprocess in-line citations, match against bibliography

        return text

    def block_code(self, text, lang):

        if lang == 'figure':
            #process figure block
            print("Found a figure!")
            return

        # pass through
        return HtmlRenderer.block_code(self, text, lang)

    def link(self, link, title, content):
        return "[Got: %s %s %s]" % (link, title, content)
        # return HtmlRenderer.link(self, link, title, content)

    def doc_header(self):
        #s = '<!-- %s -->' % (self.doc_info)
        #return s
        return ''

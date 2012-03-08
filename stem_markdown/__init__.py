from misaka import (Markdown, BaseRenderer, HtmlRenderer, SmartyPants,
    EXT_FENCED_CODE, EXT_TABLES, EXT_AUTOLINK, EXT_STRIKETHROUGH,
    EXT_SUPERSCRIPT, HTML_USE_XHTML,
    TABLE_ALIGN_L, TABLE_ALIGN_R, TABLE_ALIGN_C,
    TABLE_ALIGNMASK, TABLE_HEADER)

import yaml


class SfmPreprocessor(object):

    def __init__(self, doc_info):
        self.doc_info = doc_info

    def preprocess(self, text):

        # action items:
        # 1. strip out yaml header info and parse it into self.doc_info
        # 2. process internal links

        # the YAML header ends with the first Markdown header element
        header_end = text.find('\n#')
        header = text[0:header_end]
        text = text[header_end:]

        d = yaml.load(header)
        self.doc_info.update(d)

        return text


class SfmHtmlRenderer(HtmlRenderer, SfmPreprocessor):

    def __init__(self, flags):
        self.doc_info = {}
        HtmlRenderer.__init__(self, flags)
        SfmPreprocessor.__init__(self, self.doc_info)
        pass

    def block_code(self, text, lang):

        if lang is "figure":
            #process figure block
            print("Found a figure!")
            return

        # pass through
        return HtmlRenderer.block_code(self, text, lang)

    def doc_header(self):
        #s = '<!-- %s -->' % (self.doc_info)
        #return s
        return ''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArticlePicture import ArticlePicture


class ArticleParagraph(object):

    def __init__(self):
        self._pictures = None
        self._text = None

    @property
    def pictures(self):
        return self._pictures

    @pictures.setter
    def pictures(self, value):
        if isinstance(value, list):
            self._pictures = list()
            for i in value:
                if isinstance(i, ArticlePicture):
                    self._pictures.append(i)
                else:
                    self._pictures.append(ArticlePicture.from_alipay_dict(i))
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.pictures:
            if isinstance(self.pictures, list):
                for i in range(0, len(self.pictures)):
                    element = self.pictures[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pictures[i] = element.to_alipay_dict()
            if hasattr(self.pictures, 'to_alipay_dict'):
                params['pictures'] = self.pictures.to_alipay_dict()
            else:
                params['pictures'] = self.pictures
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArticleParagraph()
        if 'pictures' in d:
            o.pictures = d['pictures']
        if 'text' in d:
            o.text = d['text']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HelloBikeMarketWord(object):

    def __init__(self):
        self._words = None
        self._words_type = None

    @property
    def words(self):
        return self._words

    @words.setter
    def words(self, value):
        self._words = value
    @property
    def words_type(self):
        return self._words_type

    @words_type.setter
    def words_type(self, value):
        self._words_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.words:
            if hasattr(self.words, 'to_alipay_dict'):
                params['words'] = self.words.to_alipay_dict()
            else:
                params['words'] = self.words
        if self.words_type:
            if hasattr(self.words_type, 'to_alipay_dict'):
                params['words_type'] = self.words_type.to_alipay_dict()
            else:
                params['words_type'] = self.words_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HelloBikeMarketWord()
        if 'words' in d:
            o.words = d['words']
        if 'words_type' in d:
            o.words_type = d['words_type']
        return o



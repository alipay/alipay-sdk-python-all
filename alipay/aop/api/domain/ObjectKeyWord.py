#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ObjectKeyWord(object):

    def __init__(self):
        self._category = None
        self._key_word = None
        self._score = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def key_word(self):
        return self._key_word

    @key_word.setter
    def key_word(self, value):
        self._key_word = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.key_word:
            if hasattr(self.key_word, 'to_alipay_dict'):
                params['key_word'] = self.key_word.to_alipay_dict()
            else:
                params['key_word'] = self.key_word
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObjectKeyWord()
        if 'category' in d:
            o.category = d['category']
        if 'key_word' in d:
            o.key_word = d['key_word']
        if 'score' in d:
            o.score = d['score']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchBaseItems(object):

    def __init__(self):
        self._can_search = None
        self._key_words = None

    @property
    def can_search(self):
        return self._can_search

    @can_search.setter
    def can_search(self, value):
        self._can_search = value
    @property
    def key_words(self):
        return self._key_words

    @key_words.setter
    def key_words(self, value):
        if isinstance(value, list):
            self._key_words = list()
            for i in value:
                self._key_words.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.can_search:
            if hasattr(self.can_search, 'to_alipay_dict'):
                params['can_search'] = self.can_search.to_alipay_dict()
            else:
                params['can_search'] = self.can_search
        if self.key_words:
            if isinstance(self.key_words, list):
                for i in range(0, len(self.key_words)):
                    element = self.key_words[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_words[i] = element.to_alipay_dict()
            if hasattr(self.key_words, 'to_alipay_dict'):
                params['key_words'] = self.key_words.to_alipay_dict()
            else:
                params['key_words'] = self.key_words
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBaseItems()
        if 'can_search' in d:
            o.can_search = d['can_search']
        if 'key_words' in d:
            o.key_words = d['key_words']
        return o



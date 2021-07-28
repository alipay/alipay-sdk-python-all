#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchServiceItems(object):

    def __init__(self):
        self._box_status = None
        self._category_codes = None
        self._key_words = None
        self._template_id = None

    @property
    def box_status(self):
        return self._box_status

    @box_status.setter
    def box_status(self, value):
        self._box_status = value
    @property
    def category_codes(self):
        return self._category_codes

    @category_codes.setter
    def category_codes(self, value):
        if isinstance(value, list):
            self._category_codes = list()
            for i in value:
                self._category_codes.append(i)
    @property
    def key_words(self):
        return self._key_words

    @key_words.setter
    def key_words(self, value):
        if isinstance(value, list):
            self._key_words = list()
            for i in value:
                self._key_words.append(i)
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.box_status:
            if hasattr(self.box_status, 'to_alipay_dict'):
                params['box_status'] = self.box_status.to_alipay_dict()
            else:
                params['box_status'] = self.box_status
        if self.category_codes:
            if isinstance(self.category_codes, list):
                for i in range(0, len(self.category_codes)):
                    element = self.category_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_codes[i] = element.to_alipay_dict()
            if hasattr(self.category_codes, 'to_alipay_dict'):
                params['category_codes'] = self.category_codes.to_alipay_dict()
            else:
                params['category_codes'] = self.category_codes
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
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchServiceItems()
        if 'box_status' in d:
            o.box_status = d['box_status']
        if 'category_codes' in d:
            o.category_codes = d['category_codes']
        if 'key_words' in d:
            o.key_words = d['key_words']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o



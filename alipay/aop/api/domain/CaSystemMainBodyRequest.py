#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CaSystemMainBodyRequest(object):

    def __init__(self):
        self._key_word = None
        self._key_word_type = None
        self._kw_index = None
        self._main_body_model = None
        self._pos_page = None
        self._pos_x = None
        self._pos_y = None

    @property
    def key_word(self):
        return self._key_word

    @key_word.setter
    def key_word(self, value):
        self._key_word = value
    @property
    def key_word_type(self):
        return self._key_word_type

    @key_word_type.setter
    def key_word_type(self, value):
        self._key_word_type = value
    @property
    def kw_index(self):
        return self._kw_index

    @kw_index.setter
    def kw_index(self, value):
        self._kw_index = value
    @property
    def main_body_model(self):
        return self._main_body_model

    @main_body_model.setter
    def main_body_model(self, value):
        self._main_body_model = value
    @property
    def pos_page(self):
        return self._pos_page

    @pos_page.setter
    def pos_page(self, value):
        self._pos_page = value
    @property
    def pos_x(self):
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value):
        self._pos_x = value
    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value):
        self._pos_y = value


    def to_alipay_dict(self):
        params = dict()
        if self.key_word:
            if hasattr(self.key_word, 'to_alipay_dict'):
                params['key_word'] = self.key_word.to_alipay_dict()
            else:
                params['key_word'] = self.key_word
        if self.key_word_type:
            if hasattr(self.key_word_type, 'to_alipay_dict'):
                params['key_word_type'] = self.key_word_type.to_alipay_dict()
            else:
                params['key_word_type'] = self.key_word_type
        if self.kw_index:
            if hasattr(self.kw_index, 'to_alipay_dict'):
                params['kw_index'] = self.kw_index.to_alipay_dict()
            else:
                params['kw_index'] = self.kw_index
        if self.main_body_model:
            if hasattr(self.main_body_model, 'to_alipay_dict'):
                params['main_body_model'] = self.main_body_model.to_alipay_dict()
            else:
                params['main_body_model'] = self.main_body_model
        if self.pos_page:
            if hasattr(self.pos_page, 'to_alipay_dict'):
                params['pos_page'] = self.pos_page.to_alipay_dict()
            else:
                params['pos_page'] = self.pos_page
        if self.pos_x:
            if hasattr(self.pos_x, 'to_alipay_dict'):
                params['pos_x'] = self.pos_x.to_alipay_dict()
            else:
                params['pos_x'] = self.pos_x
        if self.pos_y:
            if hasattr(self.pos_y, 'to_alipay_dict'):
                params['pos_y'] = self.pos_y.to_alipay_dict()
            else:
                params['pos_y'] = self.pos_y
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaSystemMainBodyRequest()
        if 'key_word' in d:
            o.key_word = d['key_word']
        if 'key_word_type' in d:
            o.key_word_type = d['key_word_type']
        if 'kw_index' in d:
            o.kw_index = d['kw_index']
        if 'main_body_model' in d:
            o.main_body_model = d['main_body_model']
        if 'pos_page' in d:
            o.pos_page = d['pos_page']
        if 'pos_x' in d:
            o.pos_x = d['pos_x']
        if 'pos_y' in d:
            o.pos_y = d['pos_y']
        return o



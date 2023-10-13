#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SealTabsVO(object):

    def __init__(self):
        self._file_id = None
        self._global_key_word = None
        self._keyword = None
        self._kw_index = None
        self._page_number = None
        self._seal_type = None
        self._tab_type = None
        self._text_tab_value = None
        self._x_position = None
        self._y_position = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def global_key_word(self):
        return self._global_key_word

    @global_key_word.setter
    def global_key_word(self, value):
        self._global_key_word = value
    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, value):
        self._keyword = value
    @property
    def kw_index(self):
        return self._kw_index

    @kw_index.setter
    def kw_index(self, value):
        self._kw_index = value
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def seal_type(self):
        return self._seal_type

    @seal_type.setter
    def seal_type(self, value):
        self._seal_type = value
    @property
    def tab_type(self):
        return self._tab_type

    @tab_type.setter
    def tab_type(self, value):
        self._tab_type = value
    @property
    def text_tab_value(self):
        return self._text_tab_value

    @text_tab_value.setter
    def text_tab_value(self, value):
        self._text_tab_value = value
    @property
    def x_position(self):
        return self._x_position

    @x_position.setter
    def x_position(self, value):
        self._x_position = value
    @property
    def y_position(self):
        return self._y_position

    @y_position.setter
    def y_position(self, value):
        self._y_position = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.global_key_word:
            if hasattr(self.global_key_word, 'to_alipay_dict'):
                params['global_key_word'] = self.global_key_word.to_alipay_dict()
            else:
                params['global_key_word'] = self.global_key_word
        if self.keyword:
            if hasattr(self.keyword, 'to_alipay_dict'):
                params['keyword'] = self.keyword.to_alipay_dict()
            else:
                params['keyword'] = self.keyword
        if self.kw_index:
            if hasattr(self.kw_index, 'to_alipay_dict'):
                params['kw_index'] = self.kw_index.to_alipay_dict()
            else:
                params['kw_index'] = self.kw_index
        if self.page_number:
            if hasattr(self.page_number, 'to_alipay_dict'):
                params['page_number'] = self.page_number.to_alipay_dict()
            else:
                params['page_number'] = self.page_number
        if self.seal_type:
            if hasattr(self.seal_type, 'to_alipay_dict'):
                params['seal_type'] = self.seal_type.to_alipay_dict()
            else:
                params['seal_type'] = self.seal_type
        if self.tab_type:
            if hasattr(self.tab_type, 'to_alipay_dict'):
                params['tab_type'] = self.tab_type.to_alipay_dict()
            else:
                params['tab_type'] = self.tab_type
        if self.text_tab_value:
            if hasattr(self.text_tab_value, 'to_alipay_dict'):
                params['text_tab_value'] = self.text_tab_value.to_alipay_dict()
            else:
                params['text_tab_value'] = self.text_tab_value
        if self.x_position:
            if hasattr(self.x_position, 'to_alipay_dict'):
                params['x_position'] = self.x_position.to_alipay_dict()
            else:
                params['x_position'] = self.x_position
        if self.y_position:
            if hasattr(self.y_position, 'to_alipay_dict'):
                params['y_position'] = self.y_position.to_alipay_dict()
            else:
                params['y_position'] = self.y_position
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SealTabsVO()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'global_key_word' in d:
            o.global_key_word = d['global_key_word']
        if 'keyword' in d:
            o.keyword = d['keyword']
        if 'kw_index' in d:
            o.kw_index = d['kw_index']
        if 'page_number' in d:
            o.page_number = d['page_number']
        if 'seal_type' in d:
            o.seal_type = d['seal_type']
        if 'tab_type' in d:
            o.tab_type = d['tab_type']
        if 'text_tab_value' in d:
            o.text_tab_value = d['text_tab_value']
        if 'x_position' in d:
            o.x_position = d['x_position']
        if 'y_position' in d:
            o.y_position = d['y_position']
        return o



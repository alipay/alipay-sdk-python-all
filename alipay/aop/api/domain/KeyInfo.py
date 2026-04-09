#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KeyInfo(object):

    def __init__(self):
        self._filter_change = None
        self._page_key = None
        self._search_type = None
        self._second_page_key = None

    @property
    def filter_change(self):
        return self._filter_change

    @filter_change.setter
    def filter_change(self, value):
        self._filter_change = value
    @property
    def page_key(self):
        return self._page_key

    @page_key.setter
    def page_key(self, value):
        self._page_key = value
    @property
    def search_type(self):
        return self._search_type

    @search_type.setter
    def search_type(self, value):
        self._search_type = value
    @property
    def second_page_key(self):
        return self._second_page_key

    @second_page_key.setter
    def second_page_key(self, value):
        self._second_page_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.filter_change:
            if hasattr(self.filter_change, 'to_alipay_dict'):
                params['filter_change'] = self.filter_change.to_alipay_dict()
            else:
                params['filter_change'] = self.filter_change
        if self.page_key:
            if hasattr(self.page_key, 'to_alipay_dict'):
                params['page_key'] = self.page_key.to_alipay_dict()
            else:
                params['page_key'] = self.page_key
        if self.search_type:
            if hasattr(self.search_type, 'to_alipay_dict'):
                params['search_type'] = self.search_type.to_alipay_dict()
            else:
                params['search_type'] = self.search_type
        if self.second_page_key:
            if hasattr(self.second_page_key, 'to_alipay_dict'):
                params['second_page_key'] = self.second_page_key.to_alipay_dict()
            else:
                params['second_page_key'] = self.second_page_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KeyInfo()
        if 'filter_change' in d:
            o.filter_change = d['filter_change']
        if 'page_key' in d:
            o.page_key = d['page_key']
        if 'search_type' in d:
            o.search_type = d['search_type']
        if 'second_page_key' in d:
            o.second_page_key = d['second_page_key']
        return o



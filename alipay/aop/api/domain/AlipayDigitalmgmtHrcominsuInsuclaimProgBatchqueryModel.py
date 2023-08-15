#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtHrcominsuInsuclaimProgBatchqueryModel(object):

    def __init__(self):
        self._current_page = None
        self._data_key = None
        self._is_submit = None
        self._page_size = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value
    @property
    def is_submit(self):
        return self._is_submit

    @is_submit.setter
    def is_submit(self, value):
        self._is_submit = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        if self.is_submit:
            if hasattr(self.is_submit, 'to_alipay_dict'):
                params['is_submit'] = self.is_submit.to_alipay_dict()
            else:
                params['is_submit'] = self.is_submit
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrcominsuInsuclaimProgBatchqueryModel()
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'data_key' in d:
            o.data_key = d['data_key']
        if 'is_submit' in d:
            o.is_submit = d['is_submit']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o



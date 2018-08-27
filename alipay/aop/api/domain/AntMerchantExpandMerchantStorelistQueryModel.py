#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandMerchantStorelistQueryModel(object):

    def __init__(self):
        self._is_include_cognate = None
        self._page_num = None
        self._page_size = None
        self._pid = None

    @property
    def is_include_cognate(self):
        return self._is_include_cognate

    @is_include_cognate.setter
    def is_include_cognate(self, value):
        self._is_include_cognate = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_include_cognate:
            if hasattr(self.is_include_cognate, 'to_alipay_dict'):
                params['is_include_cognate'] = self.is_include_cognate.to_alipay_dict()
            else:
                params['is_include_cognate'] = self.is_include_cognate
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandMerchantStorelistQueryModel()
        if 'is_include_cognate' in d:
            o.is_include_cognate = d['is_include_cognate']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'pid' in d:
            o.pid = d['pid']
        return o



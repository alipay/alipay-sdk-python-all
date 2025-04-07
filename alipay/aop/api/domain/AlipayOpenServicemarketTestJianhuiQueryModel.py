#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JhUserPageDetailTest import JhUserPageDetailTest


class AlipayOpenServicemarketTestJianhuiQueryModel(object):

    def __init__(self):
        self._jianhui_test = None
        self._page_num = None
        self._page_size = None
        self._total = None

    @property
    def jianhui_test(self):
        return self._jianhui_test

    @jianhui_test.setter
    def jianhui_test(self, value):
        if isinstance(value, JhUserPageDetailTest):
            self._jianhui_test = value
        else:
            self._jianhui_test = JhUserPageDetailTest.from_alipay_dict(value)
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
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.jianhui_test:
            if hasattr(self.jianhui_test, 'to_alipay_dict'):
                params['jianhui_test'] = self.jianhui_test.to_alipay_dict()
            else:
                params['jianhui_test'] = self.jianhui_test
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
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketTestJianhuiQueryModel()
        if 'jianhui_test' in d:
            o.jianhui_test = d['jianhui_test']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'total' in d:
            o.total = d['total']
        return o



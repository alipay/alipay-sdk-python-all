#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinKeyWord(object):

    def __init__(self):
        self._keyword = None
        self._page_num = None

    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, value):
        self._keyword = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.keyword:
            if hasattr(self.keyword, 'to_alipay_dict'):
                params['keyword'] = self.keyword.to_alipay_dict()
            else:
                params['keyword'] = self.keyword
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinKeyWord()
        if 'keyword' in d:
            o.keyword = d['keyword']
        if 'page_num' in d:
            o.page_num = d['page_num']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransDishonorQueryModel(object):

    def __init__(self):
        self._dishonor_begin = None
        self._dishonor_end = None
        self._page = None

    @property
    def dishonor_begin(self):
        return self._dishonor_begin

    @dishonor_begin.setter
    def dishonor_begin(self, value):
        self._dishonor_begin = value
    @property
    def dishonor_end(self):
        return self._dishonor_end

    @dishonor_end.setter
    def dishonor_end(self, value):
        self._dishonor_end = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value


    def to_alipay_dict(self):
        params = dict()
        if self.dishonor_begin:
            if hasattr(self.dishonor_begin, 'to_alipay_dict'):
                params['dishonor_begin'] = self.dishonor_begin.to_alipay_dict()
            else:
                params['dishonor_begin'] = self.dishonor_begin
        if self.dishonor_end:
            if hasattr(self.dishonor_end, 'to_alipay_dict'):
                params['dishonor_end'] = self.dishonor_end.to_alipay_dict()
            else:
                params['dishonor_end'] = self.dishonor_end
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransDishonorQueryModel()
        if 'dishonor_begin' in d:
            o.dishonor_begin = d['dishonor_begin']
        if 'dishonor_end' in d:
            o.dishonor_end = d['dishonor_end']
        if 'page' in d:
            o.page = d['page']
        return o



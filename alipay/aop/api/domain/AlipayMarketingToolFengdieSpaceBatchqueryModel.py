#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingToolFengdieSpaceBatchqueryModel(object):

    def __init__(self):
        self._page_number = None
        self._page_size = None

    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_number:
            if hasattr(self.page_number, 'to_alipay_dict'):
                params['page_number'] = self.page_number.to_alipay_dict()
            else:
                params['page_number'] = self.page_number
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
        o = AlipayMarketingToolFengdieSpaceBatchqueryModel()
        if 'page_number' in d:
            o.page_number = d['page_number']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o



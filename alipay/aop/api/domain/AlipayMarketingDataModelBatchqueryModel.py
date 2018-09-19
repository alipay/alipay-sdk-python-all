#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingDataModelBatchqueryModel(object):

    def __init__(self):
        self._page = None
        self._size = None

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value


    def to_alipay_dict(self):
        params = dict()
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingDataModelBatchqueryModel()
        if 'page' in d:
            o.page = d['page']
        if 'size' in d:
            o.size = d['size']
        return o



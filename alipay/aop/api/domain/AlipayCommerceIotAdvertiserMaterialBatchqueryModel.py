#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotAdvertiserMaterialBatchqueryModel(object):

    def __init__(self):
        self._only_total = None
        self._page_num = None
        self._page_size = None

    @property
    def only_total(self):
        return self._only_total

    @only_total.setter
    def only_total(self, value):
        self._only_total = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.only_total:
            if hasattr(self.only_total, 'to_alipay_dict'):
                params['only_total'] = self.only_total.to_alipay_dict()
            else:
                params['only_total'] = self.only_total
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotAdvertiserMaterialBatchqueryModel()
        if 'only_total' in d:
            o.only_total = d['only_total']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o



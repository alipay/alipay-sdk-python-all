#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordermaterialsMaterialsBatchqueryModel(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._production_order_no = None

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
    def production_order_no(self):
        return self._production_order_no

    @production_order_no.setter
    def production_order_no(self, value):
        self._production_order_no = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.production_order_no:
            if hasattr(self.production_order_no, 'to_alipay_dict'):
                params['production_order_no'] = self.production_order_no.to_alipay_dict()
            else:
                params['production_order_no'] = self.production_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordermaterialsMaterialsBatchqueryModel()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'production_order_no' in d:
            o.production_order_no = d['production_order_no']
        return o



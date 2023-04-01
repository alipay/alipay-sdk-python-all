#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceServiceproductPageQueryModel(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._service_expense_sub_type = None

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
    def service_expense_sub_type(self):
        return self._service_expense_sub_type

    @service_expense_sub_type.setter
    def service_expense_sub_type(self, value):
        self._service_expense_sub_type = value


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
        if self.service_expense_sub_type:
            if hasattr(self.service_expense_sub_type, 'to_alipay_dict'):
                params['service_expense_sub_type'] = self.service_expense_sub_type.to_alipay_dict()
            else:
                params['service_expense_sub_type'] = self.service_expense_sub_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceServiceproductPageQueryModel()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'service_expense_sub_type' in d:
            o.service_expense_sub_type = d['service_expense_sub_type']
        return o



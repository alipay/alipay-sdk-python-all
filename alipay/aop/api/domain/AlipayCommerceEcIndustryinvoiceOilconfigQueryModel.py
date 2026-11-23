#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcIndustryinvoiceOilconfigQueryModel(object):

    def __init__(self):
        self._item_tax_code = None
        self._page_num = None
        self._page_size = None
        self._tax_no = None

    @property
    def item_tax_code(self):
        return self._item_tax_code

    @item_tax_code.setter
    def item_tax_code(self, value):
        self._item_tax_code = value
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
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_tax_code:
            if hasattr(self.item_tax_code, 'to_alipay_dict'):
                params['item_tax_code'] = self.item_tax_code.to_alipay_dict()
            else:
                params['item_tax_code'] = self.item_tax_code
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
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcIndustryinvoiceOilconfigQueryModel()
        if 'item_tax_code' in d:
            o.item_tax_code = d['item_tax_code']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceFarmerproductionQueryModel(object):

    def __init__(self):
        self._cert_no = None
        self._farmer_id = None
        self._farmer_item_id = None
        self._page_no = None
        self._page_size = None
        self._sale_end_date = None
        self._sale_start_date = None
        self._tax_code = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def farmer_id(self):
        return self._farmer_id

    @farmer_id.setter
    def farmer_id(self, value):
        self._farmer_id = value
    @property
    def farmer_item_id(self):
        return self._farmer_item_id

    @farmer_item_id.setter
    def farmer_item_id(self, value):
        self._farmer_item_id = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def sale_end_date(self):
        return self._sale_end_date

    @sale_end_date.setter
    def sale_end_date(self, value):
        self._sale_end_date = value
    @property
    def sale_start_date(self):
        return self._sale_start_date

    @sale_start_date.setter
    def sale_start_date(self, value):
        self._sale_start_date = value
    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, value):
        self._tax_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.farmer_id:
            if hasattr(self.farmer_id, 'to_alipay_dict'):
                params['farmer_id'] = self.farmer_id.to_alipay_dict()
            else:
                params['farmer_id'] = self.farmer_id
        if self.farmer_item_id:
            if hasattr(self.farmer_item_id, 'to_alipay_dict'):
                params['farmer_item_id'] = self.farmer_item_id.to_alipay_dict()
            else:
                params['farmer_item_id'] = self.farmer_item_id
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.sale_end_date:
            if hasattr(self.sale_end_date, 'to_alipay_dict'):
                params['sale_end_date'] = self.sale_end_date.to_alipay_dict()
            else:
                params['sale_end_date'] = self.sale_end_date
        if self.sale_start_date:
            if hasattr(self.sale_start_date, 'to_alipay_dict'):
                params['sale_start_date'] = self.sale_start_date.to_alipay_dict()
            else:
                params['sale_start_date'] = self.sale_start_date
        if self.tax_code:
            if hasattr(self.tax_code, 'to_alipay_dict'):
                params['tax_code'] = self.tax_code.to_alipay_dict()
            else:
                params['tax_code'] = self.tax_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceFarmerproductionQueryModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'farmer_id' in d:
            o.farmer_id = d['farmer_id']
        if 'farmer_item_id' in d:
            o.farmer_item_id = d['farmer_item_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sale_end_date' in d:
            o.sale_end_date = d['sale_end_date']
        if 'sale_start_date' in d:
            o.sale_start_date = d['sale_start_date']
        if 'tax_code' in d:
            o.tax_code = d['tax_code']
        return o



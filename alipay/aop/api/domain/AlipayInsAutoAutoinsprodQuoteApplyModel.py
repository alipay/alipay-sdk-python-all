#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsProduct import InsProduct
from alipay.aop.api.domain.InsProduct import InsProduct


class AlipayInsAutoAutoinsprodQuoteApplyModel(object):

    def __init__(self):
        self._business_product = None
        self._check_code = None
        self._check_code_id = None
        self._check_type = None
        self._company_id = None
        self._company_ids = None
        self._enquiry_biz_id = None
        self._force_product = None
        self._is_tong_rong = None
        self._quote_type = None
        self._tax_inst_code = None
        self._tax_inst_name = None
        self._tax_payment_code = None
        self._tax_payment_date = None
        self._tax_type = None

    @property
    def business_product(self):
        return self._business_product

    @business_product.setter
    def business_product(self, value):
        if isinstance(value, InsProduct):
            self._business_product = value
        else:
            self._business_product = InsProduct.from_alipay_dict(value)
    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def check_code_id(self):
        return self._check_code_id

    @check_code_id.setter
    def check_code_id(self, value):
        self._check_code_id = value
    @property
    def check_type(self):
        return self._check_type

    @check_type.setter
    def check_type(self, value):
        self._check_type = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def company_ids(self):
        return self._company_ids

    @company_ids.setter
    def company_ids(self, value):
        if isinstance(value, list):
            self._company_ids = list()
            for i in value:
                self._company_ids.append(i)
    @property
    def enquiry_biz_id(self):
        return self._enquiry_biz_id

    @enquiry_biz_id.setter
    def enquiry_biz_id(self, value):
        self._enquiry_biz_id = value
    @property
    def force_product(self):
        return self._force_product

    @force_product.setter
    def force_product(self, value):
        if isinstance(value, InsProduct):
            self._force_product = value
        else:
            self._force_product = InsProduct.from_alipay_dict(value)
    @property
    def is_tong_rong(self):
        return self._is_tong_rong

    @is_tong_rong.setter
    def is_tong_rong(self, value):
        self._is_tong_rong = value
    @property
    def quote_type(self):
        return self._quote_type

    @quote_type.setter
    def quote_type(self, value):
        self._quote_type = value
    @property
    def tax_inst_code(self):
        return self._tax_inst_code

    @tax_inst_code.setter
    def tax_inst_code(self, value):
        self._tax_inst_code = value
    @property
    def tax_inst_name(self):
        return self._tax_inst_name

    @tax_inst_name.setter
    def tax_inst_name(self, value):
        self._tax_inst_name = value
    @property
    def tax_payment_code(self):
        return self._tax_payment_code

    @tax_payment_code.setter
    def tax_payment_code(self, value):
        self._tax_payment_code = value
    @property
    def tax_payment_date(self):
        return self._tax_payment_date

    @tax_payment_date.setter
    def tax_payment_date(self, value):
        self._tax_payment_date = value
    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, value):
        self._tax_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_product:
            if hasattr(self.business_product, 'to_alipay_dict'):
                params['business_product'] = self.business_product.to_alipay_dict()
            else:
                params['business_product'] = self.business_product
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.check_code_id:
            if hasattr(self.check_code_id, 'to_alipay_dict'):
                params['check_code_id'] = self.check_code_id.to_alipay_dict()
            else:
                params['check_code_id'] = self.check_code_id
        if self.check_type:
            if hasattr(self.check_type, 'to_alipay_dict'):
                params['check_type'] = self.check_type.to_alipay_dict()
            else:
                params['check_type'] = self.check_type
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.company_ids:
            if isinstance(self.company_ids, list):
                for i in range(0, len(self.company_ids)):
                    element = self.company_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.company_ids[i] = element.to_alipay_dict()
            if hasattr(self.company_ids, 'to_alipay_dict'):
                params['company_ids'] = self.company_ids.to_alipay_dict()
            else:
                params['company_ids'] = self.company_ids
        if self.enquiry_biz_id:
            if hasattr(self.enquiry_biz_id, 'to_alipay_dict'):
                params['enquiry_biz_id'] = self.enquiry_biz_id.to_alipay_dict()
            else:
                params['enquiry_biz_id'] = self.enquiry_biz_id
        if self.force_product:
            if hasattr(self.force_product, 'to_alipay_dict'):
                params['force_product'] = self.force_product.to_alipay_dict()
            else:
                params['force_product'] = self.force_product
        if self.is_tong_rong:
            if hasattr(self.is_tong_rong, 'to_alipay_dict'):
                params['is_tong_rong'] = self.is_tong_rong.to_alipay_dict()
            else:
                params['is_tong_rong'] = self.is_tong_rong
        if self.quote_type:
            if hasattr(self.quote_type, 'to_alipay_dict'):
                params['quote_type'] = self.quote_type.to_alipay_dict()
            else:
                params['quote_type'] = self.quote_type
        if self.tax_inst_code:
            if hasattr(self.tax_inst_code, 'to_alipay_dict'):
                params['tax_inst_code'] = self.tax_inst_code.to_alipay_dict()
            else:
                params['tax_inst_code'] = self.tax_inst_code
        if self.tax_inst_name:
            if hasattr(self.tax_inst_name, 'to_alipay_dict'):
                params['tax_inst_name'] = self.tax_inst_name.to_alipay_dict()
            else:
                params['tax_inst_name'] = self.tax_inst_name
        if self.tax_payment_code:
            if hasattr(self.tax_payment_code, 'to_alipay_dict'):
                params['tax_payment_code'] = self.tax_payment_code.to_alipay_dict()
            else:
                params['tax_payment_code'] = self.tax_payment_code
        if self.tax_payment_date:
            if hasattr(self.tax_payment_date, 'to_alipay_dict'):
                params['tax_payment_date'] = self.tax_payment_date.to_alipay_dict()
            else:
                params['tax_payment_date'] = self.tax_payment_date
        if self.tax_type:
            if hasattr(self.tax_type, 'to_alipay_dict'):
                params['tax_type'] = self.tax_type.to_alipay_dict()
            else:
                params['tax_type'] = self.tax_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoAutoinsprodQuoteApplyModel()
        if 'business_product' in d:
            o.business_product = d['business_product']
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'check_code_id' in d:
            o.check_code_id = d['check_code_id']
        if 'check_type' in d:
            o.check_type = d['check_type']
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'company_ids' in d:
            o.company_ids = d['company_ids']
        if 'enquiry_biz_id' in d:
            o.enquiry_biz_id = d['enquiry_biz_id']
        if 'force_product' in d:
            o.force_product = d['force_product']
        if 'is_tong_rong' in d:
            o.is_tong_rong = d['is_tong_rong']
        if 'quote_type' in d:
            o.quote_type = d['quote_type']
        if 'tax_inst_code' in d:
            o.tax_inst_code = d['tax_inst_code']
        if 'tax_inst_name' in d:
            o.tax_inst_name = d['tax_inst_name']
        if 'tax_payment_code' in d:
            o.tax_payment_code = d['tax_payment_code']
        if 'tax_payment_date' in d:
            o.tax_payment_date = d['tax_payment_date']
        if 'tax_type' in d:
            o.tax_type = d['tax_type']
        return o



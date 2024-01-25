#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceBaseInfo(object):

    def __init__(self):
        self._check_code = None
        self._invoice_amt = None
        self._invoice_category = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_id = None
        self._invoice_image = None
        self._invoice_no = None
        self._invoice_out_no = None
        self._invoice_type = None
        self._seller_company_name = None
        self._tax_amt = None
        self._tax_bureau_source = None

    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        self._invoice_amt = value
    @property
    def invoice_category(self):
        return self._invoice_category

    @invoice_category.setter
    def invoice_category(self, value):
        self._invoice_category = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_image(self):
        return self._invoice_image

    @invoice_image.setter
    def invoice_image(self, value):
        self._invoice_image = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_out_no(self):
        return self._invoice_out_no

    @invoice_out_no.setter
    def invoice_out_no(self, value):
        self._invoice_out_no = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def seller_company_name(self):
        return self._seller_company_name

    @seller_company_name.setter
    def seller_company_name(self, value):
        self._seller_company_name = value
    @property
    def tax_amt(self):
        return self._tax_amt

    @tax_amt.setter
    def tax_amt(self, value):
        self._tax_amt = value
    @property
    def tax_bureau_source(self):
        return self._tax_bureau_source

    @tax_bureau_source.setter
    def tax_bureau_source(self, value):
        self._tax_bureau_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_category:
            if hasattr(self.invoice_category, 'to_alipay_dict'):
                params['invoice_category'] = self.invoice_category.to_alipay_dict()
            else:
                params['invoice_category'] = self.invoice_category
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_image:
            if hasattr(self.invoice_image, 'to_alipay_dict'):
                params['invoice_image'] = self.invoice_image.to_alipay_dict()
            else:
                params['invoice_image'] = self.invoice_image
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_out_no:
            if hasattr(self.invoice_out_no, 'to_alipay_dict'):
                params['invoice_out_no'] = self.invoice_out_no.to_alipay_dict()
            else:
                params['invoice_out_no'] = self.invoice_out_no
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.seller_company_name:
            if hasattr(self.seller_company_name, 'to_alipay_dict'):
                params['seller_company_name'] = self.seller_company_name.to_alipay_dict()
            else:
                params['seller_company_name'] = self.seller_company_name
        if self.tax_amt:
            if hasattr(self.tax_amt, 'to_alipay_dict'):
                params['tax_amt'] = self.tax_amt.to_alipay_dict()
            else:
                params['tax_amt'] = self.tax_amt
        if self.tax_bureau_source:
            if hasattr(self.tax_bureau_source, 'to_alipay_dict'):
                params['tax_bureau_source'] = self.tax_bureau_source.to_alipay_dict()
            else:
                params['tax_bureau_source'] = self.tax_bureau_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceBaseInfo()
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_category' in d:
            o.invoice_category = d['invoice_category']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_image' in d:
            o.invoice_image = d['invoice_image']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_out_no' in d:
            o.invoice_out_no = d['invoice_out_no']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'seller_company_name' in d:
            o.seller_company_name = d['seller_company_name']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        if 'tax_bureau_source' in d:
            o.tax_bureau_source = d['tax_bureau_source']
        return o



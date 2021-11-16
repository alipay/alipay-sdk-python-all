#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncOutputinvoiceRcptamountQueryModel(object):

    def __init__(self):
        self._ar_no = None
        self._inst_id = None
        self._invoice_date_begin = None
        self._invoice_date_end = None
        self._ip_id = None
        self._ip_role_id = None
        self._need_invoice = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._product_code = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_date_begin(self):
        return self._invoice_date_begin

    @invoice_date_begin.setter
    def invoice_date_begin(self, value):
        self._invoice_date_begin = value
    @property
    def invoice_date_end(self):
        return self._invoice_date_end

    @invoice_date_end.setter
    def invoice_date_end(self, value):
        self._invoice_date_end = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def need_invoice(self):
        return self._need_invoice

    @need_invoice.setter
    def need_invoice(self, value):
        self._need_invoice = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_date_begin:
            if hasattr(self.invoice_date_begin, 'to_alipay_dict'):
                params['invoice_date_begin'] = self.invoice_date_begin.to_alipay_dict()
            else:
                params['invoice_date_begin'] = self.invoice_date_begin
        if self.invoice_date_end:
            if hasattr(self.invoice_date_end, 'to_alipay_dict'):
                params['invoice_date_end'] = self.invoice_date_end.to_alipay_dict()
            else:
                params['invoice_date_end'] = self.invoice_date_end
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.need_invoice:
            if hasattr(self.need_invoice, 'to_alipay_dict'):
                params['need_invoice'] = self.need_invoice.to_alipay_dict()
            else:
                params['need_invoice'] = self.need_invoice
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncOutputinvoiceRcptamountQueryModel()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_date_begin' in d:
            o.invoice_date_begin = d['invoice_date_begin']
        if 'invoice_date_end' in d:
            o.invoice_date_end = d['invoice_date_end']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'need_invoice' in d:
            o.need_invoice = d['need_invoice']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InputInvoiceOrderRequest(object):

    def __init__(self):
        self._buyer_inst_id = None
        self._currency_code = None
        self._exclude_tax_invoice_amt = None
        self._invoice_amt = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_material = None
        self._invoice_no = None
        self._invoice_receive_date = None
        self._invoice_source = None
        self._invoice_type = None
        self._operator = None
        self._out_bill_no = None
        self._out_bill_type = None
        self._relate_amount = None
        self._relate_tax_amt = None
        self._seller_ip_role_id = None
        self._source = None
        self._tax_amt = None
        self._tax_rate = None

    @property
    def buyer_inst_id(self):
        return self._buyer_inst_id

    @buyer_inst_id.setter
    def buyer_inst_id(self, value):
        self._buyer_inst_id = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def exclude_tax_invoice_amt(self):
        return self._exclude_tax_invoice_amt

    @exclude_tax_invoice_amt.setter
    def exclude_tax_invoice_amt(self, value):
        self._exclude_tax_invoice_amt = value
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        self._invoice_amt = value
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
    def invoice_material(self):
        return self._invoice_material

    @invoice_material.setter
    def invoice_material(self, value):
        self._invoice_material = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_receive_date(self):
        return self._invoice_receive_date

    @invoice_receive_date.setter
    def invoice_receive_date(self, value):
        self._invoice_receive_date = value
    @property
    def invoice_source(self):
        return self._invoice_source

    @invoice_source.setter
    def invoice_source(self, value):
        self._invoice_source = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_bill_no(self):
        return self._out_bill_no

    @out_bill_no.setter
    def out_bill_no(self, value):
        self._out_bill_no = value
    @property
    def out_bill_type(self):
        return self._out_bill_type

    @out_bill_type.setter
    def out_bill_type(self, value):
        self._out_bill_type = value
    @property
    def relate_amount(self):
        return self._relate_amount

    @relate_amount.setter
    def relate_amount(self, value):
        self._relate_amount = value
    @property
    def relate_tax_amt(self):
        return self._relate_tax_amt

    @relate_tax_amt.setter
    def relate_tax_amt(self, value):
        self._relate_tax_amt = value
    @property
    def seller_ip_role_id(self):
        return self._seller_ip_role_id

    @seller_ip_role_id.setter
    def seller_ip_role_id(self, value):
        self._seller_ip_role_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def tax_amt(self):
        return self._tax_amt

    @tax_amt.setter
    def tax_amt(self, value):
        self._tax_amt = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_inst_id:
            if hasattr(self.buyer_inst_id, 'to_alipay_dict'):
                params['buyer_inst_id'] = self.buyer_inst_id.to_alipay_dict()
            else:
                params['buyer_inst_id'] = self.buyer_inst_id
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.exclude_tax_invoice_amt:
            if hasattr(self.exclude_tax_invoice_amt, 'to_alipay_dict'):
                params['exclude_tax_invoice_amt'] = self.exclude_tax_invoice_amt.to_alipay_dict()
            else:
                params['exclude_tax_invoice_amt'] = self.exclude_tax_invoice_amt
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
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
        if self.invoice_material:
            if hasattr(self.invoice_material, 'to_alipay_dict'):
                params['invoice_material'] = self.invoice_material.to_alipay_dict()
            else:
                params['invoice_material'] = self.invoice_material
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_receive_date:
            if hasattr(self.invoice_receive_date, 'to_alipay_dict'):
                params['invoice_receive_date'] = self.invoice_receive_date.to_alipay_dict()
            else:
                params['invoice_receive_date'] = self.invoice_receive_date
        if self.invoice_source:
            if hasattr(self.invoice_source, 'to_alipay_dict'):
                params['invoice_source'] = self.invoice_source.to_alipay_dict()
            else:
                params['invoice_source'] = self.invoice_source
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_bill_no:
            if hasattr(self.out_bill_no, 'to_alipay_dict'):
                params['out_bill_no'] = self.out_bill_no.to_alipay_dict()
            else:
                params['out_bill_no'] = self.out_bill_no
        if self.out_bill_type:
            if hasattr(self.out_bill_type, 'to_alipay_dict'):
                params['out_bill_type'] = self.out_bill_type.to_alipay_dict()
            else:
                params['out_bill_type'] = self.out_bill_type
        if self.relate_amount:
            if hasattr(self.relate_amount, 'to_alipay_dict'):
                params['relate_amount'] = self.relate_amount.to_alipay_dict()
            else:
                params['relate_amount'] = self.relate_amount
        if self.relate_tax_amt:
            if hasattr(self.relate_tax_amt, 'to_alipay_dict'):
                params['relate_tax_amt'] = self.relate_tax_amt.to_alipay_dict()
            else:
                params['relate_tax_amt'] = self.relate_tax_amt
        if self.seller_ip_role_id:
            if hasattr(self.seller_ip_role_id, 'to_alipay_dict'):
                params['seller_ip_role_id'] = self.seller_ip_role_id.to_alipay_dict()
            else:
                params['seller_ip_role_id'] = self.seller_ip_role_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.tax_amt:
            if hasattr(self.tax_amt, 'to_alipay_dict'):
                params['tax_amt'] = self.tax_amt.to_alipay_dict()
            else:
                params['tax_amt'] = self.tax_amt
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceOrderRequest()
        if 'buyer_inst_id' in d:
            o.buyer_inst_id = d['buyer_inst_id']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'exclude_tax_invoice_amt' in d:
            o.exclude_tax_invoice_amt = d['exclude_tax_invoice_amt']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_material' in d:
            o.invoice_material = d['invoice_material']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_receive_date' in d:
            o.invoice_receive_date = d['invoice_receive_date']
        if 'invoice_source' in d:
            o.invoice_source = d['invoice_source']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_bill_no' in d:
            o.out_bill_no = d['out_bill_no']
        if 'out_bill_type' in d:
            o.out_bill_type = d['out_bill_type']
        if 'relate_amount' in d:
            o.relate_amount = d['relate_amount']
        if 'relate_tax_amt' in d:
            o.relate_tax_amt = d['relate_tax_amt']
        if 'seller_ip_role_id' in d:
            o.seller_ip_role_id = d['seller_ip_role_id']
        if 'source' in d:
            o.source = d['source']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o



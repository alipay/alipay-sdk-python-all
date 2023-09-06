#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceArrivalDetailDTO(object):

    def __init__(self):
        self._arrival_id = None
        self._expense_id = None
        self._ext_json = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._invoice_bill_id = None
        self._invoice_id = None
        self._invoice_line_id = None
        self._use_amount = None
        self._wht_amount = None
        self._wht_rate = None

    @property
    def arrival_id(self):
        return self._arrival_id

    @arrival_id.setter
    def arrival_id(self, value):
        self._arrival_id = value
    @property
    def expense_id(self):
        return self._expense_id

    @expense_id.setter
    def expense_id(self, value):
        self._expense_id = value
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def invoice_bill_id(self):
        return self._invoice_bill_id

    @invoice_bill_id.setter
    def invoice_bill_id(self, value):
        self._invoice_bill_id = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_line_id(self):
        return self._invoice_line_id

    @invoice_line_id.setter
    def invoice_line_id(self, value):
        self._invoice_line_id = value
    @property
    def use_amount(self):
        return self._use_amount

    @use_amount.setter
    def use_amount(self, value):
        self._use_amount = value
    @property
    def wht_amount(self):
        return self._wht_amount

    @wht_amount.setter
    def wht_amount(self, value):
        self._wht_amount = value
    @property
    def wht_rate(self):
        return self._wht_rate

    @wht_rate.setter
    def wht_rate(self, value):
        self._wht_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrival_id:
            if hasattr(self.arrival_id, 'to_alipay_dict'):
                params['arrival_id'] = self.arrival_id.to_alipay_dict()
            else:
                params['arrival_id'] = self.arrival_id
        if self.expense_id:
            if hasattr(self.expense_id, 'to_alipay_dict'):
                params['expense_id'] = self.expense_id.to_alipay_dict()
            else:
                params['expense_id'] = self.expense_id
        if self.ext_json:
            if hasattr(self.ext_json, 'to_alipay_dict'):
                params['ext_json'] = self.ext_json.to_alipay_dict()
            else:
                params['ext_json'] = self.ext_json
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.invoice_bill_id:
            if hasattr(self.invoice_bill_id, 'to_alipay_dict'):
                params['invoice_bill_id'] = self.invoice_bill_id.to_alipay_dict()
            else:
                params['invoice_bill_id'] = self.invoice_bill_id
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_line_id:
            if hasattr(self.invoice_line_id, 'to_alipay_dict'):
                params['invoice_line_id'] = self.invoice_line_id.to_alipay_dict()
            else:
                params['invoice_line_id'] = self.invoice_line_id
        if self.use_amount:
            if hasattr(self.use_amount, 'to_alipay_dict'):
                params['use_amount'] = self.use_amount.to_alipay_dict()
            else:
                params['use_amount'] = self.use_amount
        if self.wht_amount:
            if hasattr(self.wht_amount, 'to_alipay_dict'):
                params['wht_amount'] = self.wht_amount.to_alipay_dict()
            else:
                params['wht_amount'] = self.wht_amount
        if self.wht_rate:
            if hasattr(self.wht_rate, 'to_alipay_dict'):
                params['wht_rate'] = self.wht_rate.to_alipay_dict()
            else:
                params['wht_rate'] = self.wht_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceArrivalDetailDTO()
        if 'arrival_id' in d:
            o.arrival_id = d['arrival_id']
        if 'expense_id' in d:
            o.expense_id = d['expense_id']
        if 'ext_json' in d:
            o.ext_json = d['ext_json']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'invoice_bill_id' in d:
            o.invoice_bill_id = d['invoice_bill_id']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_line_id' in d:
            o.invoice_line_id = d['invoice_line_id']
        if 'use_amount' in d:
            o.use_amount = d['use_amount']
        if 'wht_amount' in d:
            o.wht_amount = d['wht_amount']
        if 'wht_rate' in d:
            o.wht_rate = d['wht_rate']
        return o



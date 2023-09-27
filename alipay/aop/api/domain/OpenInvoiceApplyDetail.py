#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenInvoiceApplyDetail(object):

    def __init__(self):
        self._bill_amount = None
        self._bill_no = None
        self._invoice_amount = None
        self._open_id = None
        self._platform_user_id = None
        self._platform_user_id_type = None
        self._related_bill_no = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def platform_user_id(self):
        return self._platform_user_id

    @platform_user_id.setter
    def platform_user_id(self, value):
        self._platform_user_id = value
    @property
    def platform_user_id_type(self):
        return self._platform_user_id_type

    @platform_user_id_type.setter
    def platform_user_id_type(self, value):
        self._platform_user_id_type = value
    @property
    def related_bill_no(self):
        return self._related_bill_no

    @related_bill_no.setter
    def related_bill_no(self, value):
        self._related_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.platform_user_id:
            if hasattr(self.platform_user_id, 'to_alipay_dict'):
                params['platform_user_id'] = self.platform_user_id.to_alipay_dict()
            else:
                params['platform_user_id'] = self.platform_user_id
        if self.platform_user_id_type:
            if hasattr(self.platform_user_id_type, 'to_alipay_dict'):
                params['platform_user_id_type'] = self.platform_user_id_type.to_alipay_dict()
            else:
                params['platform_user_id_type'] = self.platform_user_id_type
        if self.related_bill_no:
            if hasattr(self.related_bill_no, 'to_alipay_dict'):
                params['related_bill_no'] = self.related_bill_no.to_alipay_dict()
            else:
                params['related_bill_no'] = self.related_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenInvoiceApplyDetail()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'platform_user_id' in d:
            o.platform_user_id = d['platform_user_id']
        if 'platform_user_id_type' in d:
            o.platform_user_id_type = d['platform_user_id_type']
        if 'related_bill_no' in d:
            o.related_bill_no = d['related_bill_no']
        return o



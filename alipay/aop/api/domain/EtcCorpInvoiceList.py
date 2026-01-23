#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtcCorpInvoiceList(object):

    def __init__(self):
        self._buyer_name = None
        self._failed_reason = None
        self._invoice_code = None
        self._invoice_make_time = None
        self._invoice_num = None
        self._invoice_oss_url = None
        self._invoice_status = None
        self._invoice_type = None
        self._total_amount = None
        self._total_tax_amount = None

    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def failed_reason(self):
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, value):
        self._failed_reason = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_make_time(self):
        return self._invoice_make_time

    @invoice_make_time.setter
    def invoice_make_time(self, value):
        self._invoice_make_time = value
    @property
    def invoice_num(self):
        return self._invoice_num

    @invoice_num.setter
    def invoice_num(self, value):
        self._invoice_num = value
    @property
    def invoice_oss_url(self):
        return self._invoice_oss_url

    @invoice_oss_url.setter
    def invoice_oss_url(self, value):
        self._invoice_oss_url = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_tax_amount(self):
        return self._total_tax_amount

    @total_tax_amount.setter
    def total_tax_amount(self, value):
        self._total_tax_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.failed_reason:
            if hasattr(self.failed_reason, 'to_alipay_dict'):
                params['failed_reason'] = self.failed_reason.to_alipay_dict()
            else:
                params['failed_reason'] = self.failed_reason
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_make_time:
            if hasattr(self.invoice_make_time, 'to_alipay_dict'):
                params['invoice_make_time'] = self.invoice_make_time.to_alipay_dict()
            else:
                params['invoice_make_time'] = self.invoice_make_time
        if self.invoice_num:
            if hasattr(self.invoice_num, 'to_alipay_dict'):
                params['invoice_num'] = self.invoice_num.to_alipay_dict()
            else:
                params['invoice_num'] = self.invoice_num
        if self.invoice_oss_url:
            if hasattr(self.invoice_oss_url, 'to_alipay_dict'):
                params['invoice_oss_url'] = self.invoice_oss_url.to_alipay_dict()
            else:
                params['invoice_oss_url'] = self.invoice_oss_url
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.total_tax_amount:
            if hasattr(self.total_tax_amount, 'to_alipay_dict'):
                params['total_tax_amount'] = self.total_tax_amount.to_alipay_dict()
            else:
                params['total_tax_amount'] = self.total_tax_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcCorpInvoiceList()
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'failed_reason' in d:
            o.failed_reason = d['failed_reason']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_make_time' in d:
            o.invoice_make_time = d['invoice_make_time']
        if 'invoice_num' in d:
            o.invoice_num = d['invoice_num']
        if 'invoice_oss_url' in d:
            o.invoice_oss_url = d['invoice_oss_url']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'total_tax_amount' in d:
            o.total_tax_amount = d['total_tax_amount']
        return o



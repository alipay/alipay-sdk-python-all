#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ObcInvoiceResult(object):

    def __init__(self):
        self._currency = None
        self._download_url = None
        self._id = None
        self._invoice_amt = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_no = None
        self._invoice_status = None
        self._red_flag = None
        self._redeem_amt = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
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
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def red_flag(self):
        return self._red_flag

    @red_flag.setter
    def red_flag(self, value):
        self._red_flag = value
    @property
    def redeem_amt(self):
        return self._redeem_amt

    @redeem_amt.setter
    def redeem_amt(self, value):
        self._redeem_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
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
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.red_flag:
            if hasattr(self.red_flag, 'to_alipay_dict'):
                params['red_flag'] = self.red_flag.to_alipay_dict()
            else:
                params['red_flag'] = self.red_flag
        if self.redeem_amt:
            if hasattr(self.redeem_amt, 'to_alipay_dict'):
                params['redeem_amt'] = self.redeem_amt.to_alipay_dict()
            else:
                params['redeem_amt'] = self.redeem_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObcInvoiceResult()
        if 'currency' in d:
            o.currency = d['currency']
        if 'download_url' in d:
            o.download_url = d['download_url']
        if 'id' in d:
            o.id = d['id']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'red_flag' in d:
            o.red_flag = d['red_flag']
        if 'redeem_amt' in d:
            o.redeem_amt = d['redeem_amt']
        return o



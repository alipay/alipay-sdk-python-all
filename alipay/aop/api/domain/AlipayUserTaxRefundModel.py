#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserTaxRefundModel(object):

    def __init__(self):
        self._account_book_id = None
        self._cert_no = None
        self._cert_type = None
        self._invoice_amount = None
        self._qr_code = None
        self._refund_amount = None
        self._refund_biz_no = None
        self._user_name = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_biz_no(self):
        return self._refund_biz_no

    @refund_biz_no.setter
    def refund_biz_no(self, value):
        self._refund_biz_no = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_book_id:
            if hasattr(self.account_book_id, 'to_alipay_dict'):
                params['account_book_id'] = self.account_book_id.to_alipay_dict()
            else:
                params['account_book_id'] = self.account_book_id
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_biz_no:
            if hasattr(self.refund_biz_no, 'to_alipay_dict'):
                params['refund_biz_no'] = self.refund_biz_no.to_alipay_dict()
            else:
                params['refund_biz_no'] = self.refund_biz_no
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserTaxRefundModel()
        if 'account_book_id' in d:
            o.account_book_id = d['account_book_id']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_biz_no' in d:
            o.refund_biz_no = d['refund_biz_no']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceFundTransferDetectModel(object):

    def __init__(self):
        self._monetary_amount = None
        self._payment_account = None
        self._payment_bank_name = None
        self._payment_date = None
        self._receipt_account = None
        self._receipt_bank_name = None
        self._recipient = None
        self._recipient_id = None
        self._sequence_code = None

    @property
    def monetary_amount(self):
        return self._monetary_amount

    @monetary_amount.setter
    def monetary_amount(self, value):
        self._monetary_amount = value
    @property
    def payment_account(self):
        return self._payment_account

    @payment_account.setter
    def payment_account(self, value):
        self._payment_account = value
    @property
    def payment_bank_name(self):
        return self._payment_bank_name

    @payment_bank_name.setter
    def payment_bank_name(self, value):
        self._payment_bank_name = value
    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value
    @property
    def receipt_account(self):
        return self._receipt_account

    @receipt_account.setter
    def receipt_account(self, value):
        self._receipt_account = value
    @property
    def receipt_bank_name(self):
        return self._receipt_bank_name

    @receipt_bank_name.setter
    def receipt_bank_name(self, value):
        self._receipt_bank_name = value
    @property
    def recipient(self):
        return self._recipient

    @recipient.setter
    def recipient(self, value):
        self._recipient = value
    @property
    def recipient_id(self):
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, value):
        self._recipient_id = value
    @property
    def sequence_code(self):
        return self._sequence_code

    @sequence_code.setter
    def sequence_code(self, value):
        self._sequence_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.monetary_amount:
            if hasattr(self.monetary_amount, 'to_alipay_dict'):
                params['monetary_amount'] = self.monetary_amount.to_alipay_dict()
            else:
                params['monetary_amount'] = self.monetary_amount
        if self.payment_account:
            if hasattr(self.payment_account, 'to_alipay_dict'):
                params['payment_account'] = self.payment_account.to_alipay_dict()
            else:
                params['payment_account'] = self.payment_account
        if self.payment_bank_name:
            if hasattr(self.payment_bank_name, 'to_alipay_dict'):
                params['payment_bank_name'] = self.payment_bank_name.to_alipay_dict()
            else:
                params['payment_bank_name'] = self.payment_bank_name
        if self.payment_date:
            if hasattr(self.payment_date, 'to_alipay_dict'):
                params['payment_date'] = self.payment_date.to_alipay_dict()
            else:
                params['payment_date'] = self.payment_date
        if self.receipt_account:
            if hasattr(self.receipt_account, 'to_alipay_dict'):
                params['receipt_account'] = self.receipt_account.to_alipay_dict()
            else:
                params['receipt_account'] = self.receipt_account
        if self.receipt_bank_name:
            if hasattr(self.receipt_bank_name, 'to_alipay_dict'):
                params['receipt_bank_name'] = self.receipt_bank_name.to_alipay_dict()
            else:
                params['receipt_bank_name'] = self.receipt_bank_name
        if self.recipient:
            if hasattr(self.recipient, 'to_alipay_dict'):
                params['recipient'] = self.recipient.to_alipay_dict()
            else:
                params['recipient'] = self.recipient
        if self.recipient_id:
            if hasattr(self.recipient_id, 'to_alipay_dict'):
                params['recipient_id'] = self.recipient_id.to_alipay_dict()
            else:
                params['recipient_id'] = self.recipient_id
        if self.sequence_code:
            if hasattr(self.sequence_code, 'to_alipay_dict'):
                params['sequence_code'] = self.sequence_code.to_alipay_dict()
            else:
                params['sequence_code'] = self.sequence_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceFundTransferDetectModel()
        if 'monetary_amount' in d:
            o.monetary_amount = d['monetary_amount']
        if 'payment_account' in d:
            o.payment_account = d['payment_account']
        if 'payment_bank_name' in d:
            o.payment_bank_name = d['payment_bank_name']
        if 'payment_date' in d:
            o.payment_date = d['payment_date']
        if 'receipt_account' in d:
            o.receipt_account = d['receipt_account']
        if 'receipt_bank_name' in d:
            o.receipt_bank_name = d['receipt_bank_name']
        if 'recipient' in d:
            o.recipient = d['recipient']
        if 'recipient_id' in d:
            o.recipient_id = d['recipient_id']
        if 'sequence_code' in d:
            o.sequence_code = d['sequence_code']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class OutputApplyInvoiceDetailOrder(object):

    def __init__(self):
        self._target_invoice_amt = None
        self._target_invoice_note = None
        self._target_ip_role_id = None

    @property
    def target_invoice_amt(self):
        return self._target_invoice_amt

    @target_invoice_amt.setter
    def target_invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._target_invoice_amt = value
        else:
            self._target_invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def target_invoice_note(self):
        return self._target_invoice_note

    @target_invoice_note.setter
    def target_invoice_note(self, value):
        self._target_invoice_note = value
    @property
    def target_ip_role_id(self):
        return self._target_ip_role_id

    @target_ip_role_id.setter
    def target_ip_role_id(self, value):
        self._target_ip_role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.target_invoice_amt:
            if hasattr(self.target_invoice_amt, 'to_alipay_dict'):
                params['target_invoice_amt'] = self.target_invoice_amt.to_alipay_dict()
            else:
                params['target_invoice_amt'] = self.target_invoice_amt
        if self.target_invoice_note:
            if hasattr(self.target_invoice_note, 'to_alipay_dict'):
                params['target_invoice_note'] = self.target_invoice_note.to_alipay_dict()
            else:
                params['target_invoice_note'] = self.target_invoice_note
        if self.target_ip_role_id:
            if hasattr(self.target_ip_role_id, 'to_alipay_dict'):
                params['target_ip_role_id'] = self.target_ip_role_id.to_alipay_dict()
            else:
                params['target_ip_role_id'] = self.target_ip_role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutputApplyInvoiceDetailOrder()
        if 'target_invoice_amt' in d:
            o.target_invoice_amt = d['target_invoice_amt']
        if 'target_invoice_note' in d:
            o.target_invoice_note = d['target_invoice_note']
        if 'target_ip_role_id' in d:
            o.target_ip_role_id = d['target_ip_role_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankLogTransferFormNew import BankLogTransferFormNew


class AlipayBossFncGfcenterBanklogtransferCreateModel(object):

    def __init__(self):
        self._bank_log_transfer_form_new = None

    @property
    def bank_log_transfer_form_new(self):
        return self._bank_log_transfer_form_new

    @bank_log_transfer_form_new.setter
    def bank_log_transfer_form_new(self, value):
        if isinstance(value, BankLogTransferFormNew):
            self._bank_log_transfer_form_new = value
        else:
            self._bank_log_transfer_form_new = BankLogTransferFormNew.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bank_log_transfer_form_new:
            if hasattr(self.bank_log_transfer_form_new, 'to_alipay_dict'):
                params['bank_log_transfer_form_new'] = self.bank_log_transfer_form_new.to_alipay_dict()
            else:
                params['bank_log_transfer_form_new'] = self.bank_log_transfer_form_new
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfcenterBanklogtransferCreateModel()
        if 'bank_log_transfer_form_new' in d:
            o.bank_log_transfer_form_new = d['bank_log_transfer_form_new']
        return o



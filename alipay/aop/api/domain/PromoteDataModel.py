#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoteDataModel(object):

    def __init__(self):
        self._checked_voucher_num = None
        self._claim_voucher_num = None
        self._commission_amount = None

    @property
    def checked_voucher_num(self):
        return self._checked_voucher_num

    @checked_voucher_num.setter
    def checked_voucher_num(self, value):
        self._checked_voucher_num = value
    @property
    def claim_voucher_num(self):
        return self._claim_voucher_num

    @claim_voucher_num.setter
    def claim_voucher_num(self, value):
        self._claim_voucher_num = value
    @property
    def commission_amount(self):
        return self._commission_amount

    @commission_amount.setter
    def commission_amount(self, value):
        self._commission_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.checked_voucher_num:
            if hasattr(self.checked_voucher_num, 'to_alipay_dict'):
                params['checked_voucher_num'] = self.checked_voucher_num.to_alipay_dict()
            else:
                params['checked_voucher_num'] = self.checked_voucher_num
        if self.claim_voucher_num:
            if hasattr(self.claim_voucher_num, 'to_alipay_dict'):
                params['claim_voucher_num'] = self.claim_voucher_num.to_alipay_dict()
            else:
                params['claim_voucher_num'] = self.claim_voucher_num
        if self.commission_amount:
            if hasattr(self.commission_amount, 'to_alipay_dict'):
                params['commission_amount'] = self.commission_amount.to_alipay_dict()
            else:
                params['commission_amount'] = self.commission_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoteDataModel()
        if 'checked_voucher_num' in d:
            o.checked_voucher_num = d['checked_voucher_num']
        if 'claim_voucher_num' in d:
            o.claim_voucher_num = d['claim_voucher_num']
        if 'commission_amount' in d:
            o.commission_amount = d['commission_amount']
        return o



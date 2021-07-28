#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherValidPeriodModify import VoucherValidPeriodModify


class VoucherUseRuleModify(object):

    def __init__(self):
        self._voucher_valid_period = None

    @property
    def voucher_valid_period(self):
        return self._voucher_valid_period

    @voucher_valid_period.setter
    def voucher_valid_period(self, value):
        if isinstance(value, VoucherValidPeriodModify):
            self._voucher_valid_period = value
        else:
            self._voucher_valid_period = VoucherValidPeriodModify.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_valid_period:
            if hasattr(self.voucher_valid_period, 'to_alipay_dict'):
                params['voucher_valid_period'] = self.voucher_valid_period.to_alipay_dict()
            else:
                params['voucher_valid_period'] = self.voucher_valid_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherUseRuleModify()
        if 'voucher_valid_period' in d:
            o.voucher_valid_period = d['voucher_valid_period']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExchangeVoucher import ExchangeVoucher
from alipay.aop.api.domain.FixVoucher import FixVoucher
from alipay.aop.api.domain.VoucherValidPeriod import VoucherValidPeriod


class VoucherUseRule(object):

    def __init__(self):
        self._exchange_voucher = None
        self._fix_voucher = None
        self._voucher_valid_period = None

    @property
    def exchange_voucher(self):
        return self._exchange_voucher

    @exchange_voucher.setter
    def exchange_voucher(self, value):
        if isinstance(value, ExchangeVoucher):
            self._exchange_voucher = value
        else:
            self._exchange_voucher = ExchangeVoucher.from_alipay_dict(value)
    @property
    def fix_voucher(self):
        return self._fix_voucher

    @fix_voucher.setter
    def fix_voucher(self, value):
        if isinstance(value, FixVoucher):
            self._fix_voucher = value
        else:
            self._fix_voucher = FixVoucher.from_alipay_dict(value)
    @property
    def voucher_valid_period(self):
        return self._voucher_valid_period

    @voucher_valid_period.setter
    def voucher_valid_period(self, value):
        if isinstance(value, VoucherValidPeriod):
            self._voucher_valid_period = value
        else:
            self._voucher_valid_period = VoucherValidPeriod.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.exchange_voucher:
            if hasattr(self.exchange_voucher, 'to_alipay_dict'):
                params['exchange_voucher'] = self.exchange_voucher.to_alipay_dict()
            else:
                params['exchange_voucher'] = self.exchange_voucher
        if self.fix_voucher:
            if hasattr(self.fix_voucher, 'to_alipay_dict'):
                params['fix_voucher'] = self.fix_voucher.to_alipay_dict()
            else:
                params['fix_voucher'] = self.fix_voucher
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
        o = VoucherUseRule()
        if 'exchange_voucher' in d:
            o.exchange_voucher = d['exchange_voucher']
        if 'fix_voucher' in d:
            o.fix_voucher = d['fix_voucher']
        if 'voucher_valid_period' in d:
            o.voucher_valid_period = d['voucher_valid_period']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExchangeVoucherModify import ExchangeVoucherModify
from alipay.aop.api.domain.VoucherAvailableScopeModify import VoucherAvailableScopeModify
from alipay.aop.api.domain.VoucherValidPeriodModify import VoucherValidPeriodModify


class VoucherUseRuleModify(object):

    def __init__(self):
        self._exchange_voucher = None
        self._voucher_available_scope = None
        self._voucher_valid_period = None

    @property
    def exchange_voucher(self):
        return self._exchange_voucher

    @exchange_voucher.setter
    def exchange_voucher(self, value):
        if isinstance(value, ExchangeVoucherModify):
            self._exchange_voucher = value
        else:
            self._exchange_voucher = ExchangeVoucherModify.from_alipay_dict(value)
    @property
    def voucher_available_scope(self):
        return self._voucher_available_scope

    @voucher_available_scope.setter
    def voucher_available_scope(self, value):
        if isinstance(value, VoucherAvailableScopeModify):
            self._voucher_available_scope = value
        else:
            self._voucher_available_scope = VoucherAvailableScopeModify.from_alipay_dict(value)
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
        if self.exchange_voucher:
            if hasattr(self.exchange_voucher, 'to_alipay_dict'):
                params['exchange_voucher'] = self.exchange_voucher.to_alipay_dict()
            else:
                params['exchange_voucher'] = self.exchange_voucher
        if self.voucher_available_scope:
            if hasattr(self.voucher_available_scope, 'to_alipay_dict'):
                params['voucher_available_scope'] = self.voucher_available_scope.to_alipay_dict()
            else:
                params['voucher_available_scope'] = self.voucher_available_scope
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
        if 'exchange_voucher' in d:
            o.exchange_voucher = d['exchange_voucher']
        if 'voucher_available_scope' in d:
            o.voucher_available_scope = d['voucher_available_scope']
        if 'voucher_valid_period' in d:
            o.voucher_valid_period = d['voucher_valid_period']
        return o



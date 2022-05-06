#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiscountVoucher import DiscountVoucher
from alipay.aop.api.domain.ExchangeVoucher import ExchangeVoucher
from alipay.aop.api.domain.FixVoucher import FixVoucher
from alipay.aop.api.domain.SpecialVoucher import SpecialVoucher
from alipay.aop.api.domain.VoucherAvailableScope import VoucherAvailableScope
from alipay.aop.api.domain.VoucherValidPeriod import VoucherValidPeriod


class VoucherUseRule(object):

    def __init__(self):
        self._discount_voucher = None
        self._exchange_voucher = None
        self._fix_voucher = None
        self._special_voucher = None
        self._voucher_available_scope = None
        self._voucher_valid_period = None

    @property
    def discount_voucher(self):
        return self._discount_voucher

    @discount_voucher.setter
    def discount_voucher(self, value):
        if isinstance(value, DiscountVoucher):
            self._discount_voucher = value
        else:
            self._discount_voucher = DiscountVoucher.from_alipay_dict(value)
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
    def special_voucher(self):
        return self._special_voucher

    @special_voucher.setter
    def special_voucher(self, value):
        if isinstance(value, SpecialVoucher):
            self._special_voucher = value
        else:
            self._special_voucher = SpecialVoucher.from_alipay_dict(value)
    @property
    def voucher_available_scope(self):
        return self._voucher_available_scope

    @voucher_available_scope.setter
    def voucher_available_scope(self, value):
        if isinstance(value, VoucherAvailableScope):
            self._voucher_available_scope = value
        else:
            self._voucher_available_scope = VoucherAvailableScope.from_alipay_dict(value)
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
        if self.discount_voucher:
            if hasattr(self.discount_voucher, 'to_alipay_dict'):
                params['discount_voucher'] = self.discount_voucher.to_alipay_dict()
            else:
                params['discount_voucher'] = self.discount_voucher
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
        if self.special_voucher:
            if hasattr(self.special_voucher, 'to_alipay_dict'):
                params['special_voucher'] = self.special_voucher.to_alipay_dict()
            else:
                params['special_voucher'] = self.special_voucher
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
        o = VoucherUseRule()
        if 'discount_voucher' in d:
            o.discount_voucher = d['discount_voucher']
        if 'exchange_voucher' in d:
            o.exchange_voucher = d['exchange_voucher']
        if 'fix_voucher' in d:
            o.fix_voucher = d['fix_voucher']
        if 'special_voucher' in d:
            o.special_voucher = d['special_voucher']
        if 'voucher_available_scope' in d:
            o.voucher_available_scope = d['voucher_available_scope']
        if 'voucher_valid_period' in d:
            o.voucher_valid_period = d['voucher_valid_period']
        return o



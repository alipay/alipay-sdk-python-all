#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityDiscountVoucher import ActivityDiscountVoucher
from alipay.aop.api.domain.ActivityExchangeVoucher import ActivityExchangeVoucher
from alipay.aop.api.domain.ActivityFixVoucher import ActivityFixVoucher
from alipay.aop.api.domain.ActivitySpecialVoucher import ActivitySpecialVoucher


class CommonVoucherUseRuleLiteInfo(object):

    def __init__(self):
        self._discount_voucher = None
        self._exchange_voucher = None
        self._fix_voucher = None
        self._special_voucher = None

    @property
    def discount_voucher(self):
        return self._discount_voucher

    @discount_voucher.setter
    def discount_voucher(self, value):
        if isinstance(value, ActivityDiscountVoucher):
            self._discount_voucher = value
        else:
            self._discount_voucher = ActivityDiscountVoucher.from_alipay_dict(value)
    @property
    def exchange_voucher(self):
        return self._exchange_voucher

    @exchange_voucher.setter
    def exchange_voucher(self, value):
        if isinstance(value, ActivityExchangeVoucher):
            self._exchange_voucher = value
        else:
            self._exchange_voucher = ActivityExchangeVoucher.from_alipay_dict(value)
    @property
    def fix_voucher(self):
        return self._fix_voucher

    @fix_voucher.setter
    def fix_voucher(self, value):
        if isinstance(value, ActivityFixVoucher):
            self._fix_voucher = value
        else:
            self._fix_voucher = ActivityFixVoucher.from_alipay_dict(value)
    @property
    def special_voucher(self):
        return self._special_voucher

    @special_voucher.setter
    def special_voucher(self, value):
        if isinstance(value, ActivitySpecialVoucher):
            self._special_voucher = value
        else:
            self._special_voucher = ActivitySpecialVoucher.from_alipay_dict(value)


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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommonVoucherUseRuleLiteInfo()
        if 'discount_voucher' in d:
            o.discount_voucher = d['discount_voucher']
        if 'exchange_voucher' in d:
            o.exchange_voucher = d['exchange_voucher']
        if 'fix_voucher' in d:
            o.fix_voucher = d['fix_voucher']
        if 'special_voucher' in d:
            o.special_voucher = d['special_voucher']
        return o



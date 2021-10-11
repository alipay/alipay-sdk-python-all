#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentFixVoucher import PaymentFixVoucher
from alipay.aop.api.domain.PaymentVoucherValidPeriod import PaymentVoucherValidPeriod


class PaymentVoucherUseRuleDetail(object):

    def __init__(self):
        self._fix_voucher = None
        self._use_mode = None
        self._use_url = None
        self._voucher_quantity_limit_per_user = None
        self._voucher_quantity_limit_per_user_period_type = None
        self._voucher_valid_period = None

    @property
    def fix_voucher(self):
        return self._fix_voucher

    @fix_voucher.setter
    def fix_voucher(self, value):
        if isinstance(value, PaymentFixVoucher):
            self._fix_voucher = value
        else:
            self._fix_voucher = PaymentFixVoucher.from_alipay_dict(value)
    @property
    def use_mode(self):
        return self._use_mode

    @use_mode.setter
    def use_mode(self, value):
        self._use_mode = value
    @property
    def use_url(self):
        return self._use_url

    @use_url.setter
    def use_url(self, value):
        self._use_url = value
    @property
    def voucher_quantity_limit_per_user(self):
        return self._voucher_quantity_limit_per_user

    @voucher_quantity_limit_per_user.setter
    def voucher_quantity_limit_per_user(self, value):
        self._voucher_quantity_limit_per_user = value
    @property
    def voucher_quantity_limit_per_user_period_type(self):
        return self._voucher_quantity_limit_per_user_period_type

    @voucher_quantity_limit_per_user_period_type.setter
    def voucher_quantity_limit_per_user_period_type(self, value):
        self._voucher_quantity_limit_per_user_period_type = value
    @property
    def voucher_valid_period(self):
        return self._voucher_valid_period

    @voucher_valid_period.setter
    def voucher_valid_period(self, value):
        if isinstance(value, PaymentVoucherValidPeriod):
            self._voucher_valid_period = value
        else:
            self._voucher_valid_period = PaymentVoucherValidPeriod.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.fix_voucher:
            if hasattr(self.fix_voucher, 'to_alipay_dict'):
                params['fix_voucher'] = self.fix_voucher.to_alipay_dict()
            else:
                params['fix_voucher'] = self.fix_voucher
        if self.use_mode:
            if hasattr(self.use_mode, 'to_alipay_dict'):
                params['use_mode'] = self.use_mode.to_alipay_dict()
            else:
                params['use_mode'] = self.use_mode
        if self.use_url:
            if hasattr(self.use_url, 'to_alipay_dict'):
                params['use_url'] = self.use_url.to_alipay_dict()
            else:
                params['use_url'] = self.use_url
        if self.voucher_quantity_limit_per_user:
            if hasattr(self.voucher_quantity_limit_per_user, 'to_alipay_dict'):
                params['voucher_quantity_limit_per_user'] = self.voucher_quantity_limit_per_user.to_alipay_dict()
            else:
                params['voucher_quantity_limit_per_user'] = self.voucher_quantity_limit_per_user
        if self.voucher_quantity_limit_per_user_period_type:
            if hasattr(self.voucher_quantity_limit_per_user_period_type, 'to_alipay_dict'):
                params['voucher_quantity_limit_per_user_period_type'] = self.voucher_quantity_limit_per_user_period_type.to_alipay_dict()
            else:
                params['voucher_quantity_limit_per_user_period_type'] = self.voucher_quantity_limit_per_user_period_type
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
        o = PaymentVoucherUseRuleDetail()
        if 'fix_voucher' in d:
            o.fix_voucher = d['fix_voucher']
        if 'use_mode' in d:
            o.use_mode = d['use_mode']
        if 'use_url' in d:
            o.use_url = d['use_url']
        if 'voucher_quantity_limit_per_user' in d:
            o.voucher_quantity_limit_per_user = d['voucher_quantity_limit_per_user']
        if 'voucher_quantity_limit_per_user_period_type' in d:
            o.voucher_quantity_limit_per_user_period_type = d['voucher_quantity_limit_per_user_period_type']
        if 'voucher_valid_period' in d:
            o.voucher_valid_period = d['voucher_valid_period']
        return o



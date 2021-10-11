#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentVoucherAlipayBalanceRechargeInfo import PaymentVoucherAlipayBalanceRechargeInfo


class PaymentVoucherRechargeInfo(object):

    def __init__(self):
        self._alipay_balance_recharge_info = None
        self._recharge_type = None

    @property
    def alipay_balance_recharge_info(self):
        return self._alipay_balance_recharge_info

    @alipay_balance_recharge_info.setter
    def alipay_balance_recharge_info(self, value):
        if isinstance(value, PaymentVoucherAlipayBalanceRechargeInfo):
            self._alipay_balance_recharge_info = value
        else:
            self._alipay_balance_recharge_info = PaymentVoucherAlipayBalanceRechargeInfo.from_alipay_dict(value)
    @property
    def recharge_type(self):
        return self._recharge_type

    @recharge_type.setter
    def recharge_type(self, value):
        self._recharge_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_balance_recharge_info:
            if hasattr(self.alipay_balance_recharge_info, 'to_alipay_dict'):
                params['alipay_balance_recharge_info'] = self.alipay_balance_recharge_info.to_alipay_dict()
            else:
                params['alipay_balance_recharge_info'] = self.alipay_balance_recharge_info
        if self.recharge_type:
            if hasattr(self.recharge_type, 'to_alipay_dict'):
                params['recharge_type'] = self.recharge_type.to_alipay_dict()
            else:
                params['recharge_type'] = self.recharge_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentVoucherRechargeInfo()
        if 'alipay_balance_recharge_info' in d:
            o.alipay_balance_recharge_info = d['alipay_balance_recharge_info']
        if 'recharge_type' in d:
            o.recharge_type = d['recharge_type']
        return o



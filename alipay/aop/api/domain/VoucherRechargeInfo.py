#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherBalanceRechargeInfo import VoucherBalanceRechargeInfo


class VoucherRechargeInfo(object):

    def __init__(self):
        self._recharge_type = None
        self._voucher_balance_recharge_info = None

    @property
    def recharge_type(self):
        return self._recharge_type

    @recharge_type.setter
    def recharge_type(self, value):
        self._recharge_type = value
    @property
    def voucher_balance_recharge_info(self):
        return self._voucher_balance_recharge_info

    @voucher_balance_recharge_info.setter
    def voucher_balance_recharge_info(self, value):
        if isinstance(value, VoucherBalanceRechargeInfo):
            self._voucher_balance_recharge_info = value
        else:
            self._voucher_balance_recharge_info = VoucherBalanceRechargeInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.recharge_type:
            if hasattr(self.recharge_type, 'to_alipay_dict'):
                params['recharge_type'] = self.recharge_type.to_alipay_dict()
            else:
                params['recharge_type'] = self.recharge_type
        if self.voucher_balance_recharge_info:
            if hasattr(self.voucher_balance_recharge_info, 'to_alipay_dict'):
                params['voucher_balance_recharge_info'] = self.voucher_balance_recharge_info.to_alipay_dict()
            else:
                params['voucher_balance_recharge_info'] = self.voucher_balance_recharge_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherRechargeInfo()
        if 'recharge_type' in d:
            o.recharge_type = d['recharge_type']
        if 'voucher_balance_recharge_info' in d:
            o.voucher_balance_recharge_info = d['voucher_balance_recharge_info']
        return o



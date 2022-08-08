#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherRechargeInfo import VoucherRechargeInfo


class VoucherBudgetSupplyInfo(object):

    def __init__(self):
        self._budget_type = None
        self._voucher_recharge_info = None

    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def voucher_recharge_info(self):
        return self._voucher_recharge_info

    @voucher_recharge_info.setter
    def voucher_recharge_info(self, value):
        if isinstance(value, VoucherRechargeInfo):
            self._voucher_recharge_info = value
        else:
            self._voucher_recharge_info = VoucherRechargeInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.voucher_recharge_info:
            if hasattr(self.voucher_recharge_info, 'to_alipay_dict'):
                params['voucher_recharge_info'] = self.voucher_recharge_info.to_alipay_dict()
            else:
                params['voucher_recharge_info'] = self.voucher_recharge_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherBudgetSupplyInfo()
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'voucher_recharge_info' in d:
            o.voucher_recharge_info = d['voucher_recharge_info']
        return o



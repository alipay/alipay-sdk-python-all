#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderVoucherAvailableScopeResult import OrderVoucherAvailableScopeResult


class OrderVoucherUseRuleResult(object):

    def __init__(self):
        self._voucher_available_scope_result = None

    @property
    def voucher_available_scope_result(self):
        return self._voucher_available_scope_result

    @voucher_available_scope_result.setter
    def voucher_available_scope_result(self, value):
        if isinstance(value, OrderVoucherAvailableScopeResult):
            self._voucher_available_scope_result = value
        else:
            self._voucher_available_scope_result = OrderVoucherAvailableScopeResult.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_available_scope_result:
            if hasattr(self.voucher_available_scope_result, 'to_alipay_dict'):
                params['voucher_available_scope_result'] = self.voucher_available_scope_result.to_alipay_dict()
            else:
                params['voucher_available_scope_result'] = self.voucher_available_scope_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderVoucherUseRuleResult()
        if 'voucher_available_scope_result' in d:
            o.voucher_available_scope_result = d['voucher_available_scope_result']
        return o



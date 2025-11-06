#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivePayAndPrepayReverseCancelOpenApiOrder import ActivePayAndPrepayReverseCancelOpenApiOrder


class AlipayBossFncGfsettleprodPayandprepayreverseCancelModel(object):

    def __init__(self):
        self._active_pay_and_prepay_reverse_cancel_open_api_order = None

    @property
    def active_pay_and_prepay_reverse_cancel_open_api_order(self):
        return self._active_pay_and_prepay_reverse_cancel_open_api_order

    @active_pay_and_prepay_reverse_cancel_open_api_order.setter
    def active_pay_and_prepay_reverse_cancel_open_api_order(self, value):
        if isinstance(value, ActivePayAndPrepayReverseCancelOpenApiOrder):
            self._active_pay_and_prepay_reverse_cancel_open_api_order = value
        else:
            self._active_pay_and_prepay_reverse_cancel_open_api_order = ActivePayAndPrepayReverseCancelOpenApiOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.active_pay_and_prepay_reverse_cancel_open_api_order:
            if hasattr(self.active_pay_and_prepay_reverse_cancel_open_api_order, 'to_alipay_dict'):
                params['active_pay_and_prepay_reverse_cancel_open_api_order'] = self.active_pay_and_prepay_reverse_cancel_open_api_order.to_alipay_dict()
            else:
                params['active_pay_and_prepay_reverse_cancel_open_api_order'] = self.active_pay_and_prepay_reverse_cancel_open_api_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodPayandprepayreverseCancelModel()
        if 'active_pay_and_prepay_reverse_cancel_open_api_order' in d:
            o.active_pay_and_prepay_reverse_cancel_open_api_order = d['active_pay_and_prepay_reverse_cancel_open_api_order']
        return o



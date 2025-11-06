#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrePayApplyCancelOrder import PrePayApplyCancelOrder


class AlipayBossFncGfsettleprodPrepaymentCancelModel(object):

    def __init__(self):
        self._prepay_apply_cancel_order = None

    @property
    def prepay_apply_cancel_order(self):
        return self._prepay_apply_cancel_order

    @prepay_apply_cancel_order.setter
    def prepay_apply_cancel_order(self, value):
        if isinstance(value, PrePayApplyCancelOrder):
            self._prepay_apply_cancel_order = value
        else:
            self._prepay_apply_cancel_order = PrePayApplyCancelOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.prepay_apply_cancel_order:
            if hasattr(self.prepay_apply_cancel_order, 'to_alipay_dict'):
                params['prepay_apply_cancel_order'] = self.prepay_apply_cancel_order.to_alipay_dict()
            else:
                params['prepay_apply_cancel_order'] = self.prepay_apply_cancel_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodPrepaymentCancelModel()
        if 'prepay_apply_cancel_order' in d:
            o.prepay_apply_cancel_order = d['prepay_apply_cancel_order']
        return o



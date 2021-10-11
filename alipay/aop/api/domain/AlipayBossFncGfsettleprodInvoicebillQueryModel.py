#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentApplyQueryOrder import PaymentApplyQueryOrder


class AlipayBossFncGfsettleprodInvoicebillQueryModel(object):

    def __init__(self):
        self._payment_apply_query_order = None

    @property
    def payment_apply_query_order(self):
        return self._payment_apply_query_order

    @payment_apply_query_order.setter
    def payment_apply_query_order(self, value):
        if isinstance(value, PaymentApplyQueryOrder):
            self._payment_apply_query_order = value
        else:
            self._payment_apply_query_order = PaymentApplyQueryOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.payment_apply_query_order:
            if hasattr(self.payment_apply_query_order, 'to_alipay_dict'):
                params['payment_apply_query_order'] = self.payment_apply_query_order.to_alipay_dict()
            else:
                params['payment_apply_query_order'] = self.payment_apply_query_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodInvoicebillQueryModel()
        if 'payment_apply_query_order' in d:
            o.payment_apply_query_order = d['payment_apply_query_order']
        return o



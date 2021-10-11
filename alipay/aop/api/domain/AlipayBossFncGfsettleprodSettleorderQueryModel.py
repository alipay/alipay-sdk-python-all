#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApSettleOrderQueryOrder import ApSettleOrderQueryOrder


class AlipayBossFncGfsettleprodSettleorderQueryModel(object):

    def __init__(self):
        self._ap_settle_order_query_order = None

    @property
    def ap_settle_order_query_order(self):
        return self._ap_settle_order_query_order

    @ap_settle_order_query_order.setter
    def ap_settle_order_query_order(self, value):
        if isinstance(value, ApSettleOrderQueryOrder):
            self._ap_settle_order_query_order = value
        else:
            self._ap_settle_order_query_order = ApSettleOrderQueryOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ap_settle_order_query_order:
            if hasattr(self.ap_settle_order_query_order, 'to_alipay_dict'):
                params['ap_settle_order_query_order'] = self.ap_settle_order_query_order.to_alipay_dict()
            else:
                params['ap_settle_order_query_order'] = self.ap_settle_order_query_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodSettleorderQueryModel()
        if 'ap_settle_order_query_order' in d:
            o.ap_settle_order_query_order = d['ap_settle_order_query_order']
        return o



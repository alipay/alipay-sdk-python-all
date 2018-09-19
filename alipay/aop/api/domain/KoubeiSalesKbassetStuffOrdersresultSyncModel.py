#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessOrdersFeedBack import AccessOrdersFeedBack


class KoubeiSalesKbassetStuffOrdersresultSyncModel(object):

    def __init__(self):
        self._orders_feedback = None

    @property
    def orders_feedback(self):
        return self._orders_feedback

    @orders_feedback.setter
    def orders_feedback(self, value):
        if isinstance(value, list):
            self._orders_feedback = list()
            for i in value:
                if isinstance(i, AccessOrdersFeedBack):
                    self._orders_feedback.append(i)
                else:
                    self._orders_feedback.append(AccessOrdersFeedBack.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.orders_feedback:
            if isinstance(self.orders_feedback, list):
                for i in range(0, len(self.orders_feedback)):
                    element = self.orders_feedback[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.orders_feedback[i] = element.to_alipay_dict()
            if hasattr(self.orders_feedback, 'to_alipay_dict'):
                params['orders_feedback'] = self.orders_feedback.to_alipay_dict()
            else:
                params['orders_feedback'] = self.orders_feedback
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesKbassetStuffOrdersresultSyncModel()
        if 'orders_feedback' in d:
            o.orders_feedback = d['orders_feedback']
        return o



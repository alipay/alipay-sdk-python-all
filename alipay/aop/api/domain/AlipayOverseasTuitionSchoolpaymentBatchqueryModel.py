#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionQueryOrder import TuitionQueryOrder


class AlipayOverseasTuitionSchoolpaymentBatchqueryModel(object):

    def __init__(self):
        self._isv_pid = None
        self._pass_through_info = None
        self._payment_orders = None

    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def payment_orders(self):
        return self._payment_orders

    @payment_orders.setter
    def payment_orders(self, value):
        if isinstance(value, list):
            self._payment_orders = list()
            for i in value:
                if isinstance(i, TuitionQueryOrder):
                    self._payment_orders.append(i)
                else:
                    self._payment_orders.append(TuitionQueryOrder.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.pass_through_info:
            if hasattr(self.pass_through_info, 'to_alipay_dict'):
                params['pass_through_info'] = self.pass_through_info.to_alipay_dict()
            else:
                params['pass_through_info'] = self.pass_through_info
        if self.payment_orders:
            if isinstance(self.payment_orders, list):
                for i in range(0, len(self.payment_orders)):
                    element = self.payment_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_orders[i] = element.to_alipay_dict()
            if hasattr(self.payment_orders, 'to_alipay_dict'):
                params['payment_orders'] = self.payment_orders.to_alipay_dict()
            else:
                params['payment_orders'] = self.payment_orders
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTuitionSchoolpaymentBatchqueryModel()
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        if 'payment_orders' in d:
            o.payment_orders = d['payment_orders']
        return o



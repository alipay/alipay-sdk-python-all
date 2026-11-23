#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderList import OrderList


class OutAgentRiskInfo(object):

    def __init__(self):
        self._busi_pid_count = None
        self._order_list = None

    @property
    def busi_pid_count(self):
        return self._busi_pid_count

    @busi_pid_count.setter
    def busi_pid_count(self, value):
        self._busi_pid_count = value
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, OrderList):
                    self._order_list.append(i)
                else:
                    self._order_list.append(OrderList.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.busi_pid_count:
            if hasattr(self.busi_pid_count, 'to_alipay_dict'):
                params['busi_pid_count'] = self.busi_pid_count.to_alipay_dict()
            else:
                params['busi_pid_count'] = self.busi_pid_count
        if self.order_list:
            if isinstance(self.order_list, list):
                for i in range(0, len(self.order_list)):
                    element = self.order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_list[i] = element.to_alipay_dict()
            if hasattr(self.order_list, 'to_alipay_dict'):
                params['order_list'] = self.order_list.to_alipay_dict()
            else:
                params['order_list'] = self.order_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutAgentRiskInfo()
        if 'busi_pid_count' in d:
            o.busi_pid_count = d['busi_pid_count']
        if 'order_list' in d:
            o.order_list = d['order_list']
        return o



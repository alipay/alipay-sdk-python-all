#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcOrderItem import EcOrderItem
from alipay.aop.api.domain.EcOrderItem import EcOrderItem


class EcOrderInfo(object):

    def __init__(self):
        self._order_info = None
        self._sub_order_list = None

    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        if isinstance(value, EcOrderItem):
            self._order_info = value
        else:
            self._order_info = EcOrderItem.from_alipay_dict(value)
    @property
    def sub_order_list(self):
        return self._sub_order_list

    @sub_order_list.setter
    def sub_order_list(self, value):
        if isinstance(value, list):
            self._sub_order_list = list()
            for i in value:
                if isinstance(i, EcOrderItem):
                    self._sub_order_list.append(i)
                else:
                    self._sub_order_list.append(EcOrderItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.order_info:
            if hasattr(self.order_info, 'to_alipay_dict'):
                params['order_info'] = self.order_info.to_alipay_dict()
            else:
                params['order_info'] = self.order_info
        if self.sub_order_list:
            if isinstance(self.sub_order_list, list):
                for i in range(0, len(self.sub_order_list)):
                    element = self.sub_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_order_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_order_list, 'to_alipay_dict'):
                params['sub_order_list'] = self.sub_order_list.to_alipay_dict()
            else:
                params['sub_order_list'] = self.sub_order_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcOrderInfo()
        if 'order_info' in d:
            o.order_info = d['order_info']
        if 'sub_order_list' in d:
            o.sub_order_list = d['sub_order_list']
        return o



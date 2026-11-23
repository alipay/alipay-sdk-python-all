#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderList(object):

    def __init__(self):
        self._order_amount_list = None
        self._partner_id = None
        self._risk_level = None

    @property
    def order_amount_list(self):
        return self._order_amount_list

    @order_amount_list.setter
    def order_amount_list(self, value):
        if isinstance(value, list):
            self._order_amount_list = list()
            for i in value:
                self._order_amount_list.append(i)
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_amount_list:
            if isinstance(self.order_amount_list, list):
                for i in range(0, len(self.order_amount_list)):
                    element = self.order_amount_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_amount_list[i] = element.to_alipay_dict()
            if hasattr(self.order_amount_list, 'to_alipay_dict'):
                params['order_amount_list'] = self.order_amount_list.to_alipay_dict()
            else:
                params['order_amount_list'] = self.order_amount_list
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderList()
        if 'order_amount_list' in d:
            o.order_amount_list = d['order_amount_list']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        return o



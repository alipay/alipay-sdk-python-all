#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReceiptSimpleOrderDTO import ReceiptSimpleOrderDTO


class AlipayCommerceReceiptSyncModel(object):

    def __init__(self):
        self._order_list = None

    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, ReceiptSimpleOrderDTO):
                    self._order_list.append(i)
                else:
                    self._order_list.append(ReceiptSimpleOrderDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayCommerceReceiptSyncModel()
        if 'order_list' in d:
            o.order_list = d['order_list']
        return o



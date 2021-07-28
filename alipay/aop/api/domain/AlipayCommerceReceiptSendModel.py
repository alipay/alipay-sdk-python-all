#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReceiptOrderDTO import ReceiptOrderDTO


class AlipayCommerceReceiptSendModel(object):

    def __init__(self):
        self._order_list = None
        self._record_id = None

    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, ReceiptOrderDTO):
                    self._order_list.append(i)
                else:
                    self._order_list.append(ReceiptOrderDTO.from_alipay_dict(i))
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value


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
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceReceiptSendModel()
        if 'order_list' in d:
            o.order_list = d['order_list']
        if 'record_id' in d:
            o.record_id = d['record_id']
        return o



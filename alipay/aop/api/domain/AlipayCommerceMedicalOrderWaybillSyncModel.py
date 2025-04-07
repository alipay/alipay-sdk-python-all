#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WaybillItemVO import WaybillItemVO


class AlipayCommerceMedicalOrderWaybillSyncModel(object):

    def __init__(self):
        self._carrier_order_no = None
        self._items = None
        self._order_no = None

    @property
    def carrier_order_no(self):
        return self._carrier_order_no

    @carrier_order_no.setter
    def carrier_order_no(self, value):
        self._carrier_order_no = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, WaybillItemVO):
                    self._items.append(i)
                else:
                    self._items.append(WaybillItemVO.from_alipay_dict(i))
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.carrier_order_no:
            if hasattr(self.carrier_order_no, 'to_alipay_dict'):
                params['carrier_order_no'] = self.carrier_order_no.to_alipay_dict()
            else:
                params['carrier_order_no'] = self.carrier_order_no
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOrderWaybillSyncModel()
        if 'carrier_order_no' in d:
            o.carrier_order_no = d['carrier_order_no']
        if 'items' in d:
            o.items = d['items']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o



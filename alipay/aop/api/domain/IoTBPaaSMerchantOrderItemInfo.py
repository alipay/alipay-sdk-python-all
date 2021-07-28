#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IoTBPaaSKeyValue import IoTBPaaSKeyValue
from alipay.aop.api.domain.IoTBPaaSKeyValue import IoTBPaaSKeyValue


class IoTBPaaSMerchantOrderItemInfo(object):

    def __init__(self):
        self._attrs = None
        self._item_name = None
        self._item_num = None
        self._item_price = None
        self._specs = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, list):
            self._attrs = list()
            for i in value:
                if isinstance(i, IoTBPaaSKeyValue):
                    self._attrs.append(i)
                else:
                    self._attrs.append(IoTBPaaSKeyValue.from_alipay_dict(i))
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value
    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def specs(self):
        return self._specs

    @specs.setter
    def specs(self, value):
        if isinstance(value, list):
            self._specs = list()
            for i in value:
                if isinstance(i, IoTBPaaSKeyValue):
                    self._specs.append(i)
                else:
                    self._specs.append(IoTBPaaSKeyValue.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.attrs:
            if isinstance(self.attrs, list):
                for i in range(0, len(self.attrs)):
                    element = self.attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attrs[i] = element.to_alipay_dict()
            if hasattr(self.attrs, 'to_alipay_dict'):
                params['attrs'] = self.attrs.to_alipay_dict()
            else:
                params['attrs'] = self.attrs
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_num:
            if hasattr(self.item_num, 'to_alipay_dict'):
                params['item_num'] = self.item_num.to_alipay_dict()
            else:
                params['item_num'] = self.item_num
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.specs:
            if isinstance(self.specs, list):
                for i in range(0, len(self.specs)):
                    element = self.specs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.specs[i] = element.to_alipay_dict()
            if hasattr(self.specs, 'to_alipay_dict'):
                params['specs'] = self.specs.to_alipay_dict()
            else:
                params['specs'] = self.specs
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IoTBPaaSMerchantOrderItemInfo()
        if 'attrs' in d:
            o.attrs = d['attrs']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'specs' in d:
            o.specs = d['specs']
        return o



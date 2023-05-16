#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DynamicAttributeVO import DynamicAttributeVO
from alipay.aop.api.domain.ItemDynamicQueryOrder import ItemDynamicQueryOrder


class DynamicDataVO(object):

    def __init__(self):
        self._attribute_list = None
        self._order = None

    @property
    def attribute_list(self):
        return self._attribute_list

    @attribute_list.setter
    def attribute_list(self, value):
        if isinstance(value, list):
            self._attribute_list = list()
            for i in value:
                if isinstance(i, DynamicAttributeVO):
                    self._attribute_list.append(i)
                else:
                    self._attribute_list.append(DynamicAttributeVO.from_alipay_dict(i))
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        if isinstance(value, ItemDynamicQueryOrder):
            self._order = value
        else:
            self._order = ItemDynamicQueryOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.attribute_list:
            if isinstance(self.attribute_list, list):
                for i in range(0, len(self.attribute_list)):
                    element = self.attribute_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attribute_list[i] = element.to_alipay_dict()
            if hasattr(self.attribute_list, 'to_alipay_dict'):
                params['attribute_list'] = self.attribute_list.to_alipay_dict()
            else:
                params['attribute_list'] = self.attribute_list
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DynamicDataVO()
        if 'attribute_list' in d:
            o.attribute_list = d['attribute_list']
        if 'order' in d:
            o.order = d['order']
        return o



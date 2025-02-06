#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleQcReportCheckItem import RecycleQcReportCheckItem


class RecycleQcReportCheckItems(object):

    def __init__(self):
        self._attr_name = None
        self._items = None

    @property
    def attr_name(self):
        return self._attr_name

    @attr_name.setter
    def attr_name(self, value):
        self._attr_name = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, RecycleQcReportCheckItem):
                    self._items.append(i)
                else:
                    self._items.append(RecycleQcReportCheckItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.attr_name:
            if hasattr(self.attr_name, 'to_alipay_dict'):
                params['attr_name'] = self.attr_name.to_alipay_dict()
            else:
                params['attr_name'] = self.attr_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleQcReportCheckItems()
        if 'attr_name' in d:
            o.attr_name = d['attr_name']
        if 'items' in d:
            o.items = d['items']
        return o



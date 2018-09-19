#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemUnitInfo import ItemUnitInfo


class ItemPackageInfo(object):

    def __init__(self):
        self._item_units = None
        self._title = None

    @property
    def item_units(self):
        return self._item_units

    @item_units.setter
    def item_units(self, value):
        if isinstance(value, list):
            self._item_units = list()
            for i in value:
                if isinstance(i, ItemUnitInfo):
                    self._item_units.append(i)
                else:
                    self._item_units.append(ItemUnitInfo.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_units:
            if isinstance(self.item_units, list):
                for i in range(0, len(self.item_units)):
                    element = self.item_units[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_units[i] = element.to_alipay_dict()
            if hasattr(self.item_units, 'to_alipay_dict'):
                params['item_units'] = self.item_units.to_alipay_dict()
            else:
                params['item_units'] = self.item_units
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemPackageInfo()
        if 'item_units' in d:
            o.item_units = d['item_units']
        if 'title' in d:
            o.title = d['title']
        return o



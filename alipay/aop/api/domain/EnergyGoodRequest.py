#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnergyExtRequest import EnergyExtRequest


class EnergyGoodRequest(object):

    def __init__(self):
        self._full_energy = None
        self._item_name = None
        self._items = None
        self._quantity = None

    @property
    def full_energy(self):
        return self._full_energy

    @full_energy.setter
    def full_energy(self, value):
        self._full_energy = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, EnergyExtRequest):
                    self._items.append(i)
                else:
                    self._items.append(EnergyExtRequest.from_alipay_dict(i))
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.full_energy:
            if hasattr(self.full_energy, 'to_alipay_dict'):
                params['full_energy'] = self.full_energy.to_alipay_dict()
            else:
                params['full_energy'] = self.full_energy
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
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
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnergyGoodRequest()
        if 'full_energy' in d:
            o.full_energy = d['full_energy']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'items' in d:
            o.items = d['items']
        if 'quantity' in d:
            o.quantity = d['quantity']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnergyExtRequest import EnergyExtRequest


class EnergyQueryRsp(object):

    def __init__(self):
        self._failed_msg = None
        self._full_energy = None
        self._item_name = None
        self._items = None
        self._result = None

    @property
    def failed_msg(self):
        return self._failed_msg

    @failed_msg.setter
    def failed_msg(self, value):
        self._failed_msg = value
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
        if isinstance(value, EnergyExtRequest):
            self._items = value
        else:
            self._items = EnergyExtRequest.from_alipay_dict(value)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.failed_msg:
            if hasattr(self.failed_msg, 'to_alipay_dict'):
                params['failed_msg'] = self.failed_msg.to_alipay_dict()
            else:
                params['failed_msg'] = self.failed_msg
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
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnergyQueryRsp()
        if 'failed_msg' in d:
            o.failed_msg = d['failed_msg']
        if 'full_energy' in d:
            o.full_energy = d['full_energy']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'items' in d:
            o.items = d['items']
        if 'result' in d:
            o.result = d['result']
        return o



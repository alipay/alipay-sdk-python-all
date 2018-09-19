#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetReverseGoodsItem(object):

    def __init__(self):
        self._memo = None
        self._phase = None
        self._reverse_apply_order_id = None
        self._reverse_apply_order_item_id = None
        self._type = None
        self._value = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value):
        self._phase = value
    @property
    def reverse_apply_order_id(self):
        return self._reverse_apply_order_id

    @reverse_apply_order_id.setter
    def reverse_apply_order_id(self, value):
        self._reverse_apply_order_id = value
    @property
    def reverse_apply_order_item_id(self):
        return self._reverse_apply_order_item_id

    @reverse_apply_order_item_id.setter
    def reverse_apply_order_item_id(self, value):
        self._reverse_apply_order_item_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.phase:
            if hasattr(self.phase, 'to_alipay_dict'):
                params['phase'] = self.phase.to_alipay_dict()
            else:
                params['phase'] = self.phase
        if self.reverse_apply_order_id:
            if hasattr(self.reverse_apply_order_id, 'to_alipay_dict'):
                params['reverse_apply_order_id'] = self.reverse_apply_order_id.to_alipay_dict()
            else:
                params['reverse_apply_order_id'] = self.reverse_apply_order_id
        if self.reverse_apply_order_item_id:
            if hasattr(self.reverse_apply_order_item_id, 'to_alipay_dict'):
                params['reverse_apply_order_item_id'] = self.reverse_apply_order_item_id.to_alipay_dict()
            else:
                params['reverse_apply_order_item_id'] = self.reverse_apply_order_item_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetReverseGoodsItem()
        if 'memo' in d:
            o.memo = d['memo']
        if 'phase' in d:
            o.phase = d['phase']
        if 'reverse_apply_order_id' in d:
            o.reverse_apply_order_id = d['reverse_apply_order_id']
        if 'reverse_apply_order_item_id' in d:
            o.reverse_apply_order_item_id = d['reverse_apply_order_item_id']
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o



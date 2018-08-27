#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosOrderKey import PosOrderKey


class KoubeiCateringOrderBillCancelModel(object):

    def __init__(self):
        self._action = None
        self._cancel_time = None
        self._pos_order_key = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def pos_order_key(self):
        return self._pos_order_key

    @pos_order_key.setter
    def pos_order_key(self, value):
        if isinstance(value, PosOrderKey):
            self._pos_order_key = value
        else:
            self._pos_order_key = PosOrderKey.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.pos_order_key:
            if hasattr(self.pos_order_key, 'to_alipay_dict'):
                params['pos_order_key'] = self.pos_order_key.to_alipay_dict()
            else:
                params['pos_order_key'] = self.pos_order_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderBillCancelModel()
        if 'action' in d:
            o.action = d['action']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'pos_order_key' in d:
            o.pos_order_key = d['pos_order_key']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosOrderKey import PosOrderKey


class KoubeiCateringOrderInfoCancelModel(object):

    def __init__(self):
        self._close_time = None
        self._pos_order_key = None

    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
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
        if self.close_time:
            if hasattr(self.close_time, 'to_alipay_dict'):
                params['close_time'] = self.close_time.to_alipay_dict()
            else:
                params['close_time'] = self.close_time
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
        o = KoubeiCateringOrderInfoCancelModel()
        if 'close_time' in d:
            o.close_time = d['close_time']
        if 'pos_order_key' in d:
            o.pos_order_key = d['pos_order_key']
        return o



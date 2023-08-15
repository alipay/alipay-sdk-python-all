#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniOrderExtInfoDTO(object):

    def __init__(self):
        self._door_time = None
        self._order_str = None

    @property
    def door_time(self):
        return self._door_time

    @door_time.setter
    def door_time(self, value):
        self._door_time = value
    @property
    def order_str(self):
        return self._order_str

    @order_str.setter
    def order_str(self, value):
        self._order_str = value


    def to_alipay_dict(self):
        params = dict()
        if self.door_time:
            if hasattr(self.door_time, 'to_alipay_dict'):
                params['door_time'] = self.door_time.to_alipay_dict()
            else:
                params['door_time'] = self.door_time
        if self.order_str:
            if hasattr(self.order_str, 'to_alipay_dict'):
                params['order_str'] = self.order_str.to_alipay_dict()
            else:
                params['order_str'] = self.order_str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniOrderExtInfoDTO()
        if 'door_time' in d:
            o.door_time = d['door_time']
        if 'order_str' in d:
            o.order_str = d['order_str']
        return o



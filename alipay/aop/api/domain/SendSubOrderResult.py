#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SendSubOrderResult(object):

    def __init__(self):
        self._order_expire_time = None
        self._order_id = None

    @property
    def order_expire_time(self):
        return self._order_expire_time

    @order_expire_time.setter
    def order_expire_time(self, value):
        self._order_expire_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_expire_time:
            if hasattr(self.order_expire_time, 'to_alipay_dict'):
                params['order_expire_time'] = self.order_expire_time.to_alipay_dict()
            else:
                params['order_expire_time'] = self.order_expire_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SendSubOrderResult()
        if 'order_expire_time' in d:
            o.order_expire_time = d['order_expire_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o



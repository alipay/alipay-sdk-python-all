#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TargetSendOrderParam(object):

    def __init__(self):
        self._camp_order_id = None
        self._interest_id = None
        self._send_order_id = None

    @property
    def camp_order_id(self):
        return self._camp_order_id

    @camp_order_id.setter
    def camp_order_id(self, value):
        self._camp_order_id = value
    @property
    def interest_id(self):
        return self._interest_id

    @interest_id.setter
    def interest_id(self, value):
        self._interest_id = value
    @property
    def send_order_id(self):
        return self._send_order_id

    @send_order_id.setter
    def send_order_id(self, value):
        self._send_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_order_id:
            if hasattr(self.camp_order_id, 'to_alipay_dict'):
                params['camp_order_id'] = self.camp_order_id.to_alipay_dict()
            else:
                params['camp_order_id'] = self.camp_order_id
        if self.interest_id:
            if hasattr(self.interest_id, 'to_alipay_dict'):
                params['interest_id'] = self.interest_id.to_alipay_dict()
            else:
                params['interest_id'] = self.interest_id
        if self.send_order_id:
            if hasattr(self.send_order_id, 'to_alipay_dict'):
                params['send_order_id'] = self.send_order_id.to_alipay_dict()
            else:
                params['send_order_id'] = self.send_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TargetSendOrderParam()
        if 'camp_order_id' in d:
            o.camp_order_id = d['camp_order_id']
        if 'interest_id' in d:
            o.interest_id = d['interest_id']
        if 'send_order_id' in d:
            o.send_order_id = d['send_order_id']
        return o



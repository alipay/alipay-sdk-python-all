#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AttachGoodReq(object):

    def __init__(self):
        self._attach_good_id = None
        self._quantity = None

    @property
    def attach_good_id(self):
        return self._attach_good_id

    @attach_good_id.setter
    def attach_good_id(self, value):
        self._attach_good_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.attach_good_id:
            if hasattr(self.attach_good_id, 'to_alipay_dict'):
                params['attach_good_id'] = self.attach_good_id.to_alipay_dict()
            else:
                params['attach_good_id'] = self.attach_good_id
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
        o = AttachGoodReq()
        if 'attach_good_id' in d:
            o.attach_good_id = d['attach_good_id']
        if 'quantity' in d:
            o.quantity = d['quantity']
        return o



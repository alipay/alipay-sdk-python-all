#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentInfoWithId(object):

    def __init__(self):
        self._payment_ids = None
        self._type = None

    @property
    def payment_ids(self):
        return self._payment_ids

    @payment_ids.setter
    def payment_ids(self, value):
        if isinstance(value, list):
            self._payment_ids = list()
            for i in value:
                self._payment_ids.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.payment_ids:
            if isinstance(self.payment_ids, list):
                for i in range(0, len(self.payment_ids)):
                    element = self.payment_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_ids[i] = element.to_alipay_dict()
            if hasattr(self.payment_ids, 'to_alipay_dict'):
                params['payment_ids'] = self.payment_ids.to_alipay_dict()
            else:
                params['payment_ids'] = self.payment_ids
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentInfoWithId()
        if 'payment_ids' in d:
            o.payment_ids = d['payment_ids']
        if 'type' in d:
            o.type = d['type']
        return o



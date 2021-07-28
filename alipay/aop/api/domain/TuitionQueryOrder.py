#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TuitionQueryOrder(object):

    def __init__(self):
        self._alipay_payment_id = None
        self._isv_payment_id = None

    @property
    def alipay_payment_id(self):
        return self._alipay_payment_id

    @alipay_payment_id.setter
    def alipay_payment_id(self, value):
        self._alipay_payment_id = value
    @property
    def isv_payment_id(self):
        return self._isv_payment_id

    @isv_payment_id.setter
    def isv_payment_id(self, value):
        self._isv_payment_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_payment_id:
            if hasattr(self.alipay_payment_id, 'to_alipay_dict'):
                params['alipay_payment_id'] = self.alipay_payment_id.to_alipay_dict()
            else:
                params['alipay_payment_id'] = self.alipay_payment_id
        if self.isv_payment_id:
            if hasattr(self.isv_payment_id, 'to_alipay_dict'):
                params['isv_payment_id'] = self.isv_payment_id.to_alipay_dict()
            else:
                params['isv_payment_id'] = self.isv_payment_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionQueryOrder()
        if 'alipay_payment_id' in d:
            o.alipay_payment_id = d['alipay_payment_id']
        if 'isv_payment_id' in d:
            o.isv_payment_id = d['isv_payment_id']
        return o



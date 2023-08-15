#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudGeneralsaasOnepassInitializeModel(object):

    def __init__(self):
        self._outer_order_no = None
        self._phone = None

    @property
    def outer_order_no(self):
        return self._outer_order_no

    @outer_order_no.setter
    def outer_order_no(self, value):
        self._outer_order_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.outer_order_no:
            if hasattr(self.outer_order_no, 'to_alipay_dict'):
                params['outer_order_no'] = self.outer_order_no.to_alipay_dict()
            else:
                params['outer_order_no'] = self.outer_order_no
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudGeneralsaasOnepassInitializeModel()
        if 'outer_order_no' in d:
            o.outer_order_no = d['outer_order_no']
        if 'phone' in d:
            o.phone = d['phone']
        return o



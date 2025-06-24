#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalRegisterCancelorderNotifyModel(object):

    def __init__(self):
        self._number_no = None
        self._order_id = None
        self._platform_code = None
        self._register_id = None

    @property
    def number_no(self):
        return self._number_no

    @number_no.setter
    def number_no(self, value):
        self._number_no = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.number_no:
            if hasattr(self.number_no, 'to_alipay_dict'):
                params['number_no'] = self.number_no.to_alipay_dict()
            else:
                params['number_no'] = self.number_no
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.register_id:
            if hasattr(self.register_id, 'to_alipay_dict'):
                params['register_id'] = self.register_id.to_alipay_dict()
            else:
                params['register_id'] = self.register_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalRegisterCancelorderNotifyModel()
        if 'number_no' in d:
            o.number_no = d['number_no']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'register_id' in d:
            o.register_id = d['register_id']
        return o



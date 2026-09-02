#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSaasAccountModifyModel(object):

    def __init__(self):
        self._customer_id = None
        self._enterprise_registration_no = None
        self._out_merchant_name = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def enterprise_registration_no(self):
        return self._enterprise_registration_no

    @enterprise_registration_no.setter
    def enterprise_registration_no(self, value):
        self._enterprise_registration_no = value
    @property
    def out_merchant_name(self):
        return self._out_merchant_name

    @out_merchant_name.setter
    def out_merchant_name(self, value):
        self._out_merchant_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.enterprise_registration_no:
            if hasattr(self.enterprise_registration_no, 'to_alipay_dict'):
                params['enterprise_registration_no'] = self.enterprise_registration_no.to_alipay_dict()
            else:
                params['enterprise_registration_no'] = self.enterprise_registration_no
        if self.out_merchant_name:
            if hasattr(self.out_merchant_name, 'to_alipay_dict'):
                params['out_merchant_name'] = self.out_merchant_name.to_alipay_dict()
            else:
                params['out_merchant_name'] = self.out_merchant_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSaasAccountModifyModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'enterprise_registration_no' in d:
            o.enterprise_registration_no = d['enterprise_registration_no']
        if 'out_merchant_name' in d:
            o.out_merchant_name = d['out_merchant_name']
        return o



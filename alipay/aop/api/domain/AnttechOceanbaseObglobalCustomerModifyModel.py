#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UpdateCustomerRequest import UpdateCustomerRequest


class AnttechOceanbaseObglobalCustomerModifyModel(object):

    def __init__(self):
        self._update_customer_request = None

    @property
    def update_customer_request(self):
        return self._update_customer_request

    @update_customer_request.setter
    def update_customer_request(self, value):
        if isinstance(value, UpdateCustomerRequest):
            self._update_customer_request = value
        else:
            self._update_customer_request = UpdateCustomerRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.update_customer_request:
            if hasattr(self.update_customer_request, 'to_alipay_dict'):
                params['update_customer_request'] = self.update_customer_request.to_alipay_dict()
            else:
                params['update_customer_request'] = self.update_customer_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalCustomerModifyModel()
        if 'update_customer_request' in d:
            o.update_customer_request = d['update_customer_request']
        return o



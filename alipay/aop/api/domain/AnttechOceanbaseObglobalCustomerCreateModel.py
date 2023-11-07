#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreateCustomerRequest import CreateCustomerRequest


class AnttechOceanbaseObglobalCustomerCreateModel(object):

    def __init__(self):
        self._create_customer_request = None

    @property
    def create_customer_request(self):
        return self._create_customer_request

    @create_customer_request.setter
    def create_customer_request(self, value):
        if isinstance(value, CreateCustomerRequest):
            self._create_customer_request = value
        else:
            self._create_customer_request = CreateCustomerRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.create_customer_request:
            if hasattr(self.create_customer_request, 'to_alipay_dict'):
                params['create_customer_request'] = self.create_customer_request.to_alipay_dict()
            else:
                params['create_customer_request'] = self.create_customer_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalCustomerCreateModel()
        if 'create_customer_request' in d:
            o.create_customer_request = d['create_customer_request']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceRegisterCreateDTO import InvoiceRegisterCreateDTO


class AlipayEbppInvoiceTopregisterRegisterCreateModel(object):

    def __init__(self):
        self._create_request = None

    @property
    def create_request(self):
        return self._create_request

    @create_request.setter
    def create_request(self, value):
        if isinstance(value, InvoiceRegisterCreateDTO):
            self._create_request = value
        else:
            self._create_request = InvoiceRegisterCreateDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.create_request:
            if hasattr(self.create_request, 'to_alipay_dict'):
                params['create_request'] = self.create_request.to_alipay_dict()
            else:
                params['create_request'] = self.create_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceTopregisterRegisterCreateModel()
        if 'create_request' in d:
            o.create_request = d['create_request']
        return o



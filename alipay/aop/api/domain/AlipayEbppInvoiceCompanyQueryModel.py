#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceCompanyQueryModel(object):

    def __init__(self):
        self._payee_register_no = None
        self._register_id = None

    @property
    def payee_register_no(self):
        return self._payee_register_no

    @payee_register_no.setter
    def payee_register_no(self, value):
        self._payee_register_no = value
    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.payee_register_no:
            if hasattr(self.payee_register_no, 'to_alipay_dict'):
                params['payee_register_no'] = self.payee_register_no.to_alipay_dict()
            else:
                params['payee_register_no'] = self.payee_register_no
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
        o = AlipayEbppInvoiceCompanyQueryModel()
        if 'payee_register_no' in d:
            o.payee_register_no = d['payee_register_no']
        if 'register_id' in d:
            o.register_id = d['register_id']
        return o



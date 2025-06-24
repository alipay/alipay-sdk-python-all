#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneServiceAvailableQueryModel(object):

    def __init__(self):
        self._ser_contract_no = None

    @property
    def ser_contract_no(self):
        return self._ser_contract_no

    @ser_contract_no.setter
    def ser_contract_no(self, value):
        self._ser_contract_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ser_contract_no:
            if hasattr(self.ser_contract_no, 'to_alipay_dict'):
                params['ser_contract_no'] = self.ser_contract_no.to_alipay_dict()
            else:
                params['ser_contract_no'] = self.ser_contract_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneServiceAvailableQueryModel()
        if 'ser_contract_no' in d:
            o.ser_contract_no = d['ser_contract_no']
        return o



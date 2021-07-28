#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractManagerProcessSyncRequest import ContractManagerProcessSyncRequest


class AlipayEcoContractProcessSyncModel(object):

    def __init__(self):
        self._batch_no = None
        self._flows = None
        self._sign_platform_code = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def flows(self):
        return self._flows

    @flows.setter
    def flows(self, value):
        if isinstance(value, list):
            self._flows = list()
            for i in value:
                if isinstance(i, ContractManagerProcessSyncRequest):
                    self._flows.append(i)
                else:
                    self._flows.append(ContractManagerProcessSyncRequest.from_alipay_dict(i))
    @property
    def sign_platform_code(self):
        return self._sign_platform_code

    @sign_platform_code.setter
    def sign_platform_code(self, value):
        self._sign_platform_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.flows:
            if isinstance(self.flows, list):
                for i in range(0, len(self.flows)):
                    element = self.flows[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.flows[i] = element.to_alipay_dict()
            if hasattr(self.flows, 'to_alipay_dict'):
                params['flows'] = self.flows.to_alipay_dict()
            else:
                params['flows'] = self.flows
        if self.sign_platform_code:
            if hasattr(self.sign_platform_code, 'to_alipay_dict'):
                params['sign_platform_code'] = self.sign_platform_code.to_alipay_dict()
            else:
                params['sign_platform_code'] = self.sign_platform_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoContractProcessSyncModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'flows' in d:
            o.flows = d['flows']
        if 'sign_platform_code' in d:
            o.sign_platform_code = d['sign_platform_code']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApplyCodeRequest import ApplyCodeRequest


class AntMerchantExpandScodeApplyModel(object):

    def __init__(self):
        self._apply_code_request = None

    @property
    def apply_code_request(self):
        return self._apply_code_request

    @apply_code_request.setter
    def apply_code_request(self, value):
        if isinstance(value, list):
            self._apply_code_request = list()
            for i in value:
                if isinstance(i, ApplyCodeRequest):
                    self._apply_code_request.append(i)
                else:
                    self._apply_code_request.append(ApplyCodeRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.apply_code_request:
            if isinstance(self.apply_code_request, list):
                for i in range(0, len(self.apply_code_request)):
                    element = self.apply_code_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_code_request[i] = element.to_alipay_dict()
            if hasattr(self.apply_code_request, 'to_alipay_dict'):
                params['apply_code_request'] = self.apply_code_request.to_alipay_dict()
            else:
                params['apply_code_request'] = self.apply_code_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandScodeApplyModel()
        if 'apply_code_request' in d:
            o.apply_code_request = d['apply_code_request']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UpdateCodeRequest import UpdateCodeRequest


class AntMerchantExpandScodeModifyModel(object):

    def __init__(self):
        self._update_code_request = None

    @property
    def update_code_request(self):
        return self._update_code_request

    @update_code_request.setter
    def update_code_request(self, value):
        if isinstance(value, list):
            self._update_code_request = list()
            for i in value:
                if isinstance(i, UpdateCodeRequest):
                    self._update_code_request.append(i)
                else:
                    self._update_code_request.append(UpdateCodeRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.update_code_request:
            if isinstance(self.update_code_request, list):
                for i in range(0, len(self.update_code_request)):
                    element = self.update_code_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.update_code_request[i] = element.to_alipay_dict()
            if hasattr(self.update_code_request, 'to_alipay_dict'):
                params['update_code_request'] = self.update_code_request.to_alipay_dict()
            else:
                params['update_code_request'] = self.update_code_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandScodeModifyModel()
        if 'update_code_request' in d:
            o.update_code_request = d['update_code_request']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EncryptRequest import EncryptRequest


class AlipayCommerceMedicalInsuranceClaimQueryModel(object):

    def __init__(self):
        self._encrypt_request = None

    @property
    def encrypt_request(self):
        return self._encrypt_request

    @encrypt_request.setter
    def encrypt_request(self, value):
        if isinstance(value, EncryptRequest):
            self._encrypt_request = value
        else:
            self._encrypt_request = EncryptRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.encrypt_request:
            if hasattr(self.encrypt_request, 'to_alipay_dict'):
                params['encrypt_request'] = self.encrypt_request.to_alipay_dict()
            else:
                params['encrypt_request'] = self.encrypt_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceClaimQueryModel()
        if 'encrypt_request' in d:
            o.encrypt_request = d['encrypt_request']
        return o



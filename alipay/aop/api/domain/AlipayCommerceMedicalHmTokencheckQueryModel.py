#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHmTokencheckQueryModel(object):

    def __init__(self):
        self._hm_token = None

    @property
    def hm_token(self):
        return self._hm_token

    @hm_token.setter
    def hm_token(self, value):
        self._hm_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.hm_token:
            if hasattr(self.hm_token, 'to_alipay_dict'):
                params['hm_token'] = self.hm_token.to_alipay_dict()
            else:
                params['hm_token'] = self.hm_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHmTokencheckQueryModel()
        if 'hm_token' in d:
            o.hm_token = d['hm_token']
        return o



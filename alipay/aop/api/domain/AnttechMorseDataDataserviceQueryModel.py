#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseDataDataserviceQueryModel(object):

    def __init__(self):
        self._consult_id = None
        self._mobile_sha_256 = None

    @property
    def consult_id(self):
        return self._consult_id

    @consult_id.setter
    def consult_id(self, value):
        self._consult_id = value
    @property
    def mobile_sha_256(self):
        return self._mobile_sha_256

    @mobile_sha_256.setter
    def mobile_sha_256(self, value):
        self._mobile_sha_256 = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_id:
            if hasattr(self.consult_id, 'to_alipay_dict'):
                params['consult_id'] = self.consult_id.to_alipay_dict()
            else:
                params['consult_id'] = self.consult_id
        if self.mobile_sha_256:
            if hasattr(self.mobile_sha_256, 'to_alipay_dict'):
                params['mobile_sha_256'] = self.mobile_sha_256.to_alipay_dict()
            else:
                params['mobile_sha_256'] = self.mobile_sha_256
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseDataDataserviceQueryModel()
        if 'consult_id' in d:
            o.consult_id = d['consult_id']
        if 'mobile_sha_256' in d:
            o.mobile_sha_256 = d['mobile_sha_256']
        return o



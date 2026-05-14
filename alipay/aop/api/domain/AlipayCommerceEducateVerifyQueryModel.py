#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateVerifyQueryModel(object):

    def __init__(self):
        self._verify_request_id = None

    @property
    def verify_request_id(self):
        return self._verify_request_id

    @verify_request_id.setter
    def verify_request_id(self, value):
        self._verify_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.verify_request_id:
            if hasattr(self.verify_request_id, 'to_alipay_dict'):
                params['verify_request_id'] = self.verify_request_id.to_alipay_dict()
            else:
                params['verify_request_id'] = self.verify_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateVerifyQueryModel()
        if 'verify_request_id' in d:
            o.verify_request_id = d['verify_request_id']
        return o



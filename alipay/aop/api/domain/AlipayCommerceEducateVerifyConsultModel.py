#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VerifyOrderInfo import VerifyOrderInfo


class AlipayCommerceEducateVerifyConsultModel(object):

    def __init__(self):
        self._verify_info = None
        self._verify_request_id = None

    @property
    def verify_info(self):
        return self._verify_info

    @verify_info.setter
    def verify_info(self, value):
        if isinstance(value, VerifyOrderInfo):
            self._verify_info = value
        else:
            self._verify_info = VerifyOrderInfo.from_alipay_dict(value)
    @property
    def verify_request_id(self):
        return self._verify_request_id

    @verify_request_id.setter
    def verify_request_id(self, value):
        self._verify_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.verify_info:
            if hasattr(self.verify_info, 'to_alipay_dict'):
                params['verify_info'] = self.verify_info.to_alipay_dict()
            else:
                params['verify_info'] = self.verify_info
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
        o = AlipayCommerceEducateVerifyConsultModel()
        if 'verify_info' in d:
            o.verify_info = d['verify_info']
        if 'verify_request_id' in d:
            o.verify_request_id = d['verify_request_id']
        return o



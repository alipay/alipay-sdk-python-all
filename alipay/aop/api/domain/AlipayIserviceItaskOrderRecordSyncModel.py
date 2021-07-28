#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HomeApiRequest import HomeApiRequest


class AlipayIserviceItaskOrderRecordSyncModel(object):

    def __init__(self):
        self._home_api_request = None

    @property
    def home_api_request(self):
        return self._home_api_request

    @home_api_request.setter
    def home_api_request(self, value):
        if isinstance(value, HomeApiRequest):
            self._home_api_request = value
        else:
            self._home_api_request = HomeApiRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.home_api_request:
            if hasattr(self.home_api_request, 'to_alipay_dict'):
                params['home_api_request'] = self.home_api_request.to_alipay_dict()
            else:
                params['home_api_request'] = self.home_api_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceItaskOrderRecordSyncModel()
        if 'home_api_request' in d:
            o.home_api_request = d['home_api_request']
        return o



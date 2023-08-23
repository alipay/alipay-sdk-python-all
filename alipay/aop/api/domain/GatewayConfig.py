#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GatewayConfig(object):

    def __init__(self):
        self._endpoint = None
        self._name = None

    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value):
        self._endpoint = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.endpoint:
            if hasattr(self.endpoint, 'to_alipay_dict'):
                params['endpoint'] = self.endpoint.to_alipay_dict()
            else:
                params['endpoint'] = self.endpoint
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GatewayConfig()
        if 'endpoint' in d:
            o.endpoint = d['endpoint']
        if 'name' in d:
            o.name = d['name']
        return o



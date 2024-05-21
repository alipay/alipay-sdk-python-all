#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryOrientedRuleInfo(object):

    def __init__(self):
        self._client_platform = None

    @property
    def client_platform(self):
        return self._client_platform

    @client_platform.setter
    def client_platform(self, value):
        self._client_platform = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_platform:
            if hasattr(self.client_platform, 'to_alipay_dict'):
                params['client_platform'] = self.client_platform.to_alipay_dict()
            else:
                params['client_platform'] = self.client_platform
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryOrientedRuleInfo()
        if 'client_platform' in d:
            o.client_platform = d['client_platform']
        return o



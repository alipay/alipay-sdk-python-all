#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSportsInsurancetrainCreateModel(object):

    def __init__(self):
        self._resource_id = None
        self._security_data = None

    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def security_data(self):
        return self._security_data

    @security_data.setter
    def security_data(self, value):
        self._security_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.security_data:
            if hasattr(self.security_data, 'to_alipay_dict'):
                params['security_data'] = self.security_data.to_alipay_dict()
            else:
                params['security_data'] = self.security_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSportsInsurancetrainCreateModel()
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'security_data' in d:
            o.security_data = d['security_data']
        return o



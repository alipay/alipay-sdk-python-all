#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskRiskprofileQueryModel(object):

    def __init__(self):
        self._request_from = None
        self._request_id = None
        self._risk_object = None
        self._risk_object_value = None
        self._risk_profile = None

    @property
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def risk_object(self):
        return self._risk_object

    @risk_object.setter
    def risk_object(self, value):
        if isinstance(value, list):
            self._risk_object = list()
            for i in value:
                self._risk_object.append(i)
    @property
    def risk_object_value(self):
        return self._risk_object_value

    @risk_object_value.setter
    def risk_object_value(self, value):
        if isinstance(value, list):
            self._risk_object_value = list()
            for i in value:
                self._risk_object_value.append(i)
    @property
    def risk_profile(self):
        return self._risk_profile

    @risk_profile.setter
    def risk_profile(self, value):
        if isinstance(value, list):
            self._risk_profile = list()
            for i in value:
                self._risk_profile.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.request_from:
            if hasattr(self.request_from, 'to_alipay_dict'):
                params['request_from'] = self.request_from.to_alipay_dict()
            else:
                params['request_from'] = self.request_from
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.risk_object:
            if isinstance(self.risk_object, list):
                for i in range(0, len(self.risk_object)):
                    element = self.risk_object[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_object[i] = element.to_alipay_dict()
            if hasattr(self.risk_object, 'to_alipay_dict'):
                params['risk_object'] = self.risk_object.to_alipay_dict()
            else:
                params['risk_object'] = self.risk_object
        if self.risk_object_value:
            if isinstance(self.risk_object_value, list):
                for i in range(0, len(self.risk_object_value)):
                    element = self.risk_object_value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_object_value[i] = element.to_alipay_dict()
            if hasattr(self.risk_object_value, 'to_alipay_dict'):
                params['risk_object_value'] = self.risk_object_value.to_alipay_dict()
            else:
                params['risk_object_value'] = self.risk_object_value
        if self.risk_profile:
            if isinstance(self.risk_profile, list):
                for i in range(0, len(self.risk_profile)):
                    element = self.risk_profile[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_profile[i] = element.to_alipay_dict()
            if hasattr(self.risk_profile, 'to_alipay_dict'):
                params['risk_profile'] = self.risk_profile.to_alipay_dict()
            else:
                params['risk_profile'] = self.risk_profile
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskRiskprofileQueryModel()
        if 'request_from' in d:
            o.request_from = d['request_from']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'risk_object' in d:
            o.risk_object = d['risk_object']
        if 'risk_object_value' in d:
            o.risk_object_value = d['risk_object_value']
        if 'risk_profile' in d:
            o.risk_profile = d['risk_profile']
        return o



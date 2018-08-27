#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SecurityScene import SecurityScene
from alipay.aop.api.domain.ServiceContext import ServiceContext


class AlipaySecurityRiskPolicyQueryModel(object):

    def __init__(self):
        self._risk_type = None
        self._security_scene = None
        self._service_context = None

    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value
    @property
    def security_scene(self):
        return self._security_scene

    @security_scene.setter
    def security_scene(self, value):
        if isinstance(value, SecurityScene):
            self._security_scene = value
        else:
            self._security_scene = SecurityScene.from_alipay_dict(value)
    @property
    def service_context(self):
        return self._service_context

    @service_context.setter
    def service_context(self, value):
        if isinstance(value, ServiceContext):
            self._service_context = value
        else:
            self._service_context = ServiceContext.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        if self.security_scene:
            if hasattr(self.security_scene, 'to_alipay_dict'):
                params['security_scene'] = self.security_scene.to_alipay_dict()
            else:
                params['security_scene'] = self.security_scene
        if self.service_context:
            if hasattr(self.service_context, 'to_alipay_dict'):
                params['service_context'] = self.service_context.to_alipay_dict()
            else:
                params['service_context'] = self.service_context
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskPolicyQueryModel()
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'security_scene' in d:
            o.security_scene = d['security_scene']
        if 'service_context' in d:
            o.service_context = d['service_context']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlescenterDocusignresultQueryModel(object):

    def __init__(self):
        self._application_system = None
        self._business_line_code = None
        self._flow_id = None
        self._scene_code = None
        self._sign_task_id = None
        self._tenant = None

    @property
    def application_system(self):
        return self._application_system

    @application_system.setter
    def application_system(self, value):
        self._application_system = value
    @property
    def business_line_code(self):
        return self._business_line_code

    @business_line_code.setter
    def business_line_code(self, value):
        self._business_line_code = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sign_task_id(self):
        return self._sign_task_id

    @sign_task_id.setter
    def sign_task_id(self, value):
        self._sign_task_id = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_system:
            if hasattr(self.application_system, 'to_alipay_dict'):
                params['application_system'] = self.application_system.to_alipay_dict()
            else:
                params['application_system'] = self.application_system
        if self.business_line_code:
            if hasattr(self.business_line_code, 'to_alipay_dict'):
                params['business_line_code'] = self.business_line_code.to_alipay_dict()
            else:
                params['business_line_code'] = self.business_line_code
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.sign_task_id:
            if hasattr(self.sign_task_id, 'to_alipay_dict'):
                params['sign_task_id'] = self.sign_task_id.to_alipay_dict()
            else:
                params['sign_task_id'] = self.sign_task_id
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlescenterDocusignresultQueryModel()
        if 'application_system' in d:
            o.application_system = d['application_system']
        if 'business_line_code' in d:
            o.business_line_code = d['business_line_code']
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sign_task_id' in d:
            o.sign_task_id = d['sign_task_id']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntsignDetailQueryModel(object):

    def __init__(self):
        self._app_name = None
        self._biz_no = None
        self._business_line_code = None
        self._scene_code = None
        self._sign_flow_id = None
        self._sign_task_id = None
        self._tenant = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def business_line_code(self):
        return self._business_line_code

    @business_line_code.setter
    def business_line_code(self, value):
        self._business_line_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value
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
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.business_line_code:
            if hasattr(self.business_line_code, 'to_alipay_dict'):
                params['business_line_code'] = self.business_line_code.to_alipay_dict()
            else:
                params['business_line_code'] = self.business_line_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.sign_flow_id:
            if hasattr(self.sign_flow_id, 'to_alipay_dict'):
                params['sign_flow_id'] = self.sign_flow_id.to_alipay_dict()
            else:
                params['sign_flow_id'] = self.sign_flow_id
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
        o = AlipayBossProdAntsignDetailQueryModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'business_line_code' in d:
            o.business_line_code = d['business_line_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sign_flow_id' in d:
            o.sign_flow_id = d['sign_flow_id']
        if 'sign_task_id' in d:
            o.sign_task_id = d['sign_task_id']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o



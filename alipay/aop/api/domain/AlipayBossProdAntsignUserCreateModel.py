#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntsignUserCreateModel(object):

    def __init__(self):
        self._app_name = None
        self._business_line_code = None
        self._cert_number = None
        self._scene_code = None
        self._tenant = None
        self._user_cert_type = None
        self._user_name = None
        self._user_type = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def business_line_code(self):
        return self._business_line_code

    @business_line_code.setter
    def business_line_code(self, value):
        self._business_line_code = value
    @property
    def cert_number(self):
        return self._cert_number

    @cert_number.setter
    def cert_number(self, value):
        self._cert_number = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def user_cert_type(self):
        return self._user_cert_type

    @user_cert_type.setter
    def user_cert_type(self, value):
        self._user_cert_type = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.business_line_code:
            if hasattr(self.business_line_code, 'to_alipay_dict'):
                params['business_line_code'] = self.business_line_code.to_alipay_dict()
            else:
                params['business_line_code'] = self.business_line_code
        if self.cert_number:
            if hasattr(self.cert_number, 'to_alipay_dict'):
                params['cert_number'] = self.cert_number.to_alipay_dict()
            else:
                params['cert_number'] = self.cert_number
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.user_cert_type:
            if hasattr(self.user_cert_type, 'to_alipay_dict'):
                params['user_cert_type'] = self.user_cert_type.to_alipay_dict()
            else:
                params['user_cert_type'] = self.user_cert_type
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntsignUserCreateModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'business_line_code' in d:
            o.business_line_code = d['business_line_code']
        if 'cert_number' in d:
            o.cert_number = d['cert_number']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'user_cert_type' in d:
            o.user_cert_type = d['user_cert_type']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o



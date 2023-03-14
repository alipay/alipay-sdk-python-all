#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntSignTaskRequest import AntSignTaskRequest


class AlipayBossProdAntCasignCreateModel(object):

    def __init__(self):
        self._ant_sign_task_request_list = None
        self._app_name = None
        self._biz_name = None
        self._biz_no = None
        self._biz_type = None
        self._business_line_code = None
        self._callback_url = None
        self._expire_date = None
        self._scene_code = None
        self._sign_task_type = None
        self._sign_version = None
        self._tenant = None

    @property
    def ant_sign_task_request_list(self):
        return self._ant_sign_task_request_list

    @ant_sign_task_request_list.setter
    def ant_sign_task_request_list(self, value):
        if isinstance(value, list):
            self._ant_sign_task_request_list = list()
            for i in value:
                if isinstance(i, AntSignTaskRequest):
                    self._ant_sign_task_request_list.append(i)
                else:
                    self._ant_sign_task_request_list.append(AntSignTaskRequest.from_alipay_dict(i))
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def biz_name(self):
        return self._biz_name

    @biz_name.setter
    def biz_name(self, value):
        self._biz_name = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def business_line_code(self):
        return self._business_line_code

    @business_line_code.setter
    def business_line_code(self, value):
        self._business_line_code = value
    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sign_task_type(self):
        return self._sign_task_type

    @sign_task_type.setter
    def sign_task_type(self, value):
        self._sign_task_type = value
    @property
    def sign_version(self):
        return self._sign_version

    @sign_version.setter
    def sign_version(self, value):
        self._sign_version = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_sign_task_request_list:
            if isinstance(self.ant_sign_task_request_list, list):
                for i in range(0, len(self.ant_sign_task_request_list)):
                    element = self.ant_sign_task_request_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ant_sign_task_request_list[i] = element.to_alipay_dict()
            if hasattr(self.ant_sign_task_request_list, 'to_alipay_dict'):
                params['ant_sign_task_request_list'] = self.ant_sign_task_request_list.to_alipay_dict()
            else:
                params['ant_sign_task_request_list'] = self.ant_sign_task_request_list
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.biz_name:
            if hasattr(self.biz_name, 'to_alipay_dict'):
                params['biz_name'] = self.biz_name.to_alipay_dict()
            else:
                params['biz_name'] = self.biz_name
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.business_line_code:
            if hasattr(self.business_line_code, 'to_alipay_dict'):
                params['business_line_code'] = self.business_line_code.to_alipay_dict()
            else:
                params['business_line_code'] = self.business_line_code
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.sign_task_type:
            if hasattr(self.sign_task_type, 'to_alipay_dict'):
                params['sign_task_type'] = self.sign_task_type.to_alipay_dict()
            else:
                params['sign_task_type'] = self.sign_task_type
        if self.sign_version:
            if hasattr(self.sign_version, 'to_alipay_dict'):
                params['sign_version'] = self.sign_version.to_alipay_dict()
            else:
                params['sign_version'] = self.sign_version
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
        o = AlipayBossProdAntCasignCreateModel()
        if 'ant_sign_task_request_list' in d:
            o.ant_sign_task_request_list = d['ant_sign_task_request_list']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'biz_name' in d:
            o.biz_name = d['biz_name']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'business_line_code' in d:
            o.business_line_code = d['business_line_code']
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sign_task_type' in d:
            o.sign_task_type = d['sign_task_type']
        if 'sign_version' in d:
            o.sign_version = d['sign_version']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o



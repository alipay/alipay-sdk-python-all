#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Principal import Principal


class SignTask(object):

    def __init__(self):
        self._biz_data = None
        self._biz_id = None
        self._cb_type = None
        self._cb_url = None
        self._cert_sign_type = None
        self._enter_type = None
        self._principal_list = None
        self._signer_type = None
        self._task_expire = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def cb_type(self):
        return self._cb_type

    @cb_type.setter
    def cb_type(self, value):
        self._cb_type = value
    @property
    def cb_url(self):
        return self._cb_url

    @cb_url.setter
    def cb_url(self, value):
        self._cb_url = value
    @property
    def cert_sign_type(self):
        return self._cert_sign_type

    @cert_sign_type.setter
    def cert_sign_type(self, value):
        self._cert_sign_type = value
    @property
    def enter_type(self):
        return self._enter_type

    @enter_type.setter
    def enter_type(self, value):
        self._enter_type = value
    @property
    def principal_list(self):
        return self._principal_list

    @principal_list.setter
    def principal_list(self, value):
        if isinstance(value, list):
            self._principal_list = list()
            for i in value:
                if isinstance(i, Principal):
                    self._principal_list.append(i)
                else:
                    self._principal_list.append(Principal.from_alipay_dict(i))
    @property
    def signer_type(self):
        return self._signer_type

    @signer_type.setter
    def signer_type(self, value):
        self._signer_type = value
    @property
    def task_expire(self):
        return self._task_expire

    @task_expire.setter
    def task_expire(self, value):
        self._task_expire = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.cb_type:
            if hasattr(self.cb_type, 'to_alipay_dict'):
                params['cb_type'] = self.cb_type.to_alipay_dict()
            else:
                params['cb_type'] = self.cb_type
        if self.cb_url:
            if hasattr(self.cb_url, 'to_alipay_dict'):
                params['cb_url'] = self.cb_url.to_alipay_dict()
            else:
                params['cb_url'] = self.cb_url
        if self.cert_sign_type:
            if hasattr(self.cert_sign_type, 'to_alipay_dict'):
                params['cert_sign_type'] = self.cert_sign_type.to_alipay_dict()
            else:
                params['cert_sign_type'] = self.cert_sign_type
        if self.enter_type:
            if hasattr(self.enter_type, 'to_alipay_dict'):
                params['enter_type'] = self.enter_type.to_alipay_dict()
            else:
                params['enter_type'] = self.enter_type
        if self.principal_list:
            if isinstance(self.principal_list, list):
                for i in range(0, len(self.principal_list)):
                    element = self.principal_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.principal_list[i] = element.to_alipay_dict()
            if hasattr(self.principal_list, 'to_alipay_dict'):
                params['principal_list'] = self.principal_list.to_alipay_dict()
            else:
                params['principal_list'] = self.principal_list
        if self.signer_type:
            if hasattr(self.signer_type, 'to_alipay_dict'):
                params['signer_type'] = self.signer_type.to_alipay_dict()
            else:
                params['signer_type'] = self.signer_type
        if self.task_expire:
            if hasattr(self.task_expire, 'to_alipay_dict'):
                params['task_expire'] = self.task_expire.to_alipay_dict()
            else:
                params['task_expire'] = self.task_expire
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignTask()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'cb_type' in d:
            o.cb_type = d['cb_type']
        if 'cb_url' in d:
            o.cb_url = d['cb_url']
        if 'cert_sign_type' in d:
            o.cert_sign_type = d['cert_sign_type']
        if 'enter_type' in d:
            o.enter_type = d['enter_type']
        if 'principal_list' in d:
            o.principal_list = d['principal_list']
        if 'signer_type' in d:
            o.signer_type = d['signer_type']
        if 'task_expire' in d:
            o.task_expire = d['task_expire']
        return o



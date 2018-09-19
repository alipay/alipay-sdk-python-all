#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMedicalcareCommonDataSyncModel(object):

    def __init__(self):
        self._app_code = None
        self._data_body = None
        self._data_type = None
        self._template_id = None
        self._user_id = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def data_body(self):
        return self._data_body

    @data_body.setter
    def data_body(self, value):
        self._data_body = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.data_body:
            if hasattr(self.data_body, 'to_alipay_dict'):
                params['data_body'] = self.data_body.to_alipay_dict()
            else:
                params['data_body'] = self.data_body
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMedicalcareCommonDataSyncModel()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'data_body' in d:
            o.data_body = d['data_body']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



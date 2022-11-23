#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserGamecenterLogSubmitModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._error_code = None
        self._error_desc = None
        self._open_id = None
        self._openapi_name = None
        self._request_body = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def openapi_name(self):
        return self._openapi_name

    @openapi_name.setter
    def openapi_name(self, value):
        self._openapi_name = value
    @property
    def request_body(self):
        return self._request_body

    @request_body.setter
    def request_body(self, value):
        self._request_body = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_desc:
            if hasattr(self.error_desc, 'to_alipay_dict'):
                params['error_desc'] = self.error_desc.to_alipay_dict()
            else:
                params['error_desc'] = self.error_desc
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.openapi_name:
            if hasattr(self.openapi_name, 'to_alipay_dict'):
                params['openapi_name'] = self.openapi_name.to_alipay_dict()
            else:
                params['openapi_name'] = self.openapi_name
        if self.request_body:
            if hasattr(self.request_body, 'to_alipay_dict'):
                params['request_body'] = self.request_body.to_alipay_dict()
            else:
                params['request_body'] = self.request_body
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserGamecenterLogSubmitModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_desc' in d:
            o.error_desc = d['error_desc']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'openapi_name' in d:
            o.openapi_name = d['openapi_name']
        if 'request_body' in d:
            o.request_body = d['request_body']
        return o



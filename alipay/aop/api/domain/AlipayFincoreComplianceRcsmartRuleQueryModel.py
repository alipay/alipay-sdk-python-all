#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceRcsmartRuleQueryModel(object):

    def __init__(self):
        self._app_name = None
        self._app_token = None
        self._file_id = None
        self._request_id = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_token:
            if hasattr(self.app_token, 'to_alipay_dict'):
                params['app_token'] = self.app_token.to_alipay_dict()
            else:
                params['app_token'] = self.app_token
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceRcsmartRuleQueryModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_token' in d:
            o.app_token = d['app_token']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o



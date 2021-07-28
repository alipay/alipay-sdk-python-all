#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlegalchainNotaryprocsumQueryModel(object):

    def __init__(self):
        self._bas_data_id = None
        self._request_app_name = None
        self._request_time_stamp = None
        self._request_token = None

    @property
    def bas_data_id(self):
        return self._bas_data_id

    @bas_data_id.setter
    def bas_data_id(self, value):
        self._bas_data_id = value
    @property
    def request_app_name(self):
        return self._request_app_name

    @request_app_name.setter
    def request_app_name(self, value):
        self._request_app_name = value
    @property
    def request_time_stamp(self):
        return self._request_time_stamp

    @request_time_stamp.setter
    def request_time_stamp(self, value):
        self._request_time_stamp = value
    @property
    def request_token(self):
        return self._request_token

    @request_token.setter
    def request_token(self, value):
        self._request_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.bas_data_id:
            if hasattr(self.bas_data_id, 'to_alipay_dict'):
                params['bas_data_id'] = self.bas_data_id.to_alipay_dict()
            else:
                params['bas_data_id'] = self.bas_data_id
        if self.request_app_name:
            if hasattr(self.request_app_name, 'to_alipay_dict'):
                params['request_app_name'] = self.request_app_name.to_alipay_dict()
            else:
                params['request_app_name'] = self.request_app_name
        if self.request_time_stamp:
            if hasattr(self.request_time_stamp, 'to_alipay_dict'):
                params['request_time_stamp'] = self.request_time_stamp.to_alipay_dict()
            else:
                params['request_time_stamp'] = self.request_time_stamp
        if self.request_token:
            if hasattr(self.request_token, 'to_alipay_dict'):
                params['request_token'] = self.request_token.to_alipay_dict()
            else:
                params['request_token'] = self.request_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlegalchainNotaryprocsumQueryModel()
        if 'bas_data_id' in d:
            o.bas_data_id = d['bas_data_id']
        if 'request_app_name' in d:
            o.request_app_name = d['request_app_name']
        if 'request_time_stamp' in d:
            o.request_time_stamp = d['request_time_stamp']
        if 'request_token' in d:
            o.request_token = d['request_token']
        return o



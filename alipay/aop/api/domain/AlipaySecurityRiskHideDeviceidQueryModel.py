#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskHideDeviceidQueryModel(object):

    def __init__(self):
        self._app_key_client = None
        self._app_key_server = None
        self._app_name = None
        self._deviceid_token = None

    @property
    def app_key_client(self):
        return self._app_key_client

    @app_key_client.setter
    def app_key_client(self, value):
        self._app_key_client = value
    @property
    def app_key_server(self):
        return self._app_key_server

    @app_key_server.setter
    def app_key_server(self, value):
        self._app_key_server = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def deviceid_token(self):
        return self._deviceid_token

    @deviceid_token.setter
    def deviceid_token(self, value):
        self._deviceid_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_key_client:
            if hasattr(self.app_key_client, 'to_alipay_dict'):
                params['app_key_client'] = self.app_key_client.to_alipay_dict()
            else:
                params['app_key_client'] = self.app_key_client
        if self.app_key_server:
            if hasattr(self.app_key_server, 'to_alipay_dict'):
                params['app_key_server'] = self.app_key_server.to_alipay_dict()
            else:
                params['app_key_server'] = self.app_key_server
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.deviceid_token:
            if hasattr(self.deviceid_token, 'to_alipay_dict'):
                params['deviceid_token'] = self.deviceid_token.to_alipay_dict()
            else:
                params['deviceid_token'] = self.deviceid_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskHideDeviceidQueryModel()
        if 'app_key_client' in d:
            o.app_key_client = d['app_key_client']
        if 'app_key_server' in d:
            o.app_key_server = d['app_key_server']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'deviceid_token' in d:
            o.deviceid_token = d['deviceid_token']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SharePeerPaySecurityInfo(object):

    def __init__(self):
        self._app_name = None
        self._client_ip = None
        self._external_device_id = None
        self._terminal_type = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def external_device_id(self):
        return self._external_device_id

    @external_device_id.setter
    def external_device_id(self, value):
        self._external_device_id = value
    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.external_device_id:
            if hasattr(self.external_device_id, 'to_alipay_dict'):
                params['external_device_id'] = self.external_device_id.to_alipay_dict()
            else:
                params['external_device_id'] = self.external_device_id
        if self.terminal_type:
            if hasattr(self.terminal_type, 'to_alipay_dict'):
                params['terminal_type'] = self.terminal_type.to_alipay_dict()
            else:
                params['terminal_type'] = self.terminal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SharePeerPaySecurityInfo()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'external_device_id' in d:
            o.external_device_id = d['external_device_id']
        if 'terminal_type' in d:
            o.terminal_type = d['terminal_type']
        return o



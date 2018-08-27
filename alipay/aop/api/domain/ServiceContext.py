#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceContext(object):

    def __init__(self):
        self._client_ip = None
        self._client_pcidguid = None
        self._server_name = None
        self._session_id = None
        self._user_id = None

    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def client_pcidguid(self):
        return self._client_pcidguid

    @client_pcidguid.setter
    def client_pcidguid(self, value):
        self._client_pcidguid = value
    @property
    def server_name(self):
        return self._server_name

    @server_name.setter
    def server_name(self, value):
        self._server_name = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.client_pcidguid:
            if hasattr(self.client_pcidguid, 'to_alipay_dict'):
                params['client_pcidguid'] = self.client_pcidguid.to_alipay_dict()
            else:
                params['client_pcidguid'] = self.client_pcidguid
        if self.server_name:
            if hasattr(self.server_name, 'to_alipay_dict'):
                params['server_name'] = self.server_name.to_alipay_dict()
            else:
                params['server_name'] = self.server_name
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
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
        o = ServiceContext()
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'client_pcidguid' in d:
            o.client_pcidguid = d['client_pcidguid']
        if 'server_name' in d:
            o.server_name = d['server_name']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



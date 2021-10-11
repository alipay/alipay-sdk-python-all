#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCliveConnectCreateModel(object):

    def __init__(self):
        self._app_type = None
        self._client_info = None
        self._client_ip = None
        self._enter_url = None
        self._ext_values = None
        self._group_id = None
        self._path_id = None
        self._priority = None
        self._reconnect = None
        self._server_id = None
        self._service_token = None
        self._session_uuid = None
        self._src = None
        self._visitor_id = None
        self._visitor_name = None
        self._visitor_type = None

    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def client_info(self):
        return self._client_info

    @client_info.setter
    def client_info(self, value):
        self._client_info = value
    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def enter_url(self):
        return self._enter_url

    @enter_url.setter
    def enter_url(self, value):
        self._enter_url = value
    @property
    def ext_values(self):
        return self._ext_values

    @ext_values.setter
    def ext_values(self, value):
        self._ext_values = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def path_id(self):
        return self._path_id

    @path_id.setter
    def path_id(self, value):
        self._path_id = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def reconnect(self):
        return self._reconnect

    @reconnect.setter
    def reconnect(self, value):
        self._reconnect = value
    @property
    def server_id(self):
        return self._server_id

    @server_id.setter
    def server_id(self, value):
        self._server_id = value
    @property
    def service_token(self):
        return self._service_token

    @service_token.setter
    def service_token(self, value):
        self._service_token = value
    @property
    def session_uuid(self):
        return self._session_uuid

    @session_uuid.setter
    def session_uuid(self, value):
        self._session_uuid = value
    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, value):
        self._src = value
    @property
    def visitor_id(self):
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, value):
        self._visitor_id = value
    @property
    def visitor_name(self):
        return self._visitor_name

    @visitor_name.setter
    def visitor_name(self, value):
        self._visitor_name = value
    @property
    def visitor_type(self):
        return self._visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        self._visitor_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.client_info:
            if hasattr(self.client_info, 'to_alipay_dict'):
                params['client_info'] = self.client_info.to_alipay_dict()
            else:
                params['client_info'] = self.client_info
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.enter_url:
            if hasattr(self.enter_url, 'to_alipay_dict'):
                params['enter_url'] = self.enter_url.to_alipay_dict()
            else:
                params['enter_url'] = self.enter_url
        if self.ext_values:
            if hasattr(self.ext_values, 'to_alipay_dict'):
                params['ext_values'] = self.ext_values.to_alipay_dict()
            else:
                params['ext_values'] = self.ext_values
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.path_id:
            if hasattr(self.path_id, 'to_alipay_dict'):
                params['path_id'] = self.path_id.to_alipay_dict()
            else:
                params['path_id'] = self.path_id
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.reconnect:
            if hasattr(self.reconnect, 'to_alipay_dict'):
                params['reconnect'] = self.reconnect.to_alipay_dict()
            else:
                params['reconnect'] = self.reconnect
        if self.server_id:
            if hasattr(self.server_id, 'to_alipay_dict'):
                params['server_id'] = self.server_id.to_alipay_dict()
            else:
                params['server_id'] = self.server_id
        if self.service_token:
            if hasattr(self.service_token, 'to_alipay_dict'):
                params['service_token'] = self.service_token.to_alipay_dict()
            else:
                params['service_token'] = self.service_token
        if self.session_uuid:
            if hasattr(self.session_uuid, 'to_alipay_dict'):
                params['session_uuid'] = self.session_uuid.to_alipay_dict()
            else:
                params['session_uuid'] = self.session_uuid
        if self.src:
            if hasattr(self.src, 'to_alipay_dict'):
                params['src'] = self.src.to_alipay_dict()
            else:
                params['src'] = self.src
        if self.visitor_id:
            if hasattr(self.visitor_id, 'to_alipay_dict'):
                params['visitor_id'] = self.visitor_id.to_alipay_dict()
            else:
                params['visitor_id'] = self.visitor_id
        if self.visitor_name:
            if hasattr(self.visitor_name, 'to_alipay_dict'):
                params['visitor_name'] = self.visitor_name.to_alipay_dict()
            else:
                params['visitor_name'] = self.visitor_name
        if self.visitor_type:
            if hasattr(self.visitor_type, 'to_alipay_dict'):
                params['visitor_type'] = self.visitor_type.to_alipay_dict()
            else:
                params['visitor_type'] = self.visitor_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCliveConnectCreateModel()
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'client_info' in d:
            o.client_info = d['client_info']
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'enter_url' in d:
            o.enter_url = d['enter_url']
        if 'ext_values' in d:
            o.ext_values = d['ext_values']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'path_id' in d:
            o.path_id = d['path_id']
        if 'priority' in d:
            o.priority = d['priority']
        if 'reconnect' in d:
            o.reconnect = d['reconnect']
        if 'server_id' in d:
            o.server_id = d['server_id']
        if 'service_token' in d:
            o.service_token = d['service_token']
        if 'session_uuid' in d:
            o.session_uuid = d['session_uuid']
        if 'src' in d:
            o.src = d['src']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        if 'visitor_name' in d:
            o.visitor_name = d['visitor_name']
        if 'visitor_type' in d:
            o.visitor_type = d['visitor_type']
        return o



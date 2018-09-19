#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasSyncSingledataSendModel(object):

    def __init__(self):
        self._app_max_version = None
        self._app_min_version = None
        self._binary_payload = None
        self._biz_tag = None
        self._biz_type = None
        self._client_app = None
        self._device_id = None
        self._immediate_sync = None
        self._link_token = None
        self._os_type = None
        self._payload = None
        self._third_msg_id = None
        self._valid_end = None
        self._valid_start = None

    @property
    def app_max_version(self):
        return self._app_max_version

    @app_max_version.setter
    def app_max_version(self, value):
        self._app_max_version = value
    @property
    def app_min_version(self):
        return self._app_min_version

    @app_min_version.setter
    def app_min_version(self, value):
        self._app_min_version = value
    @property
    def binary_payload(self):
        return self._binary_payload

    @binary_payload.setter
    def binary_payload(self, value):
        self._binary_payload = value
    @property
    def biz_tag(self):
        return self._biz_tag

    @biz_tag.setter
    def biz_tag(self, value):
        self._biz_tag = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def client_app(self):
        return self._client_app

    @client_app.setter
    def client_app(self, value):
        self._client_app = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def immediate_sync(self):
        return self._immediate_sync

    @immediate_sync.setter
    def immediate_sync(self, value):
        self._immediate_sync = value
    @property
    def link_token(self):
        return self._link_token

    @link_token.setter
    def link_token(self, value):
        self._link_token = value
    @property
    def os_type(self):
        return self._os_type

    @os_type.setter
    def os_type(self, value):
        self._os_type = value
    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = value
    @property
    def third_msg_id(self):
        return self._third_msg_id

    @third_msg_id.setter
    def third_msg_id(self, value):
        self._third_msg_id = value
    @property
    def valid_end(self):
        return self._valid_end

    @valid_end.setter
    def valid_end(self, value):
        self._valid_end = value
    @property
    def valid_start(self):
        return self._valid_start

    @valid_start.setter
    def valid_start(self, value):
        self._valid_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_max_version:
            if hasattr(self.app_max_version, 'to_alipay_dict'):
                params['app_max_version'] = self.app_max_version.to_alipay_dict()
            else:
                params['app_max_version'] = self.app_max_version
        if self.app_min_version:
            if hasattr(self.app_min_version, 'to_alipay_dict'):
                params['app_min_version'] = self.app_min_version.to_alipay_dict()
            else:
                params['app_min_version'] = self.app_min_version
        if self.binary_payload:
            if hasattr(self.binary_payload, 'to_alipay_dict'):
                params['binary_payload'] = self.binary_payload.to_alipay_dict()
            else:
                params['binary_payload'] = self.binary_payload
        if self.biz_tag:
            if hasattr(self.biz_tag, 'to_alipay_dict'):
                params['biz_tag'] = self.biz_tag.to_alipay_dict()
            else:
                params['biz_tag'] = self.biz_tag
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.client_app:
            if hasattr(self.client_app, 'to_alipay_dict'):
                params['client_app'] = self.client_app.to_alipay_dict()
            else:
                params['client_app'] = self.client_app
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.immediate_sync:
            if hasattr(self.immediate_sync, 'to_alipay_dict'):
                params['immediate_sync'] = self.immediate_sync.to_alipay_dict()
            else:
                params['immediate_sync'] = self.immediate_sync
        if self.link_token:
            if hasattr(self.link_token, 'to_alipay_dict'):
                params['link_token'] = self.link_token.to_alipay_dict()
            else:
                params['link_token'] = self.link_token
        if self.os_type:
            if hasattr(self.os_type, 'to_alipay_dict'):
                params['os_type'] = self.os_type.to_alipay_dict()
            else:
                params['os_type'] = self.os_type
        if self.payload:
            if hasattr(self.payload, 'to_alipay_dict'):
                params['payload'] = self.payload.to_alipay_dict()
            else:
                params['payload'] = self.payload
        if self.third_msg_id:
            if hasattr(self.third_msg_id, 'to_alipay_dict'):
                params['third_msg_id'] = self.third_msg_id.to_alipay_dict()
            else:
                params['third_msg_id'] = self.third_msg_id
        if self.valid_end:
            if hasattr(self.valid_end, 'to_alipay_dict'):
                params['valid_end'] = self.valid_end.to_alipay_dict()
            else:
                params['valid_end'] = self.valid_end
        if self.valid_start:
            if hasattr(self.valid_start, 'to_alipay_dict'):
                params['valid_start'] = self.valid_start.to_alipay_dict()
            else:
                params['valid_start'] = self.valid_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasSyncSingledataSendModel()
        if 'app_max_version' in d:
            o.app_max_version = d['app_max_version']
        if 'app_min_version' in d:
            o.app_min_version = d['app_min_version']
        if 'binary_payload' in d:
            o.binary_payload = d['binary_payload']
        if 'biz_tag' in d:
            o.biz_tag = d['biz_tag']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'client_app' in d:
            o.client_app = d['client_app']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'immediate_sync' in d:
            o.immediate_sync = d['immediate_sync']
        if 'link_token' in d:
            o.link_token = d['link_token']
        if 'os_type' in d:
            o.os_type = d['os_type']
        if 'payload' in d:
            o.payload = d['payload']
        if 'third_msg_id' in d:
            o.third_msg_id = d['third_msg_id']
        if 'valid_end' in d:
            o.valid_end = d['valid_end']
        if 'valid_start' in d:
            o.valid_start = d['valid_start']
        return o



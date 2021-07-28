#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WorldTicketType import WorldTicketType


class WorldOfflineDataInfo(object):

    def __init__(self):
        self._auth_mode = None
        self._available_ticket_types = None
        self._cert_type = None
        self._config = None
        self._data_from = None
        self._expire_time = None
        self._offline_data = None
        self._private_key = None
        self._qrcode = None
        self._script_mac = None
        self._script_name = None
        self._script_type = None
        self._upload_raw_code = None
        self._use_script = None

    @property
    def auth_mode(self):
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, value):
        self._auth_mode = value
    @property
    def available_ticket_types(self):
        return self._available_ticket_types

    @available_ticket_types.setter
    def available_ticket_types(self, value):
        if isinstance(value, list):
            self._available_ticket_types = list()
            for i in value:
                if isinstance(i, WorldTicketType):
                    self._available_ticket_types.append(i)
                else:
                    self._available_ticket_types.append(WorldTicketType.from_alipay_dict(i))
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value
    @property
    def data_from(self):
        return self._data_from

    @data_from.setter
    def data_from(self, value):
        self._data_from = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def offline_data(self):
        return self._offline_data

    @offline_data.setter
    def offline_data(self, value):
        self._offline_data = value
    @property
    def private_key(self):
        return self._private_key

    @private_key.setter
    def private_key(self, value):
        self._private_key = value
    @property
    def qrcode(self):
        return self._qrcode

    @qrcode.setter
    def qrcode(self, value):
        self._qrcode = value
    @property
    def script_mac(self):
        return self._script_mac

    @script_mac.setter
    def script_mac(self, value):
        self._script_mac = value
    @property
    def script_name(self):
        return self._script_name

    @script_name.setter
    def script_name(self, value):
        self._script_name = value
    @property
    def script_type(self):
        return self._script_type

    @script_type.setter
    def script_type(self, value):
        self._script_type = value
    @property
    def upload_raw_code(self):
        return self._upload_raw_code

    @upload_raw_code.setter
    def upload_raw_code(self, value):
        self._upload_raw_code = value
    @property
    def use_script(self):
        return self._use_script

    @use_script.setter
    def use_script(self, value):
        self._use_script = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_mode:
            if hasattr(self.auth_mode, 'to_alipay_dict'):
                params['auth_mode'] = self.auth_mode.to_alipay_dict()
            else:
                params['auth_mode'] = self.auth_mode
        if self.available_ticket_types:
            if isinstance(self.available_ticket_types, list):
                for i in range(0, len(self.available_ticket_types)):
                    element = self.available_ticket_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_ticket_types[i] = element.to_alipay_dict()
            if hasattr(self.available_ticket_types, 'to_alipay_dict'):
                params['available_ticket_types'] = self.available_ticket_types.to_alipay_dict()
            else:
                params['available_ticket_types'] = self.available_ticket_types
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.config:
            if hasattr(self.config, 'to_alipay_dict'):
                params['config'] = self.config.to_alipay_dict()
            else:
                params['config'] = self.config
        if self.data_from:
            if hasattr(self.data_from, 'to_alipay_dict'):
                params['data_from'] = self.data_from.to_alipay_dict()
            else:
                params['data_from'] = self.data_from
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.offline_data:
            if hasattr(self.offline_data, 'to_alipay_dict'):
                params['offline_data'] = self.offline_data.to_alipay_dict()
            else:
                params['offline_data'] = self.offline_data
        if self.private_key:
            if hasattr(self.private_key, 'to_alipay_dict'):
                params['private_key'] = self.private_key.to_alipay_dict()
            else:
                params['private_key'] = self.private_key
        if self.qrcode:
            if hasattr(self.qrcode, 'to_alipay_dict'):
                params['qrcode'] = self.qrcode.to_alipay_dict()
            else:
                params['qrcode'] = self.qrcode
        if self.script_mac:
            if hasattr(self.script_mac, 'to_alipay_dict'):
                params['script_mac'] = self.script_mac.to_alipay_dict()
            else:
                params['script_mac'] = self.script_mac
        if self.script_name:
            if hasattr(self.script_name, 'to_alipay_dict'):
                params['script_name'] = self.script_name.to_alipay_dict()
            else:
                params['script_name'] = self.script_name
        if self.script_type:
            if hasattr(self.script_type, 'to_alipay_dict'):
                params['script_type'] = self.script_type.to_alipay_dict()
            else:
                params['script_type'] = self.script_type
        if self.upload_raw_code:
            if hasattr(self.upload_raw_code, 'to_alipay_dict'):
                params['upload_raw_code'] = self.upload_raw_code.to_alipay_dict()
            else:
                params['upload_raw_code'] = self.upload_raw_code
        if self.use_script:
            if hasattr(self.use_script, 'to_alipay_dict'):
                params['use_script'] = self.use_script.to_alipay_dict()
            else:
                params['use_script'] = self.use_script
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorldOfflineDataInfo()
        if 'auth_mode' in d:
            o.auth_mode = d['auth_mode']
        if 'available_ticket_types' in d:
            o.available_ticket_types = d['available_ticket_types']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'config' in d:
            o.config = d['config']
        if 'data_from' in d:
            o.data_from = d['data_from']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'offline_data' in d:
            o.offline_data = d['offline_data']
        if 'private_key' in d:
            o.private_key = d['private_key']
        if 'qrcode' in d:
            o.qrcode = d['qrcode']
        if 'script_mac' in d:
            o.script_mac = d['script_mac']
        if 'script_name' in d:
            o.script_name = d['script_name']
        if 'script_type' in d:
            o.script_type = d['script_type']
        if 'upload_raw_code' in d:
            o.upload_raw_code = d['upload_raw_code']
        if 'use_script' in d:
            o.use_script = d['use_script']
        return o



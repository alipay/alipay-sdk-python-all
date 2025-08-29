#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChatExtraParams(object):

    def __init__(self):
        self._agent_ext_info = None
        self._cert_no = None
        self._cert_type = None
        self._city_code = None
        self._city_name = None
        self._entrance = None
        self._from_source = None
        self._latitude = None
        self._longitude = None
        self._phone_no = None
        self._plugin_env = None

    @property
    def agent_ext_info(self):
        return self._agent_ext_info

    @agent_ext_info.setter
    def agent_ext_info(self, value):
        self._agent_ext_info = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def entrance(self):
        return self._entrance

    @entrance.setter
    def entrance(self, value):
        self._entrance = value
    @property
    def from_source(self):
        return self._from_source

    @from_source.setter
    def from_source(self, value):
        self._from_source = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def plugin_env(self):
        return self._plugin_env

    @plugin_env.setter
    def plugin_env(self, value):
        self._plugin_env = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_ext_info:
            if hasattr(self.agent_ext_info, 'to_alipay_dict'):
                params['agent_ext_info'] = self.agent_ext_info.to_alipay_dict()
            else:
                params['agent_ext_info'] = self.agent_ext_info
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.entrance:
            if hasattr(self.entrance, 'to_alipay_dict'):
                params['entrance'] = self.entrance.to_alipay_dict()
            else:
                params['entrance'] = self.entrance
        if self.from_source:
            if hasattr(self.from_source, 'to_alipay_dict'):
                params['from_source'] = self.from_source.to_alipay_dict()
            else:
                params['from_source'] = self.from_source
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.plugin_env:
            if hasattr(self.plugin_env, 'to_alipay_dict'):
                params['plugin_env'] = self.plugin_env.to_alipay_dict()
            else:
                params['plugin_env'] = self.plugin_env
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatExtraParams()
        if 'agent_ext_info' in d:
            o.agent_ext_info = d['agent_ext_info']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'entrance' in d:
            o.entrance = d['entrance']
        if 'from_source' in d:
            o.from_source = d['from_source']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'plugin_env' in d:
            o.plugin_env = d['plugin_env']
        return o



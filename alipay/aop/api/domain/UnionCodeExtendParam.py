#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnionCodeExtendParam(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._channel_id = None
        self._city = None
        self._client_ip = None
        self._code_create_time = None
        self._country = None
        self._exhibit_role = None
        self._exhibit_role_cert_no = None
        self._exhibit_role_cert_type = None
        self._exhibit_role_name = None
        self._machine_type = None
        self._province = None
        self._user_name = None

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
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def code_create_time(self):
        return self._code_create_time

    @code_create_time.setter
    def code_create_time(self, value):
        self._code_create_time = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def exhibit_role(self):
        return self._exhibit_role

    @exhibit_role.setter
    def exhibit_role(self, value):
        self._exhibit_role = value
    @property
    def exhibit_role_cert_no(self):
        return self._exhibit_role_cert_no

    @exhibit_role_cert_no.setter
    def exhibit_role_cert_no(self, value):
        self._exhibit_role_cert_no = value
    @property
    def exhibit_role_cert_type(self):
        return self._exhibit_role_cert_type

    @exhibit_role_cert_type.setter
    def exhibit_role_cert_type(self, value):
        self._exhibit_role_cert_type = value
    @property
    def exhibit_role_name(self):
        return self._exhibit_role_name

    @exhibit_role_name.setter
    def exhibit_role_name(self, value):
        self._exhibit_role_name = value
    @property
    def machine_type(self):
        return self._machine_type

    @machine_type.setter
    def machine_type(self, value):
        self._machine_type = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.code_create_time:
            if hasattr(self.code_create_time, 'to_alipay_dict'):
                params['code_create_time'] = self.code_create_time.to_alipay_dict()
            else:
                params['code_create_time'] = self.code_create_time
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.exhibit_role:
            if hasattr(self.exhibit_role, 'to_alipay_dict'):
                params['exhibit_role'] = self.exhibit_role.to_alipay_dict()
            else:
                params['exhibit_role'] = self.exhibit_role
        if self.exhibit_role_cert_no:
            if hasattr(self.exhibit_role_cert_no, 'to_alipay_dict'):
                params['exhibit_role_cert_no'] = self.exhibit_role_cert_no.to_alipay_dict()
            else:
                params['exhibit_role_cert_no'] = self.exhibit_role_cert_no
        if self.exhibit_role_cert_type:
            if hasattr(self.exhibit_role_cert_type, 'to_alipay_dict'):
                params['exhibit_role_cert_type'] = self.exhibit_role_cert_type.to_alipay_dict()
            else:
                params['exhibit_role_cert_type'] = self.exhibit_role_cert_type
        if self.exhibit_role_name:
            if hasattr(self.exhibit_role_name, 'to_alipay_dict'):
                params['exhibit_role_name'] = self.exhibit_role_name.to_alipay_dict()
            else:
                params['exhibit_role_name'] = self.exhibit_role_name
        if self.machine_type:
            if hasattr(self.machine_type, 'to_alipay_dict'):
                params['machine_type'] = self.machine_type.to_alipay_dict()
            else:
                params['machine_type'] = self.machine_type
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnionCodeExtendParam()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'city' in d:
            o.city = d['city']
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'code_create_time' in d:
            o.code_create_time = d['code_create_time']
        if 'country' in d:
            o.country = d['country']
        if 'exhibit_role' in d:
            o.exhibit_role = d['exhibit_role']
        if 'exhibit_role_cert_no' in d:
            o.exhibit_role_cert_no = d['exhibit_role_cert_no']
        if 'exhibit_role_cert_type' in d:
            o.exhibit_role_cert_type = d['exhibit_role_cert_type']
        if 'exhibit_role_name' in d:
            o.exhibit_role_name = d['exhibit_role_name']
        if 'machine_type' in d:
            o.machine_type = d['machine_type']
        if 'province' in d:
            o.province = d['province']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniCloudAossuggestQueryModel(object):

    def __init__(self):
        self._city_code = None
        self._client_env = None
        self._device_id = None
        self._latitude = None
        self._longitude = None
        self._open_id = None
        self._project_id = None
        self._query = None
        self._size = None
        self._user_id = None
        self._user_id_type = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def client_env(self):
        return self._client_env

    @client_env.setter
    def client_env(self, value):
        self._client_env = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_type(self):
        return self._user_id_type

    @user_id_type.setter
    def user_id_type(self, value):
        self._user_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.client_env:
            if hasattr(self.client_env, 'to_alipay_dict'):
                params['client_env'] = self.client_env.to_alipay_dict()
            else:
                params['client_env'] = self.client_env
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
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
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_type:
            if hasattr(self.user_id_type, 'to_alipay_dict'):
                params['user_id_type'] = self.user_id_type.to_alipay_dict()
            else:
                params['user_id_type'] = self.user_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniCloudAossuggestQueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'client_env' in d:
            o.client_env = d['client_env']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'query' in d:
            o.query = d['query']
        if 'size' in d:
            o.size = d['size']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_type' in d:
            o.user_id_type = d['user_id_type']
        return o



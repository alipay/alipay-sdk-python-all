#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApeRecContext(object):

    def __init__(self):
        self._city_code = None
        self._client_env = None
        self._current_item_id = None
        self._device_id = None
        self._latitude = None
        self._longitude = None

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
    def current_item_id(self):
        return self._current_item_id

    @current_item_id.setter
    def current_item_id(self, value):
        self._current_item_id = value
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
        if self.current_item_id:
            if hasattr(self.current_item_id, 'to_alipay_dict'):
                params['current_item_id'] = self.current_item_id.to_alipay_dict()
            else:
                params['current_item_id'] = self.current_item_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApeRecContext()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'client_env' in d:
            o.client_env = d['client_env']
        if 'current_item_id' in d:
            o.current_item_id = d['current_item_id']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        return o



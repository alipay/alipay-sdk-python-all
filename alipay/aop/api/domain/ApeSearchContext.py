#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApeSearchContext(object):

    def __init__(self):
        self._city_code = None
        self._client_env = None
        self._device_id = None
        self._expose_item_list = None
        self._filter_condition = None
        self._latitude = None
        self._longitude = None
        self._size = None
        self._sort_type = None
        self._start_index = None

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
    def expose_item_list(self):
        return self._expose_item_list

    @expose_item_list.setter
    def expose_item_list(self, value):
        if isinstance(value, list):
            self._expose_item_list = list()
            for i in value:
                self._expose_item_list.append(i)
    @property
    def filter_condition(self):
        return self._filter_condition

    @filter_condition.setter
    def filter_condition(self, value):
        self._filter_condition = value
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
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def sort_type(self):
        return self._sort_type

    @sort_type.setter
    def sort_type(self, value):
        self._sort_type = value
    @property
    def start_index(self):
        return self._start_index

    @start_index.setter
    def start_index(self, value):
        self._start_index = value


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
        if self.expose_item_list:
            if isinstance(self.expose_item_list, list):
                for i in range(0, len(self.expose_item_list)):
                    element = self.expose_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.expose_item_list[i] = element.to_alipay_dict()
            if hasattr(self.expose_item_list, 'to_alipay_dict'):
                params['expose_item_list'] = self.expose_item_list.to_alipay_dict()
            else:
                params['expose_item_list'] = self.expose_item_list
        if self.filter_condition:
            if hasattr(self.filter_condition, 'to_alipay_dict'):
                params['filter_condition'] = self.filter_condition.to_alipay_dict()
            else:
                params['filter_condition'] = self.filter_condition
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
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.sort_type:
            if hasattr(self.sort_type, 'to_alipay_dict'):
                params['sort_type'] = self.sort_type.to_alipay_dict()
            else:
                params['sort_type'] = self.sort_type
        if self.start_index:
            if hasattr(self.start_index, 'to_alipay_dict'):
                params['start_index'] = self.start_index.to_alipay_dict()
            else:
                params['start_index'] = self.start_index
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApeSearchContext()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'client_env' in d:
            o.client_env = d['client_env']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'expose_item_list' in d:
            o.expose_item_list = d['expose_item_list']
        if 'filter_condition' in d:
            o.filter_condition = d['filter_condition']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'size' in d:
            o.size = d['size']
        if 'sort_type' in d:
            o.sort_type = d['sort_type']
        if 'start_index' in d:
            o.start_index = d['start_index']
        return o



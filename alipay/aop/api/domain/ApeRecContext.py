#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApeRecContext(object):

    def __init__(self):
        self._black_index_list = None
        self._cate = None
        self._city_code = None
        self._client_env = None
        self._current_item_id = None
        self._device_id = None
        self._landing_item_list = None
        self._latitude = None
        self._lbs_distance = None
        self._longitude = None
        self._other_index_list = None
        self._select_id_list = None
        self._tags = None

    @property
    def black_index_list(self):
        return self._black_index_list

    @black_index_list.setter
    def black_index_list(self, value):
        if isinstance(value, list):
            self._black_index_list = list()
            for i in value:
                self._black_index_list.append(i)
    @property
    def cate(self):
        return self._cate

    @cate.setter
    def cate(self, value):
        if isinstance(value, list):
            self._cate = list()
            for i in value:
                self._cate.append(i)
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
    def landing_item_list(self):
        return self._landing_item_list

    @landing_item_list.setter
    def landing_item_list(self, value):
        if isinstance(value, list):
            self._landing_item_list = list()
            for i in value:
                self._landing_item_list.append(i)
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def lbs_distance(self):
        return self._lbs_distance

    @lbs_distance.setter
    def lbs_distance(self, value):
        self._lbs_distance = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def other_index_list(self):
        return self._other_index_list

    @other_index_list.setter
    def other_index_list(self, value):
        if isinstance(value, list):
            self._other_index_list = list()
            for i in value:
                self._other_index_list.append(i)
    @property
    def select_id_list(self):
        return self._select_id_list

    @select_id_list.setter
    def select_id_list(self, value):
        if isinstance(value, list):
            self._select_id_list = list()
            for i in value:
                self._select_id_list.append(i)
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.black_index_list:
            if isinstance(self.black_index_list, list):
                for i in range(0, len(self.black_index_list)):
                    element = self.black_index_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.black_index_list[i] = element.to_alipay_dict()
            if hasattr(self.black_index_list, 'to_alipay_dict'):
                params['black_index_list'] = self.black_index_list.to_alipay_dict()
            else:
                params['black_index_list'] = self.black_index_list
        if self.cate:
            if isinstance(self.cate, list):
                for i in range(0, len(self.cate)):
                    element = self.cate[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cate[i] = element.to_alipay_dict()
            if hasattr(self.cate, 'to_alipay_dict'):
                params['cate'] = self.cate.to_alipay_dict()
            else:
                params['cate'] = self.cate
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
        if self.landing_item_list:
            if isinstance(self.landing_item_list, list):
                for i in range(0, len(self.landing_item_list)):
                    element = self.landing_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.landing_item_list[i] = element.to_alipay_dict()
            if hasattr(self.landing_item_list, 'to_alipay_dict'):
                params['landing_item_list'] = self.landing_item_list.to_alipay_dict()
            else:
                params['landing_item_list'] = self.landing_item_list
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.lbs_distance:
            if hasattr(self.lbs_distance, 'to_alipay_dict'):
                params['lbs_distance'] = self.lbs_distance.to_alipay_dict()
            else:
                params['lbs_distance'] = self.lbs_distance
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.other_index_list:
            if isinstance(self.other_index_list, list):
                for i in range(0, len(self.other_index_list)):
                    element = self.other_index_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_index_list[i] = element.to_alipay_dict()
            if hasattr(self.other_index_list, 'to_alipay_dict'):
                params['other_index_list'] = self.other_index_list.to_alipay_dict()
            else:
                params['other_index_list'] = self.other_index_list
        if self.select_id_list:
            if isinstance(self.select_id_list, list):
                for i in range(0, len(self.select_id_list)):
                    element = self.select_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.select_id_list[i] = element.to_alipay_dict()
            if hasattr(self.select_id_list, 'to_alipay_dict'):
                params['select_id_list'] = self.select_id_list.to_alipay_dict()
            else:
                params['select_id_list'] = self.select_id_list
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApeRecContext()
        if 'black_index_list' in d:
            o.black_index_list = d['black_index_list']
        if 'cate' in d:
            o.cate = d['cate']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'client_env' in d:
            o.client_env = d['client_env']
        if 'current_item_id' in d:
            o.current_item_id = d['current_item_id']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'landing_item_list' in d:
            o.landing_item_list = d['landing_item_list']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'lbs_distance' in d:
            o.lbs_distance = d['lbs_distance']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'other_index_list' in d:
            o.other_index_list = d['other_index_list']
        if 'select_id_list' in d:
            o.select_id_list = d['select_id_list']
        if 'tags' in d:
            o.tags = d['tags']
        return o



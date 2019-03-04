#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMemberDataItemBigbuyQueryModel(object):

    def __init__(self):
        self._city_code = None
        self._latitude = None
        self._longitude = None
        self._space_code_list = None
        self._user_id = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
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
    def space_code_list(self):
        return self._space_code_list

    @space_code_list.setter
    def space_code_list(self, value):
        if isinstance(value, list):
            self._space_code_list = list()
            for i in value:
                self._space_code_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
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
        if self.space_code_list:
            if isinstance(self.space_code_list, list):
                for i in range(0, len(self.space_code_list)):
                    element = self.space_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.space_code_list[i] = element.to_alipay_dict()
            if hasattr(self.space_code_list, 'to_alipay_dict'):
                params['space_code_list'] = self.space_code_list.to_alipay_dict()
            else:
                params['space_code_list'] = self.space_code_list
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
        o = KoubeiMemberDataItemBigbuyQueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'space_code_list' in d:
            o.space_code_list = d['space_code_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMallCircleRecommenditemQueryModel(object):

    def __init__(self):
        self._city_code = None
        self._data_set_id = None
        self._display_channel = None
        self._latitude = None
        self._longitude = None
        self._page_size = None
        self._start = None
        self._terminal_type = None
        self._tribe_id = None
        self._user_id = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def data_set_id(self):
        return self._data_set_id

    @data_set_id.setter
    def data_set_id(self, value):
        self._data_set_id = value
    @property
    def display_channel(self):
        return self._display_channel

    @display_channel.setter
    def display_channel(self, value):
        self._display_channel = value
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
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value
    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value
    @property
    def tribe_id(self):
        return self._tribe_id

    @tribe_id.setter
    def tribe_id(self, value):
        self._tribe_id = value
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
        if self.data_set_id:
            if hasattr(self.data_set_id, 'to_alipay_dict'):
                params['data_set_id'] = self.data_set_id.to_alipay_dict()
            else:
                params['data_set_id'] = self.data_set_id
        if self.display_channel:
            if hasattr(self.display_channel, 'to_alipay_dict'):
                params['display_channel'] = self.display_channel.to_alipay_dict()
            else:
                params['display_channel'] = self.display_channel
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
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.start:
            if hasattr(self.start, 'to_alipay_dict'):
                params['start'] = self.start.to_alipay_dict()
            else:
                params['start'] = self.start
        if self.terminal_type:
            if hasattr(self.terminal_type, 'to_alipay_dict'):
                params['terminal_type'] = self.terminal_type.to_alipay_dict()
            else:
                params['terminal_type'] = self.terminal_type
        if self.tribe_id:
            if hasattr(self.tribe_id, 'to_alipay_dict'):
                params['tribe_id'] = self.tribe_id.to_alipay_dict()
            else:
                params['tribe_id'] = self.tribe_id
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
        o = KoubeiMallCircleRecommenditemQueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'data_set_id' in d:
            o.data_set_id = d['data_set_id']
        if 'display_channel' in d:
            o.display_channel = d['display_channel']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start' in d:
            o.start = d['start']
        if 'terminal_type' in d:
            o.terminal_type = d['terminal_type']
        if 'tribe_id' in d:
            o.tribe_id = d['tribe_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



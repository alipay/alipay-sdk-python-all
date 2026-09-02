#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CheckInRecordDTO(object):

    def __init__(self):
        self._biz_code = None
        self._check_in_method = None
        self._check_in_time = None
        self._latitude = None
        self._location = None
        self._longitude = None
        self._open_id = None
        self._user_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def check_in_method(self):
        return self._check_in_method

    @check_in_method.setter
    def check_in_method(self, value):
        self._check_in_method = value
    @property
    def check_in_time(self):
        return self._check_in_time

    @check_in_time.setter
    def check_in_time(self, value):
        self._check_in_time = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.check_in_method:
            if hasattr(self.check_in_method, 'to_alipay_dict'):
                params['check_in_method'] = self.check_in_method.to_alipay_dict()
            else:
                params['check_in_method'] = self.check_in_method
        if self.check_in_time:
            if hasattr(self.check_in_time, 'to_alipay_dict'):
                params['check_in_time'] = self.check_in_time.to_alipay_dict()
            else:
                params['check_in_time'] = self.check_in_time
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
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
        o = CheckInRecordDTO()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'check_in_method' in d:
            o.check_in_method = d['check_in_method']
        if 'check_in_time' in d:
            o.check_in_time = d['check_in_time']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'location' in d:
            o.location = d['location']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



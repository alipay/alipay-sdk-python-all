#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarbonJusticeQueryOpenapiDTO(object):

    def __init__(self):
        self._distance = None
        self._open_id = None
        self._pay_time = None
        self._trip_type = None
        self._user_id = None

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def trip_type(self):
        return self._trip_type

    @trip_type.setter
    def trip_type(self, value):
        self._trip_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.trip_type:
            if hasattr(self.trip_type, 'to_alipay_dict'):
                params['trip_type'] = self.trip_type.to_alipay_dict()
            else:
                params['trip_type'] = self.trip_type
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
        o = CarbonJusticeQueryOpenapiDTO()
        if 'distance' in d:
            o.distance = d['distance']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'trip_type' in d:
            o.trip_type = d['trip_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



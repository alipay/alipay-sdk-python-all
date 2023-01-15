#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppTestGrayQueryModel(object):

    def __init__(self):
        self._buy_open_id = None
        self._city_id = None
        self._latitude = None
        self._uid = None

    @property
    def buy_open_id(self):
        return self._buy_open_id

    @buy_open_id.setter
    def buy_open_id(self, value):
        self._buy_open_id = value
    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.buy_open_id:
            if hasattr(self.buy_open_id, 'to_alipay_dict'):
                params['buy_open_id'] = self.buy_open_id.to_alipay_dict()
            else:
                params['buy_open_id'] = self.buy_open_id
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppTestGrayQueryModel()
        if 'buy_open_id' in d:
            o.buy_open_id = d['buy_open_id']
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'uid' in d:
            o.uid = d['uid']
        return o



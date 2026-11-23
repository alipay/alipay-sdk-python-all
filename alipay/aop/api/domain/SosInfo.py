#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SosInfo(object):

    def __init__(self):
        self._alert_address_info = None
        self._id_type = None
        self._imei = None
        self._is_self = None
        self._latitude = None
        self._location_type = None
        self._longitude = None
        self._user_address_info = None

    @property
    def alert_address_info(self):
        return self._alert_address_info

    @alert_address_info.setter
    def alert_address_info(self, value):
        self._alert_address_info = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def is_self(self):
        return self._is_self

    @is_self.setter
    def is_self(self, value):
        self._is_self = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def location_type(self):
        return self._location_type

    @location_type.setter
    def location_type(self, value):
        self._location_type = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def user_address_info(self):
        return self._user_address_info

    @user_address_info.setter
    def user_address_info(self, value):
        self._user_address_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.alert_address_info:
            if hasattr(self.alert_address_info, 'to_alipay_dict'):
                params['alert_address_info'] = self.alert_address_info.to_alipay_dict()
            else:
                params['alert_address_info'] = self.alert_address_info
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.is_self:
            if hasattr(self.is_self, 'to_alipay_dict'):
                params['is_self'] = self.is_self.to_alipay_dict()
            else:
                params['is_self'] = self.is_self
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.location_type:
            if hasattr(self.location_type, 'to_alipay_dict'):
                params['location_type'] = self.location_type.to_alipay_dict()
            else:
                params['location_type'] = self.location_type
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.user_address_info:
            if hasattr(self.user_address_info, 'to_alipay_dict'):
                params['user_address_info'] = self.user_address_info.to_alipay_dict()
            else:
                params['user_address_info'] = self.user_address_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SosInfo()
        if 'alert_address_info' in d:
            o.alert_address_info = d['alert_address_info']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'imei' in d:
            o.imei = d['imei']
        if 'is_self' in d:
            o.is_self = d['is_self']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'location_type' in d:
            o.location_type = d['location_type']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'user_address_info' in d:
            o.user_address_info = d['user_address_info']
        return o



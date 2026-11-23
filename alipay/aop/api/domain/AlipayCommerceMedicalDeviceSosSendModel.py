#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDeviceSosSendModel(object):

    def __init__(self):
        self._address = None
        self._aq_user_id = None
        self._assistance_id = None
        self._device_id = None
        self._latitude = None
        self._location_at = None
        self._location_type = None
        self._longitude = None
        self._occurred_at = None
        self._operation_type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def aq_user_id(self):
        return self._aq_user_id

    @aq_user_id.setter
    def aq_user_id(self, value):
        self._aq_user_id = value
    @property
    def assistance_id(self):
        return self._assistance_id

    @assistance_id.setter
    def assistance_id(self, value):
        self._assistance_id = value
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
    def location_at(self):
        return self._location_at

    @location_at.setter
    def location_at(self, value):
        self._location_at = value
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
    def occurred_at(self):
        return self._occurred_at

    @occurred_at.setter
    def occurred_at(self, value):
        self._occurred_at = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.aq_user_id:
            if hasattr(self.aq_user_id, 'to_alipay_dict'):
                params['aq_user_id'] = self.aq_user_id.to_alipay_dict()
            else:
                params['aq_user_id'] = self.aq_user_id
        if self.assistance_id:
            if hasattr(self.assistance_id, 'to_alipay_dict'):
                params['assistance_id'] = self.assistance_id.to_alipay_dict()
            else:
                params['assistance_id'] = self.assistance_id
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
        if self.location_at:
            if hasattr(self.location_at, 'to_alipay_dict'):
                params['location_at'] = self.location_at.to_alipay_dict()
            else:
                params['location_at'] = self.location_at
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
        if self.occurred_at:
            if hasattr(self.occurred_at, 'to_alipay_dict'):
                params['occurred_at'] = self.occurred_at.to_alipay_dict()
            else:
                params['occurred_at'] = self.occurred_at
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDeviceSosSendModel()
        if 'address' in d:
            o.address = d['address']
        if 'aq_user_id' in d:
            o.aq_user_id = d['aq_user_id']
        if 'assistance_id' in d:
            o.assistance_id = d['assistance_id']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'location_at' in d:
            o.location_at = d['location_at']
        if 'location_type' in d:
            o.location_type = d['location_type']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'occurred_at' in d:
            o.occurred_at = d['occurred_at']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        return o



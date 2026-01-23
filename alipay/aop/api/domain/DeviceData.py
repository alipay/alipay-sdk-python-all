#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceData(object):

    def __init__(self):
        self._community_code = None
        self._community_name = None
        self._device_sn = None
        self._device_source = None
        self._device_status = None
        self._device_type = None
        self._latitude = None
        self._longitude = None
        self._nfc_card_id = None
        self._point_code = None
        self._point_name = None
        self._response_time = None

    @property
    def community_code(self):
        return self._community_code

    @community_code.setter
    def community_code(self, value):
        self._community_code = value
    @property
    def community_name(self):
        return self._community_name

    @community_name.setter
    def community_name(self, value):
        self._community_name = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def device_source(self):
        return self._device_source

    @device_source.setter
    def device_source(self, value):
        self._device_source = value
    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, value):
        self._device_status = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
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
    def nfc_card_id(self):
        return self._nfc_card_id

    @nfc_card_id.setter
    def nfc_card_id(self, value):
        self._nfc_card_id = value
    @property
    def point_code(self):
        return self._point_code

    @point_code.setter
    def point_code(self, value):
        self._point_code = value
    @property
    def point_name(self):
        return self._point_name

    @point_name.setter
    def point_name(self, value):
        self._point_name = value
    @property
    def response_time(self):
        return self._response_time

    @response_time.setter
    def response_time(self, value):
        self._response_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.community_code:
            if hasattr(self.community_code, 'to_alipay_dict'):
                params['community_code'] = self.community_code.to_alipay_dict()
            else:
                params['community_code'] = self.community_code
        if self.community_name:
            if hasattr(self.community_name, 'to_alipay_dict'):
                params['community_name'] = self.community_name.to_alipay_dict()
            else:
                params['community_name'] = self.community_name
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.device_source:
            if hasattr(self.device_source, 'to_alipay_dict'):
                params['device_source'] = self.device_source.to_alipay_dict()
            else:
                params['device_source'] = self.device_source
        if self.device_status:
            if hasattr(self.device_status, 'to_alipay_dict'):
                params['device_status'] = self.device_status.to_alipay_dict()
            else:
                params['device_status'] = self.device_status
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
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
        if self.nfc_card_id:
            if hasattr(self.nfc_card_id, 'to_alipay_dict'):
                params['nfc_card_id'] = self.nfc_card_id.to_alipay_dict()
            else:
                params['nfc_card_id'] = self.nfc_card_id
        if self.point_code:
            if hasattr(self.point_code, 'to_alipay_dict'):
                params['point_code'] = self.point_code.to_alipay_dict()
            else:
                params['point_code'] = self.point_code
        if self.point_name:
            if hasattr(self.point_name, 'to_alipay_dict'):
                params['point_name'] = self.point_name.to_alipay_dict()
            else:
                params['point_name'] = self.point_name
        if self.response_time:
            if hasattr(self.response_time, 'to_alipay_dict'):
                params['response_time'] = self.response_time.to_alipay_dict()
            else:
                params['response_time'] = self.response_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceData()
        if 'community_code' in d:
            o.community_code = d['community_code']
        if 'community_name' in d:
            o.community_name = d['community_name']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'device_source' in d:
            o.device_source = d['device_source']
        if 'device_status' in d:
            o.device_status = d['device_status']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'nfc_card_id' in d:
            o.nfc_card_id = d['nfc_card_id']
        if 'point_code' in d:
            o.point_code = d['point_code']
        if 'point_name' in d:
            o.point_name = d['point_name']
        if 'response_time' in d:
            o.response_time = d['response_time']
        return o



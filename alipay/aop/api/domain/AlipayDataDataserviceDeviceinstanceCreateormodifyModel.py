#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceDeviceinstanceCreateormodifyModel(object):

    def __init__(self):
        self._address = None
        self._biz_token = None
        self._building_name = None
        self._city_name = None
        self._device_instance_ext_info = None
        self._device_instance_id = None
        self._device_instance_pos_name = None
        self._district = None
        self._height = None
        self._latitude = None
        self._longitude = None
        self._province_name = None
        self._screen_size = None
        self._status = None
        self._width = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def building_name(self):
        return self._building_name

    @building_name.setter
    def building_name(self, value):
        self._building_name = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def device_instance_ext_info(self):
        return self._device_instance_ext_info

    @device_instance_ext_info.setter
    def device_instance_ext_info(self, value):
        self._device_instance_ext_info = value
    @property
    def device_instance_id(self):
        return self._device_instance_id

    @device_instance_id.setter
    def device_instance_id(self, value):
        self._device_instance_id = value
    @property
    def device_instance_pos_name(self):
        return self._device_instance_pos_name

    @device_instance_pos_name.setter
    def device_instance_pos_name(self, value):
        self._device_instance_pos_name = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
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
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def screen_size(self):
        return self._screen_size

    @screen_size.setter
    def screen_size(self, value):
        self._screen_size = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.building_name:
            if hasattr(self.building_name, 'to_alipay_dict'):
                params['building_name'] = self.building_name.to_alipay_dict()
            else:
                params['building_name'] = self.building_name
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.device_instance_ext_info:
            if hasattr(self.device_instance_ext_info, 'to_alipay_dict'):
                params['device_instance_ext_info'] = self.device_instance_ext_info.to_alipay_dict()
            else:
                params['device_instance_ext_info'] = self.device_instance_ext_info
        if self.device_instance_id:
            if hasattr(self.device_instance_id, 'to_alipay_dict'):
                params['device_instance_id'] = self.device_instance_id.to_alipay_dict()
            else:
                params['device_instance_id'] = self.device_instance_id
        if self.device_instance_pos_name:
            if hasattr(self.device_instance_pos_name, 'to_alipay_dict'):
                params['device_instance_pos_name'] = self.device_instance_pos_name.to_alipay_dict()
            else:
                params['device_instance_pos_name'] = self.device_instance_pos_name
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
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
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.screen_size:
            if hasattr(self.screen_size, 'to_alipay_dict'):
                params['screen_size'] = self.screen_size.to_alipay_dict()
            else:
                params['screen_size'] = self.screen_size
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDeviceinstanceCreateormodifyModel()
        if 'address' in d:
            o.address = d['address']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'building_name' in d:
            o.building_name = d['building_name']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'device_instance_ext_info' in d:
            o.device_instance_ext_info = d['device_instance_ext_info']
        if 'device_instance_id' in d:
            o.device_instance_id = d['device_instance_id']
        if 'device_instance_pos_name' in d:
            o.device_instance_pos_name = d['device_instance_pos_name']
        if 'district' in d:
            o.district = d['district']
        if 'height' in d:
            o.height = d['height']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'screen_size' in d:
            o.screen_size = d['screen_size']
        if 'status' in d:
            o.status = d['status']
        if 'width' in d:
            o.width = d['width']
        return o



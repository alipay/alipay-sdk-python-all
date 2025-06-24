#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LocationPointInfoVO(object):

    def __init__(self):
        self._binding_card_id = None
        self._community_id = None
        self._floor_num = None
        self._latitude = None
        self._location_desc = None
        self._location_name = None
        self._location_point_id = None
        self._location_type = None
        self._longitude = None
        self._muti_floor = None
        self._out_location_point_id = None

    @property
    def binding_card_id(self):
        return self._binding_card_id

    @binding_card_id.setter
    def binding_card_id(self, value):
        self._binding_card_id = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def floor_num(self):
        return self._floor_num

    @floor_num.setter
    def floor_num(self, value):
        self._floor_num = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def location_desc(self):
        return self._location_desc

    @location_desc.setter
    def location_desc(self, value):
        self._location_desc = value
    @property
    def location_name(self):
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        self._location_name = value
    @property
    def location_point_id(self):
        return self._location_point_id

    @location_point_id.setter
    def location_point_id(self, value):
        self._location_point_id = value
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
    def muti_floor(self):
        return self._muti_floor

    @muti_floor.setter
    def muti_floor(self, value):
        self._muti_floor = value
    @property
    def out_location_point_id(self):
        return self._out_location_point_id

    @out_location_point_id.setter
    def out_location_point_id(self, value):
        self._out_location_point_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.binding_card_id:
            if hasattr(self.binding_card_id, 'to_alipay_dict'):
                params['binding_card_id'] = self.binding_card_id.to_alipay_dict()
            else:
                params['binding_card_id'] = self.binding_card_id
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.floor_num:
            if hasattr(self.floor_num, 'to_alipay_dict'):
                params['floor_num'] = self.floor_num.to_alipay_dict()
            else:
                params['floor_num'] = self.floor_num
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.location_desc:
            if hasattr(self.location_desc, 'to_alipay_dict'):
                params['location_desc'] = self.location_desc.to_alipay_dict()
            else:
                params['location_desc'] = self.location_desc
        if self.location_name:
            if hasattr(self.location_name, 'to_alipay_dict'):
                params['location_name'] = self.location_name.to_alipay_dict()
            else:
                params['location_name'] = self.location_name
        if self.location_point_id:
            if hasattr(self.location_point_id, 'to_alipay_dict'):
                params['location_point_id'] = self.location_point_id.to_alipay_dict()
            else:
                params['location_point_id'] = self.location_point_id
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
        if self.muti_floor:
            if hasattr(self.muti_floor, 'to_alipay_dict'):
                params['muti_floor'] = self.muti_floor.to_alipay_dict()
            else:
                params['muti_floor'] = self.muti_floor
        if self.out_location_point_id:
            if hasattr(self.out_location_point_id, 'to_alipay_dict'):
                params['out_location_point_id'] = self.out_location_point_id.to_alipay_dict()
            else:
                params['out_location_point_id'] = self.out_location_point_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LocationPointInfoVO()
        if 'binding_card_id' in d:
            o.binding_card_id = d['binding_card_id']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'floor_num' in d:
            o.floor_num = d['floor_num']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'location_desc' in d:
            o.location_desc = d['location_desc']
        if 'location_name' in d:
            o.location_name = d['location_name']
        if 'location_point_id' in d:
            o.location_point_id = d['location_point_id']
        if 'location_type' in d:
            o.location_type = d['location_type']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'muti_floor' in d:
            o.muti_floor = d['muti_floor']
        if 'out_location_point_id' in d:
            o.out_location_point_id = d['out_location_point_id']
        return o



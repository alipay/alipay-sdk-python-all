#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePropertyPointSaveModel(object):

    def __init__(self):
        self._action = None
        self._community_id = None
        self._device_ids = None
        self._floor_num = None
        self._job_ids = None
        self._latitude = None
        self._location_desc = None
        self._location_name = None
        self._location_point_id = None
        self._location_type = None
        self._longitude = None
        self._muti_floor = None
        self._out_device_ids = None
        self._out_location_point_id = None
        self._unbind_card = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def device_ids(self):
        return self._device_ids

    @device_ids.setter
    def device_ids(self, value):
        if isinstance(value, list):
            self._device_ids = list()
            for i in value:
                self._device_ids.append(i)
    @property
    def floor_num(self):
        return self._floor_num

    @floor_num.setter
    def floor_num(self, value):
        self._floor_num = value
    @property
    def job_ids(self):
        return self._job_ids

    @job_ids.setter
    def job_ids(self, value):
        if isinstance(value, list):
            self._job_ids = list()
            for i in value:
                self._job_ids.append(i)
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
    def out_device_ids(self):
        return self._out_device_ids

    @out_device_ids.setter
    def out_device_ids(self, value):
        if isinstance(value, list):
            self._out_device_ids = list()
            for i in value:
                self._out_device_ids.append(i)
    @property
    def out_location_point_id(self):
        return self._out_location_point_id

    @out_location_point_id.setter
    def out_location_point_id(self, value):
        self._out_location_point_id = value
    @property
    def unbind_card(self):
        return self._unbind_card

    @unbind_card.setter
    def unbind_card(self, value):
        self._unbind_card = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.device_ids:
            if isinstance(self.device_ids, list):
                for i in range(0, len(self.device_ids)):
                    element = self.device_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_ids[i] = element.to_alipay_dict()
            if hasattr(self.device_ids, 'to_alipay_dict'):
                params['device_ids'] = self.device_ids.to_alipay_dict()
            else:
                params['device_ids'] = self.device_ids
        if self.floor_num:
            if hasattr(self.floor_num, 'to_alipay_dict'):
                params['floor_num'] = self.floor_num.to_alipay_dict()
            else:
                params['floor_num'] = self.floor_num
        if self.job_ids:
            if isinstance(self.job_ids, list):
                for i in range(0, len(self.job_ids)):
                    element = self.job_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.job_ids[i] = element.to_alipay_dict()
            if hasattr(self.job_ids, 'to_alipay_dict'):
                params['job_ids'] = self.job_ids.to_alipay_dict()
            else:
                params['job_ids'] = self.job_ids
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
        if self.out_device_ids:
            if isinstance(self.out_device_ids, list):
                for i in range(0, len(self.out_device_ids)):
                    element = self.out_device_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_device_ids[i] = element.to_alipay_dict()
            if hasattr(self.out_device_ids, 'to_alipay_dict'):
                params['out_device_ids'] = self.out_device_ids.to_alipay_dict()
            else:
                params['out_device_ids'] = self.out_device_ids
        if self.out_location_point_id:
            if hasattr(self.out_location_point_id, 'to_alipay_dict'):
                params['out_location_point_id'] = self.out_location_point_id.to_alipay_dict()
            else:
                params['out_location_point_id'] = self.out_location_point_id
        if self.unbind_card:
            if hasattr(self.unbind_card, 'to_alipay_dict'):
                params['unbind_card'] = self.unbind_card.to_alipay_dict()
            else:
                params['unbind_card'] = self.unbind_card
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePropertyPointSaveModel()
        if 'action' in d:
            o.action = d['action']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'device_ids' in d:
            o.device_ids = d['device_ids']
        if 'floor_num' in d:
            o.floor_num = d['floor_num']
        if 'job_ids' in d:
            o.job_ids = d['job_ids']
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
        if 'out_device_ids' in d:
            o.out_device_ids = d['out_device_ids']
        if 'out_location_point_id' in d:
            o.out_location_point_id = d['out_location_point_id']
        if 'unbind_card' in d:
            o.unbind_card = d['unbind_card']
        return o



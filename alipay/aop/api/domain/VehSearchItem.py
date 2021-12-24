#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VehServiceItem import VehServiceItem


class VehSearchItem(object):

    def __init__(self):
        self._address = None
        self._biz_id = None
        self._biz_scene = None
        self._distance = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._poi_id = None
        self._support_service_list = None
        self._surplus_parking_space = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def support_service_list(self):
        return self._support_service_list

    @support_service_list.setter
    def support_service_list(self, value):
        if isinstance(value, list):
            self._support_service_list = list()
            for i in value:
                if isinstance(i, VehServiceItem):
                    self._support_service_list.append(i)
                else:
                    self._support_service_list.append(VehServiceItem.from_alipay_dict(i))
    @property
    def surplus_parking_space(self):
        return self._surplus_parking_space

    @surplus_parking_space.setter
    def surplus_parking_space(self, value):
        self._surplus_parking_space = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.support_service_list:
            if isinstance(self.support_service_list, list):
                for i in range(0, len(self.support_service_list)):
                    element = self.support_service_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.support_service_list[i] = element.to_alipay_dict()
            if hasattr(self.support_service_list, 'to_alipay_dict'):
                params['support_service_list'] = self.support_service_list.to_alipay_dict()
            else:
                params['support_service_list'] = self.support_service_list
        if self.surplus_parking_space:
            if hasattr(self.surplus_parking_space, 'to_alipay_dict'):
                params['surplus_parking_space'] = self.surplus_parking_space.to_alipay_dict()
            else:
                params['surplus_parking_space'] = self.surplus_parking_space
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehSearchItem()
        if 'address' in d:
            o.address = d['address']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'distance' in d:
            o.distance = d['distance']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'name' in d:
            o.name = d['name']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'support_service_list' in d:
            o.support_service_list = d['support_service_list']
        if 'surplus_parking_space' in d:
            o.surplus_parking_space = d['surplus_parking_space']
        return o



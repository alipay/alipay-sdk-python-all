#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NearMallBo(object):

    def __init__(self):
        self._attribute = None
        self._distance = None
        self._latitude = None
        self._longitude = None
        self._mall_id = None
        self._mall_logo = None
        self._mall_name = None

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value
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
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def mall_logo(self):
        return self._mall_logo

    @mall_logo.setter
    def mall_logo(self, value):
        self._mall_logo = value
    @property
    def mall_name(self):
        return self._mall_name

    @mall_name.setter
    def mall_name(self, value):
        self._mall_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.attribute:
            if hasattr(self.attribute, 'to_alipay_dict'):
                params['attribute'] = self.attribute.to_alipay_dict()
            else:
                params['attribute'] = self.attribute
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
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.mall_logo:
            if hasattr(self.mall_logo, 'to_alipay_dict'):
                params['mall_logo'] = self.mall_logo.to_alipay_dict()
            else:
                params['mall_logo'] = self.mall_logo
        if self.mall_name:
            if hasattr(self.mall_name, 'to_alipay_dict'):
                params['mall_name'] = self.mall_name.to_alipay_dict()
            else:
                params['mall_name'] = self.mall_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NearMallBo()
        if 'attribute' in d:
            o.attribute = d['attribute']
        if 'distance' in d:
            o.distance = d['distance']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'mall_logo' in d:
            o.mall_logo = d['mall_logo']
        if 'mall_name' in d:
            o.mall_name = d['mall_name']
        return o



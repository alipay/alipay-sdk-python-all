#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlantPlace(object):

    def __init__(self):
        self._acreage = None
        self._forest_id = None
        self._forest_name = None
        self._location = None
        self._ngo_name = None
        self._plant_time = None
        self._region = None
        self._tree_count = None

    @property
    def acreage(self):
        return self._acreage

    @acreage.setter
    def acreage(self, value):
        self._acreage = value
    @property
    def forest_id(self):
        return self._forest_id

    @forest_id.setter
    def forest_id(self, value):
        self._forest_id = value
    @property
    def forest_name(self):
        return self._forest_name

    @forest_name.setter
    def forest_name(self, value):
        self._forest_name = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def ngo_name(self):
        return self._ngo_name

    @ngo_name.setter
    def ngo_name(self, value):
        self._ngo_name = value
    @property
    def plant_time(self):
        return self._plant_time

    @plant_time.setter
    def plant_time(self, value):
        self._plant_time = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def tree_count(self):
        return self._tree_count

    @tree_count.setter
    def tree_count(self, value):
        self._tree_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.acreage:
            if hasattr(self.acreage, 'to_alipay_dict'):
                params['acreage'] = self.acreage.to_alipay_dict()
            else:
                params['acreage'] = self.acreage
        if self.forest_id:
            if hasattr(self.forest_id, 'to_alipay_dict'):
                params['forest_id'] = self.forest_id.to_alipay_dict()
            else:
                params['forest_id'] = self.forest_id
        if self.forest_name:
            if hasattr(self.forest_name, 'to_alipay_dict'):
                params['forest_name'] = self.forest_name.to_alipay_dict()
            else:
                params['forest_name'] = self.forest_name
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.ngo_name:
            if hasattr(self.ngo_name, 'to_alipay_dict'):
                params['ngo_name'] = self.ngo_name.to_alipay_dict()
            else:
                params['ngo_name'] = self.ngo_name
        if self.plant_time:
            if hasattr(self.plant_time, 'to_alipay_dict'):
                params['plant_time'] = self.plant_time.to_alipay_dict()
            else:
                params['plant_time'] = self.plant_time
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.tree_count:
            if hasattr(self.tree_count, 'to_alipay_dict'):
                params['tree_count'] = self.tree_count.to_alipay_dict()
            else:
                params['tree_count'] = self.tree_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlantPlace()
        if 'acreage' in d:
            o.acreage = d['acreage']
        if 'forest_id' in d:
            o.forest_id = d['forest_id']
        if 'forest_name' in d:
            o.forest_name = d['forest_name']
        if 'location' in d:
            o.location = d['location']
        if 'ngo_name' in d:
            o.ngo_name = d['ngo_name']
        if 'plant_time' in d:
            o.plant_time = d['plant_time']
        if 'region' in d:
            o.region = d['region']
        if 'tree_count' in d:
            o.tree_count = d['tree_count']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MassifBaseInfo(object):

    def __init__(self):
        self._city = None
        self._county = None
        self._land_area = None
        self._land_name = None
        self._lbs = None
        self._massif_id = None
        self._plant_category = None
        self._plant_crop = None
        self._province = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def county(self):
        return self._county

    @county.setter
    def county(self, value):
        self._county = value
    @property
    def land_area(self):
        return self._land_area

    @land_area.setter
    def land_area(self, value):
        self._land_area = value
    @property
    def land_name(self):
        return self._land_name

    @land_name.setter
    def land_name(self, value):
        self._land_name = value
    @property
    def lbs(self):
        return self._lbs

    @lbs.setter
    def lbs(self, value):
        self._lbs = value
    @property
    def massif_id(self):
        return self._massif_id

    @massif_id.setter
    def massif_id(self, value):
        self._massif_id = value
    @property
    def plant_category(self):
        return self._plant_category

    @plant_category.setter
    def plant_category(self, value):
        self._plant_category = value
    @property
    def plant_crop(self):
        return self._plant_crop

    @plant_crop.setter
    def plant_crop(self, value):
        self._plant_crop = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.county:
            if hasattr(self.county, 'to_alipay_dict'):
                params['county'] = self.county.to_alipay_dict()
            else:
                params['county'] = self.county
        if self.land_area:
            if hasattr(self.land_area, 'to_alipay_dict'):
                params['land_area'] = self.land_area.to_alipay_dict()
            else:
                params['land_area'] = self.land_area
        if self.land_name:
            if hasattr(self.land_name, 'to_alipay_dict'):
                params['land_name'] = self.land_name.to_alipay_dict()
            else:
                params['land_name'] = self.land_name
        if self.lbs:
            if hasattr(self.lbs, 'to_alipay_dict'):
                params['lbs'] = self.lbs.to_alipay_dict()
            else:
                params['lbs'] = self.lbs
        if self.massif_id:
            if hasattr(self.massif_id, 'to_alipay_dict'):
                params['massif_id'] = self.massif_id.to_alipay_dict()
            else:
                params['massif_id'] = self.massif_id
        if self.plant_category:
            if hasattr(self.plant_category, 'to_alipay_dict'):
                params['plant_category'] = self.plant_category.to_alipay_dict()
            else:
                params['plant_category'] = self.plant_category
        if self.plant_crop:
            if hasattr(self.plant_crop, 'to_alipay_dict'):
                params['plant_crop'] = self.plant_crop.to_alipay_dict()
            else:
                params['plant_crop'] = self.plant_crop
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MassifBaseInfo()
        if 'city' in d:
            o.city = d['city']
        if 'county' in d:
            o.county = d['county']
        if 'land_area' in d:
            o.land_area = d['land_area']
        if 'land_name' in d:
            o.land_name = d['land_name']
        if 'lbs' in d:
            o.lbs = d['lbs']
        if 'massif_id' in d:
            o.massif_id = d['massif_id']
        if 'plant_category' in d:
            o.plant_category = d['plant_category']
        if 'plant_crop' in d:
            o.plant_crop = d['plant_crop']
        if 'province' in d:
            o.province = d['province']
        return o



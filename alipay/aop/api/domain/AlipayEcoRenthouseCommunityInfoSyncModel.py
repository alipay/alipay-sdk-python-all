#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseCommunityInfoSyncModel(object):

    def __init__(self):
        self._address = None
        self._city_code = None
        self._city_name = None
        self._community_locations = None
        self._community_name = None
        self._coordsys = None
        self._district_code = None
        self._district_name = None
        self._poi = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def community_locations(self):
        return self._community_locations

    @community_locations.setter
    def community_locations(self, value):
        self._community_locations = value
    @property
    def community_name(self):
        return self._community_name

    @community_name.setter
    def community_name(self, value):
        self._community_name = value
    @property
    def coordsys(self):
        return self._coordsys

    @coordsys.setter
    def coordsys(self, value):
        self._coordsys = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def poi(self):
        return self._poi

    @poi.setter
    def poi(self, value):
        self._poi = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.community_locations:
            if hasattr(self.community_locations, 'to_alipay_dict'):
                params['community_locations'] = self.community_locations.to_alipay_dict()
            else:
                params['community_locations'] = self.community_locations
        if self.community_name:
            if hasattr(self.community_name, 'to_alipay_dict'):
                params['community_name'] = self.community_name.to_alipay_dict()
            else:
                params['community_name'] = self.community_name
        if self.coordsys:
            if hasattr(self.coordsys, 'to_alipay_dict'):
                params['coordsys'] = self.coordsys.to_alipay_dict()
            else:
                params['coordsys'] = self.coordsys
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.poi:
            if hasattr(self.poi, 'to_alipay_dict'):
                params['poi'] = self.poi.to_alipay_dict()
            else:
                params['poi'] = self.poi
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseCommunityInfoSyncModel()
        if 'address' in d:
            o.address = d['address']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'community_locations' in d:
            o.community_locations = d['community_locations']
        if 'community_name' in d:
            o.community_name = d['community_name']
        if 'coordsys' in d:
            o.coordsys = d['coordsys']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'poi' in d:
            o.poi = d['poi']
        return o



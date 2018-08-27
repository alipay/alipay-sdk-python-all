#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCplifeCommunityCreateModel(object):

    def __init__(self):
        self._associated_pois = None
        self._city_code = None
        self._community_address = None
        self._community_locations = None
        self._community_name = None
        self._district_code = None
        self._hotline = None
        self._out_community_id = None
        self._province_code = None

    @property
    def associated_pois(self):
        return self._associated_pois

    @associated_pois.setter
    def associated_pois(self, value):
        if isinstance(value, list):
            self._associated_pois = list()
            for i in value:
                self._associated_pois.append(i)
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def community_address(self):
        return self._community_address

    @community_address.setter
    def community_address(self, value):
        self._community_address = value
    @property
    def community_locations(self):
        return self._community_locations

    @community_locations.setter
    def community_locations(self, value):
        if isinstance(value, list):
            self._community_locations = list()
            for i in value:
                self._community_locations.append(i)
    @property
    def community_name(self):
        return self._community_name

    @community_name.setter
    def community_name(self, value):
        self._community_name = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def hotline(self):
        return self._hotline

    @hotline.setter
    def hotline(self, value):
        self._hotline = value
    @property
    def out_community_id(self):
        return self._out_community_id

    @out_community_id.setter
    def out_community_id(self, value):
        self._out_community_id = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.associated_pois:
            if isinstance(self.associated_pois, list):
                for i in range(0, len(self.associated_pois)):
                    element = self.associated_pois[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.associated_pois[i] = element.to_alipay_dict()
            if hasattr(self.associated_pois, 'to_alipay_dict'):
                params['associated_pois'] = self.associated_pois.to_alipay_dict()
            else:
                params['associated_pois'] = self.associated_pois
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.community_address:
            if hasattr(self.community_address, 'to_alipay_dict'):
                params['community_address'] = self.community_address.to_alipay_dict()
            else:
                params['community_address'] = self.community_address
        if self.community_locations:
            if isinstance(self.community_locations, list):
                for i in range(0, len(self.community_locations)):
                    element = self.community_locations[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.community_locations[i] = element.to_alipay_dict()
            if hasattr(self.community_locations, 'to_alipay_dict'):
                params['community_locations'] = self.community_locations.to_alipay_dict()
            else:
                params['community_locations'] = self.community_locations
        if self.community_name:
            if hasattr(self.community_name, 'to_alipay_dict'):
                params['community_name'] = self.community_name.to_alipay_dict()
            else:
                params['community_name'] = self.community_name
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.hotline:
            if hasattr(self.hotline, 'to_alipay_dict'):
                params['hotline'] = self.hotline.to_alipay_dict()
            else:
                params['hotline'] = self.hotline
        if self.out_community_id:
            if hasattr(self.out_community_id, 'to_alipay_dict'):
                params['out_community_id'] = self.out_community_id.to_alipay_dict()
            else:
                params['out_community_id'] = self.out_community_id
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifeCommunityCreateModel()
        if 'associated_pois' in d:
            o.associated_pois = d['associated_pois']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'community_address' in d:
            o.community_address = d['community_address']
        if 'community_locations' in d:
            o.community_locations = d['community_locations']
        if 'community_name' in d:
            o.community_name = d['community_name']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'hotline' in d:
            o.hotline = d['hotline']
        if 'out_community_id' in d:
            o.out_community_id = d['out_community_id']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o



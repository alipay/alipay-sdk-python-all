#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommunityPropertyCompany import CommunityPropertyCompany
from alipay.aop.api.domain.CommunityService import CommunityService


class AlipayEbppCommunityThirdpartycommunityCreateModel(object):

    def __init__(self):
        self._address = None
        self._address_memo = None
        self._alias = None
        self._city = None
        self._community_adcode = None
        self._community_adcode_name = None
        self._community_property_company = None
        self._community_service = None
        self._county = None
        self._county_name = None
        self._hot_line = None
        self._hot_line_end = None
        self._hot_line_start = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._out_community_id = None
        self._province = None
        self._street_adcode = None
        self._street_adcode_name = None
        self._support_type = None
        self._verify_type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_memo(self):
        return self._address_memo

    @address_memo.setter
    def address_memo(self, value):
        self._address_memo = value
    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def community_adcode(self):
        return self._community_adcode

    @community_adcode.setter
    def community_adcode(self, value):
        self._community_adcode = value
    @property
    def community_adcode_name(self):
        return self._community_adcode_name

    @community_adcode_name.setter
    def community_adcode_name(self, value):
        self._community_adcode_name = value
    @property
    def community_property_company(self):
        return self._community_property_company

    @community_property_company.setter
    def community_property_company(self, value):
        if isinstance(value, CommunityPropertyCompany):
            self._community_property_company = value
        else:
            self._community_property_company = CommunityPropertyCompany.from_alipay_dict(value)
    @property
    def community_service(self):
        return self._community_service

    @community_service.setter
    def community_service(self, value):
        if isinstance(value, list):
            self._community_service = list()
            for i in value:
                if isinstance(i, CommunityService):
                    self._community_service.append(i)
                else:
                    self._community_service.append(CommunityService.from_alipay_dict(i))
    @property
    def county(self):
        return self._county

    @county.setter
    def county(self, value):
        self._county = value
    @property
    def county_name(self):
        return self._county_name

    @county_name.setter
    def county_name(self, value):
        self._county_name = value
    @property
    def hot_line(self):
        return self._hot_line

    @hot_line.setter
    def hot_line(self, value):
        self._hot_line = value
    @property
    def hot_line_end(self):
        return self._hot_line_end

    @hot_line_end.setter
    def hot_line_end(self, value):
        self._hot_line_end = value
    @property
    def hot_line_start(self):
        return self._hot_line_start

    @hot_line_start.setter
    def hot_line_start(self, value):
        self._hot_line_start = value
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
    def out_community_id(self):
        return self._out_community_id

    @out_community_id.setter
    def out_community_id(self, value):
        self._out_community_id = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def street_adcode(self):
        return self._street_adcode

    @street_adcode.setter
    def street_adcode(self, value):
        self._street_adcode = value
    @property
    def street_adcode_name(self):
        return self._street_adcode_name

    @street_adcode_name.setter
    def street_adcode_name(self, value):
        self._street_adcode_name = value
    @property
    def support_type(self):
        return self._support_type

    @support_type.setter
    def support_type(self, value):
        self._support_type = value
    @property
    def verify_type(self):
        return self._verify_type

    @verify_type.setter
    def verify_type(self, value):
        self._verify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.address_memo:
            if hasattr(self.address_memo, 'to_alipay_dict'):
                params['address_memo'] = self.address_memo.to_alipay_dict()
            else:
                params['address_memo'] = self.address_memo
        if self.alias:
            if hasattr(self.alias, 'to_alipay_dict'):
                params['alias'] = self.alias.to_alipay_dict()
            else:
                params['alias'] = self.alias
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.community_adcode:
            if hasattr(self.community_adcode, 'to_alipay_dict'):
                params['community_adcode'] = self.community_adcode.to_alipay_dict()
            else:
                params['community_adcode'] = self.community_adcode
        if self.community_adcode_name:
            if hasattr(self.community_adcode_name, 'to_alipay_dict'):
                params['community_adcode_name'] = self.community_adcode_name.to_alipay_dict()
            else:
                params['community_adcode_name'] = self.community_adcode_name
        if self.community_property_company:
            if hasattr(self.community_property_company, 'to_alipay_dict'):
                params['community_property_company'] = self.community_property_company.to_alipay_dict()
            else:
                params['community_property_company'] = self.community_property_company
        if self.community_service:
            if isinstance(self.community_service, list):
                for i in range(0, len(self.community_service)):
                    element = self.community_service[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.community_service[i] = element.to_alipay_dict()
            if hasattr(self.community_service, 'to_alipay_dict'):
                params['community_service'] = self.community_service.to_alipay_dict()
            else:
                params['community_service'] = self.community_service
        if self.county:
            if hasattr(self.county, 'to_alipay_dict'):
                params['county'] = self.county.to_alipay_dict()
            else:
                params['county'] = self.county
        if self.county_name:
            if hasattr(self.county_name, 'to_alipay_dict'):
                params['county_name'] = self.county_name.to_alipay_dict()
            else:
                params['county_name'] = self.county_name
        if self.hot_line:
            if hasattr(self.hot_line, 'to_alipay_dict'):
                params['hot_line'] = self.hot_line.to_alipay_dict()
            else:
                params['hot_line'] = self.hot_line
        if self.hot_line_end:
            if hasattr(self.hot_line_end, 'to_alipay_dict'):
                params['hot_line_end'] = self.hot_line_end.to_alipay_dict()
            else:
                params['hot_line_end'] = self.hot_line_end
        if self.hot_line_start:
            if hasattr(self.hot_line_start, 'to_alipay_dict'):
                params['hot_line_start'] = self.hot_line_start.to_alipay_dict()
            else:
                params['hot_line_start'] = self.hot_line_start
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
        if self.out_community_id:
            if hasattr(self.out_community_id, 'to_alipay_dict'):
                params['out_community_id'] = self.out_community_id.to_alipay_dict()
            else:
                params['out_community_id'] = self.out_community_id
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.street_adcode:
            if hasattr(self.street_adcode, 'to_alipay_dict'):
                params['street_adcode'] = self.street_adcode.to_alipay_dict()
            else:
                params['street_adcode'] = self.street_adcode
        if self.street_adcode_name:
            if hasattr(self.street_adcode_name, 'to_alipay_dict'):
                params['street_adcode_name'] = self.street_adcode_name.to_alipay_dict()
            else:
                params['street_adcode_name'] = self.street_adcode_name
        if self.support_type:
            if hasattr(self.support_type, 'to_alipay_dict'):
                params['support_type'] = self.support_type.to_alipay_dict()
            else:
                params['support_type'] = self.support_type
        if self.verify_type:
            if hasattr(self.verify_type, 'to_alipay_dict'):
                params['verify_type'] = self.verify_type.to_alipay_dict()
            else:
                params['verify_type'] = self.verify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityThirdpartycommunityCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'address_memo' in d:
            o.address_memo = d['address_memo']
        if 'alias' in d:
            o.alias = d['alias']
        if 'city' in d:
            o.city = d['city']
        if 'community_adcode' in d:
            o.community_adcode = d['community_adcode']
        if 'community_adcode_name' in d:
            o.community_adcode_name = d['community_adcode_name']
        if 'community_property_company' in d:
            o.community_property_company = d['community_property_company']
        if 'community_service' in d:
            o.community_service = d['community_service']
        if 'county' in d:
            o.county = d['county']
        if 'county_name' in d:
            o.county_name = d['county_name']
        if 'hot_line' in d:
            o.hot_line = d['hot_line']
        if 'hot_line_end' in d:
            o.hot_line_end = d['hot_line_end']
        if 'hot_line_start' in d:
            o.hot_line_start = d['hot_line_start']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'name' in d:
            o.name = d['name']
        if 'out_community_id' in d:
            o.out_community_id = d['out_community_id']
        if 'province' in d:
            o.province = d['province']
        if 'street_adcode' in d:
            o.street_adcode = d['street_adcode']
        if 'street_adcode_name' in d:
            o.street_adcode_name = d['street_adcode_name']
        if 'support_type' in d:
            o.support_type = d['support_type']
        if 'verify_type' in d:
            o.verify_type = d['verify_type']
        return o



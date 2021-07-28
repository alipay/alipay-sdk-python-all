#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExternalPoiInfo import ExternalPoiInfo


class AlipayEbppCommunityCommunityinfoCreateModel(object):

    def __init__(self):
        self._alias = None
        self._city = None
        self._community_adcode = None
        self._community_adcode_name = None
        self._community_short_name = None
        self._county = None
        self._county_name = None
        self._hot_line = None
        self._hot_line_end = None
        self._hot_line_start = None
        self._name = None
        self._out_community_id = None
        self._pois = None
        self._province = None
        self._street_adcode = None
        self._street_adcode_name = None
        self._support_type = None
        self._verify_type = None

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
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
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
    def pois(self):
        return self._pois

    @pois.setter
    def pois(self, value):
        if isinstance(value, list):
            self._pois = list()
            for i in value:
                if isinstance(i, ExternalPoiInfo):
                    self._pois.append(i)
                else:
                    self._pois.append(ExternalPoiInfo.from_alipay_dict(i))
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
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
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
        if self.pois:
            if isinstance(self.pois, list):
                for i in range(0, len(self.pois)):
                    element = self.pois[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pois[i] = element.to_alipay_dict()
            if hasattr(self.pois, 'to_alipay_dict'):
                params['pois'] = self.pois.to_alipay_dict()
            else:
                params['pois'] = self.pois
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
        o = AlipayEbppCommunityCommunityinfoCreateModel()
        if 'alias' in d:
            o.alias = d['alias']
        if 'city' in d:
            o.city = d['city']
        if 'community_adcode' in d:
            o.community_adcode = d['community_adcode']
        if 'community_adcode_name' in d:
            o.community_adcode_name = d['community_adcode_name']
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
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
        if 'name' in d:
            o.name = d['name']
        if 'out_community_id' in d:
            o.out_community_id = d['out_community_id']
        if 'pois' in d:
            o.pois = d['pois']
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



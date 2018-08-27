#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseCommunityBaseinfoSyncModel(object):

    def __init__(self):
        self._bus_code = None
        self._bus_lat = None
        self._bus_lng = None
        self._bus_name = None
        self._bus_radius = None
        self._city_code = None
        self._city_lat = None
        self._city_lng = None
        self._city_name = None
        self._community_code = None
        self._community_lat = None
        self._community_lng = None
        self._community_name = None
        self._community_nong = None
        self._community_street = None
        self._community_tag = None
        self._district_code = None
        self._district_lat = None
        self._district_lng = None
        self._district_name = None
        self._subway_stations = None

    @property
    def bus_code(self):
        return self._bus_code

    @bus_code.setter
    def bus_code(self, value):
        self._bus_code = value
    @property
    def bus_lat(self):
        return self._bus_lat

    @bus_lat.setter
    def bus_lat(self, value):
        self._bus_lat = value
    @property
    def bus_lng(self):
        return self._bus_lng

    @bus_lng.setter
    def bus_lng(self, value):
        self._bus_lng = value
    @property
    def bus_name(self):
        return self._bus_name

    @bus_name.setter
    def bus_name(self, value):
        self._bus_name = value
    @property
    def bus_radius(self):
        return self._bus_radius

    @bus_radius.setter
    def bus_radius(self, value):
        self._bus_radius = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_lat(self):
        return self._city_lat

    @city_lat.setter
    def city_lat(self, value):
        self._city_lat = value
    @property
    def city_lng(self):
        return self._city_lng

    @city_lng.setter
    def city_lng(self, value):
        self._city_lng = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def community_code(self):
        return self._community_code

    @community_code.setter
    def community_code(self, value):
        self._community_code = value
    @property
    def community_lat(self):
        return self._community_lat

    @community_lat.setter
    def community_lat(self, value):
        self._community_lat = value
    @property
    def community_lng(self):
        return self._community_lng

    @community_lng.setter
    def community_lng(self, value):
        self._community_lng = value
    @property
    def community_name(self):
        return self._community_name

    @community_name.setter
    def community_name(self, value):
        self._community_name = value
    @property
    def community_nong(self):
        return self._community_nong

    @community_nong.setter
    def community_nong(self, value):
        self._community_nong = value
    @property
    def community_street(self):
        return self._community_street

    @community_street.setter
    def community_street(self, value):
        self._community_street = value
    @property
    def community_tag(self):
        return self._community_tag

    @community_tag.setter
    def community_tag(self, value):
        self._community_tag = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_lat(self):
        return self._district_lat

    @district_lat.setter
    def district_lat(self, value):
        self._district_lat = value
    @property
    def district_lng(self):
        return self._district_lng

    @district_lng.setter
    def district_lng(self, value):
        self._district_lng = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def subway_stations(self):
        return self._subway_stations

    @subway_stations.setter
    def subway_stations(self, value):
        if isinstance(value, list):
            self._subway_stations = list()
            for i in value:
                self._subway_stations.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.bus_code:
            if hasattr(self.bus_code, 'to_alipay_dict'):
                params['bus_code'] = self.bus_code.to_alipay_dict()
            else:
                params['bus_code'] = self.bus_code
        if self.bus_lat:
            if hasattr(self.bus_lat, 'to_alipay_dict'):
                params['bus_lat'] = self.bus_lat.to_alipay_dict()
            else:
                params['bus_lat'] = self.bus_lat
        if self.bus_lng:
            if hasattr(self.bus_lng, 'to_alipay_dict'):
                params['bus_lng'] = self.bus_lng.to_alipay_dict()
            else:
                params['bus_lng'] = self.bus_lng
        if self.bus_name:
            if hasattr(self.bus_name, 'to_alipay_dict'):
                params['bus_name'] = self.bus_name.to_alipay_dict()
            else:
                params['bus_name'] = self.bus_name
        if self.bus_radius:
            if hasattr(self.bus_radius, 'to_alipay_dict'):
                params['bus_radius'] = self.bus_radius.to_alipay_dict()
            else:
                params['bus_radius'] = self.bus_radius
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_lat:
            if hasattr(self.city_lat, 'to_alipay_dict'):
                params['city_lat'] = self.city_lat.to_alipay_dict()
            else:
                params['city_lat'] = self.city_lat
        if self.city_lng:
            if hasattr(self.city_lng, 'to_alipay_dict'):
                params['city_lng'] = self.city_lng.to_alipay_dict()
            else:
                params['city_lng'] = self.city_lng
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.community_code:
            if hasattr(self.community_code, 'to_alipay_dict'):
                params['community_code'] = self.community_code.to_alipay_dict()
            else:
                params['community_code'] = self.community_code
        if self.community_lat:
            if hasattr(self.community_lat, 'to_alipay_dict'):
                params['community_lat'] = self.community_lat.to_alipay_dict()
            else:
                params['community_lat'] = self.community_lat
        if self.community_lng:
            if hasattr(self.community_lng, 'to_alipay_dict'):
                params['community_lng'] = self.community_lng.to_alipay_dict()
            else:
                params['community_lng'] = self.community_lng
        if self.community_name:
            if hasattr(self.community_name, 'to_alipay_dict'):
                params['community_name'] = self.community_name.to_alipay_dict()
            else:
                params['community_name'] = self.community_name
        if self.community_nong:
            if hasattr(self.community_nong, 'to_alipay_dict'):
                params['community_nong'] = self.community_nong.to_alipay_dict()
            else:
                params['community_nong'] = self.community_nong
        if self.community_street:
            if hasattr(self.community_street, 'to_alipay_dict'):
                params['community_street'] = self.community_street.to_alipay_dict()
            else:
                params['community_street'] = self.community_street
        if self.community_tag:
            if hasattr(self.community_tag, 'to_alipay_dict'):
                params['community_tag'] = self.community_tag.to_alipay_dict()
            else:
                params['community_tag'] = self.community_tag
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.district_lat:
            if hasattr(self.district_lat, 'to_alipay_dict'):
                params['district_lat'] = self.district_lat.to_alipay_dict()
            else:
                params['district_lat'] = self.district_lat
        if self.district_lng:
            if hasattr(self.district_lng, 'to_alipay_dict'):
                params['district_lng'] = self.district_lng.to_alipay_dict()
            else:
                params['district_lng'] = self.district_lng
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.subway_stations:
            if isinstance(self.subway_stations, list):
                for i in range(0, len(self.subway_stations)):
                    element = self.subway_stations[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subway_stations[i] = element.to_alipay_dict()
            if hasattr(self.subway_stations, 'to_alipay_dict'):
                params['subway_stations'] = self.subway_stations.to_alipay_dict()
            else:
                params['subway_stations'] = self.subway_stations
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseCommunityBaseinfoSyncModel()
        if 'bus_code' in d:
            o.bus_code = d['bus_code']
        if 'bus_lat' in d:
            o.bus_lat = d['bus_lat']
        if 'bus_lng' in d:
            o.bus_lng = d['bus_lng']
        if 'bus_name' in d:
            o.bus_name = d['bus_name']
        if 'bus_radius' in d:
            o.bus_radius = d['bus_radius']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_lat' in d:
            o.city_lat = d['city_lat']
        if 'city_lng' in d:
            o.city_lng = d['city_lng']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'community_code' in d:
            o.community_code = d['community_code']
        if 'community_lat' in d:
            o.community_lat = d['community_lat']
        if 'community_lng' in d:
            o.community_lng = d['community_lng']
        if 'community_name' in d:
            o.community_name = d['community_name']
        if 'community_nong' in d:
            o.community_nong = d['community_nong']
        if 'community_street' in d:
            o.community_street = d['community_street']
        if 'community_tag' in d:
            o.community_tag = d['community_tag']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_lat' in d:
            o.district_lat = d['district_lat']
        if 'district_lng' in d:
            o.district_lng = d['district_lng']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'subway_stations' in d:
            o.subway_stations = d['subway_stations']
        return o



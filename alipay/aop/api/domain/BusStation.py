#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusStation(object):

    def __init__(self):
        self._address = None
        self._city_id = None
        self._city_name = None
        self._county_id = None
        self._county_name = None
        self._gaode_poiid = None
        self._lat = None
        self._lng = None
        self._name = None
        self._station_id = None
        self._station_type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def county_id(self):
        return self._county_id

    @county_id.setter
    def county_id(self, value):
        self._county_id = value
    @property
    def county_name(self):
        return self._county_name

    @county_name.setter
    def county_name(self, value):
        self._county_name = value
    @property
    def gaode_poiid(self):
        return self._gaode_poiid

    @gaode_poiid.setter
    def gaode_poiid(self, value):
        self._gaode_poiid = value
    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value
    @property
    def lng(self):
        return self._lng

    @lng.setter
    def lng(self, value):
        self._lng = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        self._station_id = value
    @property
    def station_type(self):
        return self._station_type

    @station_type.setter
    def station_type(self, value):
        self._station_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.county_id:
            if hasattr(self.county_id, 'to_alipay_dict'):
                params['county_id'] = self.county_id.to_alipay_dict()
            else:
                params['county_id'] = self.county_id
        if self.county_name:
            if hasattr(self.county_name, 'to_alipay_dict'):
                params['county_name'] = self.county_name.to_alipay_dict()
            else:
                params['county_name'] = self.county_name
        if self.gaode_poiid:
            if hasattr(self.gaode_poiid, 'to_alipay_dict'):
                params['gaode_poiid'] = self.gaode_poiid.to_alipay_dict()
            else:
                params['gaode_poiid'] = self.gaode_poiid
        if self.lat:
            if hasattr(self.lat, 'to_alipay_dict'):
                params['lat'] = self.lat.to_alipay_dict()
            else:
                params['lat'] = self.lat
        if self.lng:
            if hasattr(self.lng, 'to_alipay_dict'):
                params['lng'] = self.lng.to_alipay_dict()
            else:
                params['lng'] = self.lng
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.station_id:
            if hasattr(self.station_id, 'to_alipay_dict'):
                params['station_id'] = self.station_id.to_alipay_dict()
            else:
                params['station_id'] = self.station_id
        if self.station_type:
            if hasattr(self.station_type, 'to_alipay_dict'):
                params['station_type'] = self.station_type.to_alipay_dict()
            else:
                params['station_type'] = self.station_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusStation()
        if 'address' in d:
            o.address = d['address']
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'county_id' in d:
            o.county_id = d['county_id']
        if 'county_name' in d:
            o.county_name = d['county_name']
        if 'gaode_poiid' in d:
            o.gaode_poiid = d['gaode_poiid']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lng' in d:
            o.lng = d['lng']
        if 'name' in d:
            o.name = d['name']
        if 'station_id' in d:
            o.station_id = d['station_id']
        if 'station_type' in d:
            o.station_type = d['station_type']
        return o



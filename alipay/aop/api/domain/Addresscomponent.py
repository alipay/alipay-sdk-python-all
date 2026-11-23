#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Building import Building
from alipay.aop.api.domain.Businessarea import Businessarea
from alipay.aop.api.domain.Neighborhood import Neighborhood
from alipay.aop.api.domain.Streetnumber import Streetnumber


class Addresscomponent(object):

    def __init__(self):
        self._adcode = None
        self._building = None
        self._business_areas = None
        self._city = None
        self._citycode = None
        self._country = None
        self._district = None
        self._neighborhood = None
        self._province = None
        self._street_number = None
        self._towncode = None
        self._township = None

    @property
    def adcode(self):
        return self._adcode

    @adcode.setter
    def adcode(self, value):
        self._adcode = value
    @property
    def building(self):
        return self._building

    @building.setter
    def building(self, value):
        if isinstance(value, Building):
            self._building = value
        else:
            self._building = Building.from_alipay_dict(value)
    @property
    def business_areas(self):
        return self._business_areas

    @business_areas.setter
    def business_areas(self, value):
        if isinstance(value, list):
            self._business_areas = list()
            for i in value:
                if isinstance(i, Businessarea):
                    self._business_areas.append(i)
                else:
                    self._business_areas.append(Businessarea.from_alipay_dict(i))
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def citycode(self):
        return self._citycode

    @citycode.setter
    def citycode(self, value):
        self._citycode = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def neighborhood(self):
        return self._neighborhood

    @neighborhood.setter
    def neighborhood(self, value):
        if isinstance(value, Neighborhood):
            self._neighborhood = value
        else:
            self._neighborhood = Neighborhood.from_alipay_dict(value)
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def street_number(self):
        return self._street_number

    @street_number.setter
    def street_number(self, value):
        if isinstance(value, Streetnumber):
            self._street_number = value
        else:
            self._street_number = Streetnumber.from_alipay_dict(value)
    @property
    def towncode(self):
        return self._towncode

    @towncode.setter
    def towncode(self, value):
        self._towncode = value
    @property
    def township(self):
        return self._township

    @township.setter
    def township(self, value):
        self._township = value


    def to_alipay_dict(self):
        params = dict()
        if self.adcode:
            if hasattr(self.adcode, 'to_alipay_dict'):
                params['adcode'] = self.adcode.to_alipay_dict()
            else:
                params['adcode'] = self.adcode
        if self.building:
            if hasattr(self.building, 'to_alipay_dict'):
                params['building'] = self.building.to_alipay_dict()
            else:
                params['building'] = self.building
        if self.business_areas:
            if isinstance(self.business_areas, list):
                for i in range(0, len(self.business_areas)):
                    element = self.business_areas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_areas[i] = element.to_alipay_dict()
            if hasattr(self.business_areas, 'to_alipay_dict'):
                params['business_areas'] = self.business_areas.to_alipay_dict()
            else:
                params['business_areas'] = self.business_areas
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.citycode:
            if hasattr(self.citycode, 'to_alipay_dict'):
                params['citycode'] = self.citycode.to_alipay_dict()
            else:
                params['citycode'] = self.citycode
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.neighborhood:
            if hasattr(self.neighborhood, 'to_alipay_dict'):
                params['neighborhood'] = self.neighborhood.to_alipay_dict()
            else:
                params['neighborhood'] = self.neighborhood
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.street_number:
            if hasattr(self.street_number, 'to_alipay_dict'):
                params['street_number'] = self.street_number.to_alipay_dict()
            else:
                params['street_number'] = self.street_number
        if self.towncode:
            if hasattr(self.towncode, 'to_alipay_dict'):
                params['towncode'] = self.towncode.to_alipay_dict()
            else:
                params['towncode'] = self.towncode
        if self.township:
            if hasattr(self.township, 'to_alipay_dict'):
                params['township'] = self.township.to_alipay_dict()
            else:
                params['township'] = self.township
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Addresscomponent()
        if 'adcode' in d:
            o.adcode = d['adcode']
        if 'building' in d:
            o.building = d['building']
        if 'business_areas' in d:
            o.business_areas = d['business_areas']
        if 'city' in d:
            o.city = d['city']
        if 'citycode' in d:
            o.citycode = d['citycode']
        if 'country' in d:
            o.country = d['country']
        if 'district' in d:
            o.district = d['district']
        if 'neighborhood' in d:
            o.neighborhood = d['neighborhood']
        if 'province' in d:
            o.province = d['province']
        if 'street_number' in d:
            o.street_number = d['street_number']
        if 'towncode' in d:
            o.towncode = d['towncode']
        if 'township' in d:
            o.township = d['township']
        return o



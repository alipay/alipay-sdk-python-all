#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EntityBasicInfo(object):

    def __init__(self):
        self._address_desc = None
        self._category_code = None
        self._city = None
        self._contact_number = None
        self._entity_code = None
        self._entity_name = None
        self._latitude = None
        self._longitude = None
        self._office_hours_desc = None
        self._open_day = None
        self._province = None
        self._rent_free_time = None
        self._rent_max_price = None
        self._rent_price = None
        self._rent_price_unit = None
        self._rent_price_unit_cnt = None
        self._suburb = None

    @property
    def address_desc(self):
        return self._address_desc

    @address_desc.setter
    def address_desc(self, value):
        self._address_desc = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value
    @property
    def entity_code(self):
        return self._entity_code

    @entity_code.setter
    def entity_code(self, value):
        self._entity_code = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
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
    def office_hours_desc(self):
        return self._office_hours_desc

    @office_hours_desc.setter
    def office_hours_desc(self, value):
        self._office_hours_desc = value
    @property
    def open_day(self):
        return self._open_day

    @open_day.setter
    def open_day(self, value):
        if isinstance(value, list):
            self._open_day = list()
            for i in value:
                self._open_day.append(i)
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def rent_free_time(self):
        return self._rent_free_time

    @rent_free_time.setter
    def rent_free_time(self, value):
        self._rent_free_time = value
    @property
    def rent_max_price(self):
        return self._rent_max_price

    @rent_max_price.setter
    def rent_max_price(self, value):
        self._rent_max_price = value
    @property
    def rent_price(self):
        return self._rent_price

    @rent_price.setter
    def rent_price(self, value):
        self._rent_price = value
    @property
    def rent_price_unit(self):
        return self._rent_price_unit

    @rent_price_unit.setter
    def rent_price_unit(self, value):
        self._rent_price_unit = value
    @property
    def rent_price_unit_cnt(self):
        return self._rent_price_unit_cnt

    @rent_price_unit_cnt.setter
    def rent_price_unit_cnt(self, value):
        self._rent_price_unit_cnt = value
    @property
    def suburb(self):
        return self._suburb

    @suburb.setter
    def suburb(self, value):
        self._suburb = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_desc:
            if hasattr(self.address_desc, 'to_alipay_dict'):
                params['address_desc'] = self.address_desc.to_alipay_dict()
            else:
                params['address_desc'] = self.address_desc
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.contact_number:
            if hasattr(self.contact_number, 'to_alipay_dict'):
                params['contact_number'] = self.contact_number.to_alipay_dict()
            else:
                params['contact_number'] = self.contact_number
        if self.entity_code:
            if hasattr(self.entity_code, 'to_alipay_dict'):
                params['entity_code'] = self.entity_code.to_alipay_dict()
            else:
                params['entity_code'] = self.entity_code
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
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
        if self.office_hours_desc:
            if hasattr(self.office_hours_desc, 'to_alipay_dict'):
                params['office_hours_desc'] = self.office_hours_desc.to_alipay_dict()
            else:
                params['office_hours_desc'] = self.office_hours_desc
        if self.open_day:
            if isinstance(self.open_day, list):
                for i in range(0, len(self.open_day)):
                    element = self.open_day[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_day[i] = element.to_alipay_dict()
            if hasattr(self.open_day, 'to_alipay_dict'):
                params['open_day'] = self.open_day.to_alipay_dict()
            else:
                params['open_day'] = self.open_day
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.rent_free_time:
            if hasattr(self.rent_free_time, 'to_alipay_dict'):
                params['rent_free_time'] = self.rent_free_time.to_alipay_dict()
            else:
                params['rent_free_time'] = self.rent_free_time
        if self.rent_max_price:
            if hasattr(self.rent_max_price, 'to_alipay_dict'):
                params['rent_max_price'] = self.rent_max_price.to_alipay_dict()
            else:
                params['rent_max_price'] = self.rent_max_price
        if self.rent_price:
            if hasattr(self.rent_price, 'to_alipay_dict'):
                params['rent_price'] = self.rent_price.to_alipay_dict()
            else:
                params['rent_price'] = self.rent_price
        if self.rent_price_unit:
            if hasattr(self.rent_price_unit, 'to_alipay_dict'):
                params['rent_price_unit'] = self.rent_price_unit.to_alipay_dict()
            else:
                params['rent_price_unit'] = self.rent_price_unit
        if self.rent_price_unit_cnt:
            if hasattr(self.rent_price_unit_cnt, 'to_alipay_dict'):
                params['rent_price_unit_cnt'] = self.rent_price_unit_cnt.to_alipay_dict()
            else:
                params['rent_price_unit_cnt'] = self.rent_price_unit_cnt
        if self.suburb:
            if hasattr(self.suburb, 'to_alipay_dict'):
                params['suburb'] = self.suburb.to_alipay_dict()
            else:
                params['suburb'] = self.suburb
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EntityBasicInfo()
        if 'address_desc' in d:
            o.address_desc = d['address_desc']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'city' in d:
            o.city = d['city']
        if 'contact_number' in d:
            o.contact_number = d['contact_number']
        if 'entity_code' in d:
            o.entity_code = d['entity_code']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'office_hours_desc' in d:
            o.office_hours_desc = d['office_hours_desc']
        if 'open_day' in d:
            o.open_day = d['open_day']
        if 'province' in d:
            o.province = d['province']
        if 'rent_free_time' in d:
            o.rent_free_time = d['rent_free_time']
        if 'rent_max_price' in d:
            o.rent_max_price = d['rent_max_price']
        if 'rent_price' in d:
            o.rent_price = d['rent_price']
        if 'rent_price_unit' in d:
            o.rent_price_unit = d['rent_price_unit']
        if 'rent_price_unit_cnt' in d:
            o.rent_price_unit_cnt = d['rent_price_unit_cnt']
        if 'suburb' in d:
            o.suburb = d['suburb']
        return o



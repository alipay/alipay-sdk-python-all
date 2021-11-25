#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubVenueCreateInfo import SubVenueCreateInfo


class AlipayCommerceSportsVenueCreateModel(object):

    def __init__(self):
        self._address = None
        self._area_code = None
        self._bookable = None
        self._city_code = None
        self._desc = None
        self._extra_service_url = None
        self._join_type = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._opening_hours = None
        self._out_venue_id = None
        self._phone = None
        self._picture_list = None
        self._poi = None
        self._poster = None
        self._product_type_list = None
        self._province_code = None
        self._sub_venue_list = None
        self._tag_list = None
        self._test_venue = None
        self._traffic = None
        self._venue_pid = None
        self._venue_type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def bookable(self):
        return self._bookable

    @bookable.setter
    def bookable(self, value):
        self._bookable = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def extra_service_url(self):
        return self._extra_service_url

    @extra_service_url.setter
    def extra_service_url(self, value):
        self._extra_service_url = value
    @property
    def join_type(self):
        return self._join_type

    @join_type.setter
    def join_type(self, value):
        self._join_type = value
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
    def opening_hours(self):
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, value):
        self._opening_hours = value
    @property
    def out_venue_id(self):
        return self._out_venue_id

    @out_venue_id.setter
    def out_venue_id(self, value):
        self._out_venue_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if isinstance(value, list):
            self._phone = list()
            for i in value:
                self._phone.append(i)
    @property
    def picture_list(self):
        return self._picture_list

    @picture_list.setter
    def picture_list(self, value):
        if isinstance(value, list):
            self._picture_list = list()
            for i in value:
                self._picture_list.append(i)
    @property
    def poi(self):
        return self._poi

    @poi.setter
    def poi(self, value):
        self._poi = value
    @property
    def poster(self):
        return self._poster

    @poster.setter
    def poster(self, value):
        self._poster = value
    @property
    def product_type_list(self):
        return self._product_type_list

    @product_type_list.setter
    def product_type_list(self, value):
        if isinstance(value, list):
            self._product_type_list = list()
            for i in value:
                self._product_type_list.append(i)
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def sub_venue_list(self):
        return self._sub_venue_list

    @sub_venue_list.setter
    def sub_venue_list(self, value):
        if isinstance(value, list):
            self._sub_venue_list = list()
            for i in value:
                if isinstance(i, SubVenueCreateInfo):
                    self._sub_venue_list.append(i)
                else:
                    self._sub_venue_list.append(SubVenueCreateInfo.from_alipay_dict(i))
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                self._tag_list.append(i)
    @property
    def test_venue(self):
        return self._test_venue

    @test_venue.setter
    def test_venue(self, value):
        self._test_venue = value
    @property
    def traffic(self):
        return self._traffic

    @traffic.setter
    def traffic(self, value):
        self._traffic = value
    @property
    def venue_pid(self):
        return self._venue_pid

    @venue_pid.setter
    def venue_pid(self, value):
        self._venue_pid = value
    @property
    def venue_type(self):
        return self._venue_type

    @venue_type.setter
    def venue_type(self, value):
        if isinstance(value, list):
            self._venue_type = list()
            for i in value:
                self._venue_type.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.bookable:
            if hasattr(self.bookable, 'to_alipay_dict'):
                params['bookable'] = self.bookable.to_alipay_dict()
            else:
                params['bookable'] = self.bookable
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.extra_service_url:
            if hasattr(self.extra_service_url, 'to_alipay_dict'):
                params['extra_service_url'] = self.extra_service_url.to_alipay_dict()
            else:
                params['extra_service_url'] = self.extra_service_url
        if self.join_type:
            if hasattr(self.join_type, 'to_alipay_dict'):
                params['join_type'] = self.join_type.to_alipay_dict()
            else:
                params['join_type'] = self.join_type
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
        if self.opening_hours:
            if hasattr(self.opening_hours, 'to_alipay_dict'):
                params['opening_hours'] = self.opening_hours.to_alipay_dict()
            else:
                params['opening_hours'] = self.opening_hours
        if self.out_venue_id:
            if hasattr(self.out_venue_id, 'to_alipay_dict'):
                params['out_venue_id'] = self.out_venue_id.to_alipay_dict()
            else:
                params['out_venue_id'] = self.out_venue_id
        if self.phone:
            if isinstance(self.phone, list):
                for i in range(0, len(self.phone)):
                    element = self.phone[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.phone[i] = element.to_alipay_dict()
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.picture_list:
            if isinstance(self.picture_list, list):
                for i in range(0, len(self.picture_list)):
                    element = self.picture_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.picture_list[i] = element.to_alipay_dict()
            if hasattr(self.picture_list, 'to_alipay_dict'):
                params['picture_list'] = self.picture_list.to_alipay_dict()
            else:
                params['picture_list'] = self.picture_list
        if self.poi:
            if hasattr(self.poi, 'to_alipay_dict'):
                params['poi'] = self.poi.to_alipay_dict()
            else:
                params['poi'] = self.poi
        if self.poster:
            if hasattr(self.poster, 'to_alipay_dict'):
                params['poster'] = self.poster.to_alipay_dict()
            else:
                params['poster'] = self.poster
        if self.product_type_list:
            if isinstance(self.product_type_list, list):
                for i in range(0, len(self.product_type_list)):
                    element = self.product_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_type_list[i] = element.to_alipay_dict()
            if hasattr(self.product_type_list, 'to_alipay_dict'):
                params['product_type_list'] = self.product_type_list.to_alipay_dict()
            else:
                params['product_type_list'] = self.product_type_list
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.sub_venue_list:
            if isinstance(self.sub_venue_list, list):
                for i in range(0, len(self.sub_venue_list)):
                    element = self.sub_venue_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_venue_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_venue_list, 'to_alipay_dict'):
                params['sub_venue_list'] = self.sub_venue_list.to_alipay_dict()
            else:
                params['sub_venue_list'] = self.sub_venue_list
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
        if self.test_venue:
            if hasattr(self.test_venue, 'to_alipay_dict'):
                params['test_venue'] = self.test_venue.to_alipay_dict()
            else:
                params['test_venue'] = self.test_venue
        if self.traffic:
            if hasattr(self.traffic, 'to_alipay_dict'):
                params['traffic'] = self.traffic.to_alipay_dict()
            else:
                params['traffic'] = self.traffic
        if self.venue_pid:
            if hasattr(self.venue_pid, 'to_alipay_dict'):
                params['venue_pid'] = self.venue_pid.to_alipay_dict()
            else:
                params['venue_pid'] = self.venue_pid
        if self.venue_type:
            if isinstance(self.venue_type, list):
                for i in range(0, len(self.venue_type)):
                    element = self.venue_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.venue_type[i] = element.to_alipay_dict()
            if hasattr(self.venue_type, 'to_alipay_dict'):
                params['venue_type'] = self.venue_type.to_alipay_dict()
            else:
                params['venue_type'] = self.venue_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsVenueCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'bookable' in d:
            o.bookable = d['bookable']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'desc' in d:
            o.desc = d['desc']
        if 'extra_service_url' in d:
            o.extra_service_url = d['extra_service_url']
        if 'join_type' in d:
            o.join_type = d['join_type']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'name' in d:
            o.name = d['name']
        if 'opening_hours' in d:
            o.opening_hours = d['opening_hours']
        if 'out_venue_id' in d:
            o.out_venue_id = d['out_venue_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'picture_list' in d:
            o.picture_list = d['picture_list']
        if 'poi' in d:
            o.poi = d['poi']
        if 'poster' in d:
            o.poster = d['poster']
        if 'product_type_list' in d:
            o.product_type_list = d['product_type_list']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'sub_venue_list' in d:
            o.sub_venue_list = d['sub_venue_list']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        if 'test_venue' in d:
            o.test_venue = d['test_venue']
        if 'traffic' in d:
            o.traffic = d['traffic']
        if 'venue_pid' in d:
            o.venue_pid = d['venue_pid']
        if 'venue_type' in d:
            o.venue_type = d['venue_type']
        return o



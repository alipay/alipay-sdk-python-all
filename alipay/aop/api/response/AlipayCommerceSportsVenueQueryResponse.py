#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubVenueQueryInfo import SubVenueQueryInfo


class AlipayCommerceSportsVenueQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsVenueQueryResponse, self).__init__()
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
        self._traffic = None
        self._venue_id = None
        self._venue_pid = None
        self._venue_status = None
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
                if isinstance(i, SubVenueQueryInfo):
                    self._sub_venue_list.append(i)
                else:
                    self._sub_venue_list.append(SubVenueQueryInfo.from_alipay_dict(i))
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
    def traffic(self):
        return self._traffic

    @traffic.setter
    def traffic(self, value):
        self._traffic = value
    @property
    def venue_id(self):
        return self._venue_id

    @venue_id.setter
    def venue_id(self, value):
        self._venue_id = value
    @property
    def venue_pid(self):
        return self._venue_pid

    @venue_pid.setter
    def venue_pid(self, value):
        self._venue_pid = value
    @property
    def venue_status(self):
        return self._venue_status

    @venue_status.setter
    def venue_status(self, value):
        self._venue_status = value
    @property
    def venue_type(self):
        return self._venue_type

    @venue_type.setter
    def venue_type(self, value):
        if isinstance(value, list):
            self._venue_type = list()
            for i in value:
                self._venue_type.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsVenueQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'area_code' in response:
            self.area_code = response['area_code']
        if 'bookable' in response:
            self.bookable = response['bookable']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'desc' in response:
            self.desc = response['desc']
        if 'extra_service_url' in response:
            self.extra_service_url = response['extra_service_url']
        if 'join_type' in response:
            self.join_type = response['join_type']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'name' in response:
            self.name = response['name']
        if 'opening_hours' in response:
            self.opening_hours = response['opening_hours']
        if 'out_venue_id' in response:
            self.out_venue_id = response['out_venue_id']
        if 'phone' in response:
            self.phone = response['phone']
        if 'picture_list' in response:
            self.picture_list = response['picture_list']
        if 'poi' in response:
            self.poi = response['poi']
        if 'poster' in response:
            self.poster = response['poster']
        if 'product_type_list' in response:
            self.product_type_list = response['product_type_list']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'sub_venue_list' in response:
            self.sub_venue_list = response['sub_venue_list']
        if 'tag_list' in response:
            self.tag_list = response['tag_list']
        if 'traffic' in response:
            self.traffic = response['traffic']
        if 'venue_id' in response:
            self.venue_id = response['venue_id']
        if 'venue_pid' in response:
            self.venue_pid = response['venue_pid']
        if 'venue_status' in response:
            self.venue_status = response['venue_status']
        if 'venue_type' in response:
            self.venue_type = response['venue_type']

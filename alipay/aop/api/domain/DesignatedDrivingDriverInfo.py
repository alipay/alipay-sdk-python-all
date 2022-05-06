#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DesignatedDrivingDriverInfo(object):

    def __init__(self):
        self._contact_phone = None
        self._distance = None
        self._driver_id = None
        self._driver_name = None
        self._driving_years = None
        self._head_img = None
        self._isv = None
        self._latitude = None
        self._longitude = None
        self._service_times = None
        self._star_level = None

    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def driver_id(self):
        return self._driver_id

    @driver_id.setter
    def driver_id(self, value):
        self._driver_id = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def driving_years(self):
        return self._driving_years

    @driving_years.setter
    def driving_years(self, value):
        self._driving_years = value
    @property
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
    @property
    def isv(self):
        return self._isv

    @isv.setter
    def isv(self, value):
        self._isv = value
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
    def service_times(self):
        return self._service_times

    @service_times.setter
    def service_times(self, value):
        self._service_times = value
    @property
    def star_level(self):
        return self._star_level

    @star_level.setter
    def star_level(self, value):
        self._star_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.driver_id:
            if hasattr(self.driver_id, 'to_alipay_dict'):
                params['driver_id'] = self.driver_id.to_alipay_dict()
            else:
                params['driver_id'] = self.driver_id
        if self.driver_name:
            if hasattr(self.driver_name, 'to_alipay_dict'):
                params['driver_name'] = self.driver_name.to_alipay_dict()
            else:
                params['driver_name'] = self.driver_name
        if self.driving_years:
            if hasattr(self.driving_years, 'to_alipay_dict'):
                params['driving_years'] = self.driving_years.to_alipay_dict()
            else:
                params['driving_years'] = self.driving_years
        if self.head_img:
            if hasattr(self.head_img, 'to_alipay_dict'):
                params['head_img'] = self.head_img.to_alipay_dict()
            else:
                params['head_img'] = self.head_img
        if self.isv:
            if hasattr(self.isv, 'to_alipay_dict'):
                params['isv'] = self.isv.to_alipay_dict()
            else:
                params['isv'] = self.isv
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
        if self.service_times:
            if hasattr(self.service_times, 'to_alipay_dict'):
                params['service_times'] = self.service_times.to_alipay_dict()
            else:
                params['service_times'] = self.service_times
        if self.star_level:
            if hasattr(self.star_level, 'to_alipay_dict'):
                params['star_level'] = self.star_level.to_alipay_dict()
            else:
                params['star_level'] = self.star_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DesignatedDrivingDriverInfo()
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'distance' in d:
            o.distance = d['distance']
        if 'driver_id' in d:
            o.driver_id = d['driver_id']
        if 'driver_name' in d:
            o.driver_name = d['driver_name']
        if 'driving_years' in d:
            o.driving_years = d['driving_years']
        if 'head_img' in d:
            o.head_img = d['head_img']
        if 'isv' in d:
            o.isv = d['isv']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'service_times' in d:
            o.service_times = d['service_times']
        if 'star_level' in d:
            o.star_level = d['star_level']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProviderShop(object):

    def __init__(self):
        self._business_hours = None
        self._business_weeks = None
        self._detail_address = None
        self._latitude = None
        self._longitude = None
        self._shop_area = None
        self._shop_name = None
        self._shop_phone_num = None

    @property
    def business_hours(self):
        return self._business_hours

    @business_hours.setter
    def business_hours(self, value):
        self._business_hours = value
    @property
    def business_weeks(self):
        return self._business_weeks

    @business_weeks.setter
    def business_weeks(self, value):
        self._business_weeks = value
    @property
    def detail_address(self):
        return self._detail_address

    @detail_address.setter
    def detail_address(self, value):
        self._detail_address = value
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
    def shop_area(self):
        return self._shop_area

    @shop_area.setter
    def shop_area(self, value):
        self._shop_area = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_phone_num(self):
        return self._shop_phone_num

    @shop_phone_num.setter
    def shop_phone_num(self, value):
        self._shop_phone_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_hours:
            if hasattr(self.business_hours, 'to_alipay_dict'):
                params['business_hours'] = self.business_hours.to_alipay_dict()
            else:
                params['business_hours'] = self.business_hours
        if self.business_weeks:
            if hasattr(self.business_weeks, 'to_alipay_dict'):
                params['business_weeks'] = self.business_weeks.to_alipay_dict()
            else:
                params['business_weeks'] = self.business_weeks
        if self.detail_address:
            if hasattr(self.detail_address, 'to_alipay_dict'):
                params['detail_address'] = self.detail_address.to_alipay_dict()
            else:
                params['detail_address'] = self.detail_address
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
        if self.shop_area:
            if hasattr(self.shop_area, 'to_alipay_dict'):
                params['shop_area'] = self.shop_area.to_alipay_dict()
            else:
                params['shop_area'] = self.shop_area
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_phone_num:
            if hasattr(self.shop_phone_num, 'to_alipay_dict'):
                params['shop_phone_num'] = self.shop_phone_num.to_alipay_dict()
            else:
                params['shop_phone_num'] = self.shop_phone_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProviderShop()
        if 'business_hours' in d:
            o.business_hours = d['business_hours']
        if 'business_weeks' in d:
            o.business_weeks = d['business_weeks']
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'shop_area' in d:
            o.shop_area = d['shop_area']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_phone_num' in d:
            o.shop_phone_num = d['shop_phone_num']
        return o



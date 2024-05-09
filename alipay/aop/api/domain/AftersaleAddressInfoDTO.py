#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AftersaleAddressInfoDTO(object):

    def __init__(self):
        self._area = None
        self._city = None
        self._detail = None
        self._phone_number = None
        self._province = None
        self._user_name = None

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AftersaleAddressInfoDTO()
        if 'area' in d:
            o.area = d['area']
        if 'city' in d:
            o.city = d['city']
        if 'detail' in d:
            o.detail = d['detail']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'province' in d:
            o.province = d['province']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o



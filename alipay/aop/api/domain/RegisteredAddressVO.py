#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AreaInfoVO import AreaInfoVO
from alipay.aop.api.domain.AreaInfoVO import AreaInfoVO
from alipay.aop.api.domain.AreaInfoVO import AreaInfoVO


class RegisteredAddressVO(object):

    def __init__(self):
        self._city = None
        self._custom = None
        self._district = None
        self._province = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, AreaInfoVO):
            self._city = value
        else:
            self._city = AreaInfoVO.from_alipay_dict(value)
    @property
    def custom(self):
        return self._custom

    @custom.setter
    def custom(self, value):
        self._custom = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        if isinstance(value, AreaInfoVO):
            self._district = value
        else:
            self._district = AreaInfoVO.from_alipay_dict(value)
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        if isinstance(value, AreaInfoVO):
            self._province = value
        else:
            self._province = AreaInfoVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.custom:
            if hasattr(self.custom, 'to_alipay_dict'):
                params['custom'] = self.custom.to_alipay_dict()
            else:
                params['custom'] = self.custom
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisteredAddressVO()
        if 'city' in d:
            o.city = d['city']
        if 'custom' in d:
            o.custom = d['custom']
        if 'district' in d:
            o.district = d['district']
        if 'province' in d:
            o.province = d['province']
        return o



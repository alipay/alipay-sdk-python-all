#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehOpenBrandDTO(object):

    def __init__(self):
        self._brand_established_year = None
        self._brand_id = None
        self._brand_logo = None
        self._brand_name = None
        self._brand_name_en = None
        self._brand_origin = None
        self._initial = None

    @property
    def brand_established_year(self):
        return self._brand_established_year

    @brand_established_year.setter
    def brand_established_year(self, value):
        self._brand_established_year = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def brand_name_en(self):
        return self._brand_name_en

    @brand_name_en.setter
    def brand_name_en(self, value):
        self._brand_name_en = value
    @property
    def brand_origin(self):
        return self._brand_origin

    @brand_origin.setter
    def brand_origin(self, value):
        self._brand_origin = value
    @property
    def initial(self):
        return self._initial

    @initial.setter
    def initial(self, value):
        self._initial = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_established_year:
            if hasattr(self.brand_established_year, 'to_alipay_dict'):
                params['brand_established_year'] = self.brand_established_year.to_alipay_dict()
            else:
                params['brand_established_year'] = self.brand_established_year
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.brand_name_en:
            if hasattr(self.brand_name_en, 'to_alipay_dict'):
                params['brand_name_en'] = self.brand_name_en.to_alipay_dict()
            else:
                params['brand_name_en'] = self.brand_name_en
        if self.brand_origin:
            if hasattr(self.brand_origin, 'to_alipay_dict'):
                params['brand_origin'] = self.brand_origin.to_alipay_dict()
            else:
                params['brand_origin'] = self.brand_origin
        if self.initial:
            if hasattr(self.initial, 'to_alipay_dict'):
                params['initial'] = self.initial.to_alipay_dict()
            else:
                params['initial'] = self.initial
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehOpenBrandDTO()
        if 'brand_established_year' in d:
            o.brand_established_year = d['brand_established_year']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'brand_name_en' in d:
            o.brand_name_en = d['brand_name_en']
        if 'brand_origin' in d:
            o.brand_origin = d['brand_origin']
        if 'initial' in d:
            o.initial = d['initial']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MobilePhoneInfo(object):

    def __init__(self):
        self._city = None
        self._mobile = None
        self._operator_abbr = None
        self._operator_name = None
        self._province = None
        self._segment_number = None
        self._sub_operator = None
        self._tel_code = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def operator_abbr(self):
        return self._operator_abbr

    @operator_abbr.setter
    def operator_abbr(self, value):
        self._operator_abbr = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def segment_number(self):
        return self._segment_number

    @segment_number.setter
    def segment_number(self, value):
        self._segment_number = value
    @property
    def sub_operator(self):
        return self._sub_operator

    @sub_operator.setter
    def sub_operator(self, value):
        self._sub_operator = value
    @property
    def tel_code(self):
        return self._tel_code

    @tel_code.setter
    def tel_code(self, value):
        self._tel_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.operator_abbr:
            if hasattr(self.operator_abbr, 'to_alipay_dict'):
                params['operator_abbr'] = self.operator_abbr.to_alipay_dict()
            else:
                params['operator_abbr'] = self.operator_abbr
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.segment_number:
            if hasattr(self.segment_number, 'to_alipay_dict'):
                params['segment_number'] = self.segment_number.to_alipay_dict()
            else:
                params['segment_number'] = self.segment_number
        if self.sub_operator:
            if hasattr(self.sub_operator, 'to_alipay_dict'):
                params['sub_operator'] = self.sub_operator.to_alipay_dict()
            else:
                params['sub_operator'] = self.sub_operator
        if self.tel_code:
            if hasattr(self.tel_code, 'to_alipay_dict'):
                params['tel_code'] = self.tel_code.to_alipay_dict()
            else:
                params['tel_code'] = self.tel_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MobilePhoneInfo()
        if 'city' in d:
            o.city = d['city']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'operator_abbr' in d:
            o.operator_abbr = d['operator_abbr']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'province' in d:
            o.province = d['province']
        if 'segment_number' in d:
            o.segment_number = d['segment_number']
        if 'sub_operator' in d:
            o.sub_operator = d['sub_operator']
        if 'tel_code' in d:
            o.tel_code = d['tel_code']
        return o



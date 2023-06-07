#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EbikeBindInfo(object):

    def __init__(self):
        self._brand_code = None
        self._brand_name = None
        self._can_report_riding_distance = None
        self._ebike_name = None
        self._ebike_no = None
        self._ebike_type = None
        self._is_bind = None

    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def can_report_riding_distance(self):
        return self._can_report_riding_distance

    @can_report_riding_distance.setter
    def can_report_riding_distance(self, value):
        self._can_report_riding_distance = value
    @property
    def ebike_name(self):
        return self._ebike_name

    @ebike_name.setter
    def ebike_name(self, value):
        self._ebike_name = value
    @property
    def ebike_no(self):
        return self._ebike_no

    @ebike_no.setter
    def ebike_no(self, value):
        self._ebike_no = value
    @property
    def ebike_type(self):
        return self._ebike_type

    @ebike_type.setter
    def ebike_type(self, value):
        self._ebike_type = value
    @property
    def is_bind(self):
        return self._is_bind

    @is_bind.setter
    def is_bind(self, value):
        self._is_bind = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.can_report_riding_distance:
            if hasattr(self.can_report_riding_distance, 'to_alipay_dict'):
                params['can_report_riding_distance'] = self.can_report_riding_distance.to_alipay_dict()
            else:
                params['can_report_riding_distance'] = self.can_report_riding_distance
        if self.ebike_name:
            if hasattr(self.ebike_name, 'to_alipay_dict'):
                params['ebike_name'] = self.ebike_name.to_alipay_dict()
            else:
                params['ebike_name'] = self.ebike_name
        if self.ebike_no:
            if hasattr(self.ebike_no, 'to_alipay_dict'):
                params['ebike_no'] = self.ebike_no.to_alipay_dict()
            else:
                params['ebike_no'] = self.ebike_no
        if self.ebike_type:
            if hasattr(self.ebike_type, 'to_alipay_dict'):
                params['ebike_type'] = self.ebike_type.to_alipay_dict()
            else:
                params['ebike_type'] = self.ebike_type
        if self.is_bind:
            if hasattr(self.is_bind, 'to_alipay_dict'):
                params['is_bind'] = self.is_bind.to_alipay_dict()
            else:
                params['is_bind'] = self.is_bind
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EbikeBindInfo()
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'can_report_riding_distance' in d:
            o.can_report_riding_distance = d['can_report_riding_distance']
        if 'ebike_name' in d:
            o.ebike_name = d['ebike_name']
        if 'ebike_no' in d:
            o.ebike_no = d['ebike_no']
        if 'ebike_type' in d:
            o.ebike_type = d['ebike_type']
        if 'is_bind' in d:
            o.is_bind = d['is_bind']
        return o



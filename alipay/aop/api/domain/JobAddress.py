#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JobAddress(object):

    def __init__(self):
        self._address_name = None
        self._detail = None
        self._geo = None
        self._region_code = None

    @property
    def address_name(self):
        return self._address_name

    @address_name.setter
    def address_name(self, value):
        self._address_name = value
    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def geo(self):
        return self._geo

    @geo.setter
    def geo(self, value):
        self._geo = value
    @property
    def region_code(self):
        return self._region_code

    @region_code.setter
    def region_code(self, value):
        self._region_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_name:
            if hasattr(self.address_name, 'to_alipay_dict'):
                params['address_name'] = self.address_name.to_alipay_dict()
            else:
                params['address_name'] = self.address_name
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.geo:
            if hasattr(self.geo, 'to_alipay_dict'):
                params['geo'] = self.geo.to_alipay_dict()
            else:
                params['geo'] = self.geo
        if self.region_code:
            if hasattr(self.region_code, 'to_alipay_dict'):
                params['region_code'] = self.region_code.to_alipay_dict()
            else:
                params['region_code'] = self.region_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JobAddress()
        if 'address_name' in d:
            o.address_name = d['address_name']
        if 'detail' in d:
            o.detail = d['detail']
        if 'geo' in d:
            o.geo = d['geo']
        if 'region_code' in d:
            o.region_code = d['region_code']
        return o



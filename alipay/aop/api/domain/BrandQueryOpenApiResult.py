#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BrandQueryOpenApiResult(object):

    def __init__(self):
        self._brand_name = None
        self._brand_no = None
        self._logo_url = None
        self._owner_name = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def brand_no(self):
        return self._brand_no

    @brand_no.setter
    def brand_no(self, value):
        self._brand_no = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.brand_no:
            if hasattr(self.brand_no, 'to_alipay_dict'):
                params['brand_no'] = self.brand_no.to_alipay_dict()
            else:
                params['brand_no'] = self.brand_no
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandQueryOpenApiResult()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'brand_no' in d:
            o.brand_no = d['brand_no']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        return o



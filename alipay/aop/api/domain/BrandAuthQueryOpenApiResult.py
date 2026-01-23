#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandAppInfoOpenApi import BrandAppInfoOpenApi


class BrandAuthQueryOpenApiResult(object):

    def __init__(self):
        self._brand_app_list = None
        self._brand_id = None
        self._brand_name = None
        self._logo_url = None
        self._owner_name = None
        self._standard = None
        self._status = None

    @property
    def brand_app_list(self):
        return self._brand_app_list

    @brand_app_list.setter
    def brand_app_list(self, value):
        if isinstance(value, list):
            self._brand_app_list = list()
            for i in value:
                if isinstance(i, BrandAppInfoOpenApi):
                    self._brand_app_list.append(i)
                else:
                    self._brand_app_list.append(BrandAppInfoOpenApi.from_alipay_dict(i))
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
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
    @property
    def standard(self):
        return self._standard

    @standard.setter
    def standard(self, value):
        self._standard = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_app_list:
            if isinstance(self.brand_app_list, list):
                for i in range(0, len(self.brand_app_list)):
                    element = self.brand_app_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_app_list[i] = element.to_alipay_dict()
            if hasattr(self.brand_app_list, 'to_alipay_dict'):
                params['brand_app_list'] = self.brand_app_list.to_alipay_dict()
            else:
                params['brand_app_list'] = self.brand_app_list
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
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
        if self.standard:
            if hasattr(self.standard, 'to_alipay_dict'):
                params['standard'] = self.standard.to_alipay_dict()
            else:
                params['standard'] = self.standard
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandAuthQueryOpenApiResult()
        if 'brand_app_list' in d:
            o.brand_app_list = d['brand_app_list']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'standard' in d:
            o.standard = d['standard']
        if 'status' in d:
            o.status = d['status']
        return o



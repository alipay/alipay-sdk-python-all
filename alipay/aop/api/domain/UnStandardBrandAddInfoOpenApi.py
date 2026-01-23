#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandFileInfoOpenApi import BrandFileInfoOpenApi


class UnStandardBrandAddInfoOpenApi(object):

    def __init__(self):
        self._biz_type = None
        self._brand_category = None
        self._brand_category_name = None
        self._certification_files = None
        self._certification_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def brand_category(self):
        return self._brand_category

    @brand_category.setter
    def brand_category(self, value):
        if isinstance(value, list):
            self._brand_category = list()
            for i in value:
                self._brand_category.append(i)
    @property
    def brand_category_name(self):
        return self._brand_category_name

    @brand_category_name.setter
    def brand_category_name(self, value):
        self._brand_category_name = value
    @property
    def certification_files(self):
        return self._certification_files

    @certification_files.setter
    def certification_files(self, value):
        if isinstance(value, list):
            self._certification_files = list()
            for i in value:
                if isinstance(i, BrandFileInfoOpenApi):
                    self._certification_files.append(i)
                else:
                    self._certification_files.append(BrandFileInfoOpenApi.from_alipay_dict(i))
    @property
    def certification_type(self):
        return self._certification_type

    @certification_type.setter
    def certification_type(self, value):
        self._certification_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.brand_category:
            if isinstance(self.brand_category, list):
                for i in range(0, len(self.brand_category)):
                    element = self.brand_category[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_category[i] = element.to_alipay_dict()
            if hasattr(self.brand_category, 'to_alipay_dict'):
                params['brand_category'] = self.brand_category.to_alipay_dict()
            else:
                params['brand_category'] = self.brand_category
        if self.brand_category_name:
            if hasattr(self.brand_category_name, 'to_alipay_dict'):
                params['brand_category_name'] = self.brand_category_name.to_alipay_dict()
            else:
                params['brand_category_name'] = self.brand_category_name
        if self.certification_files:
            if isinstance(self.certification_files, list):
                for i in range(0, len(self.certification_files)):
                    element = self.certification_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certification_files[i] = element.to_alipay_dict()
            if hasattr(self.certification_files, 'to_alipay_dict'):
                params['certification_files'] = self.certification_files.to_alipay_dict()
            else:
                params['certification_files'] = self.certification_files
        if self.certification_type:
            if hasattr(self.certification_type, 'to_alipay_dict'):
                params['certification_type'] = self.certification_type.to_alipay_dict()
            else:
                params['certification_type'] = self.certification_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnStandardBrandAddInfoOpenApi()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'brand_category' in d:
            o.brand_category = d['brand_category']
        if 'brand_category_name' in d:
            o.brand_category_name = d['brand_category_name']
        if 'certification_files' in d:
            o.certification_files = d['certification_files']
        if 'certification_type' in d:
            o.certification_type = d['certification_type']
        return o



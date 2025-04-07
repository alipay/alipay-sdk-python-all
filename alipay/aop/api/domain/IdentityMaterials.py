#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IdentityMaterials(object):

    def __init__(self):
        self._description = None
        self._material_type = None
        self._pic_urls = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def pic_urls(self):
        return self._pic_urls

    @pic_urls.setter
    def pic_urls(self, value):
        if isinstance(value, list):
            self._pic_urls = list()
            for i in value:
                self._pic_urls.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        if self.pic_urls:
            if isinstance(self.pic_urls, list):
                for i in range(0, len(self.pic_urls)):
                    element = self.pic_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pic_urls[i] = element.to_alipay_dict()
            if hasattr(self.pic_urls, 'to_alipay_dict'):
                params['pic_urls'] = self.pic_urls.to_alipay_dict()
            else:
                params['pic_urls'] = self.pic_urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IdentityMaterials()
        if 'description' in d:
            o.description = d['description']
        if 'material_type' in d:
            o.material_type = d['material_type']
        if 'pic_urls' in d:
            o.pic_urls = d['pic_urls']
        return o



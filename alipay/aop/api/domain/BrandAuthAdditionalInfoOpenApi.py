#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandAppInfoOpenApi import BrandAppInfoOpenApi
from alipay.aop.api.domain.BrandFileInfoOpenApi import BrandFileInfoOpenApi


class BrandAuthAdditionalInfoOpenApi(object):

    def __init__(self):
        self._brand_app_infos = None
        self._brand_op_logo = None
        self._brand_use_scene = None

    @property
    def brand_app_infos(self):
        return self._brand_app_infos

    @brand_app_infos.setter
    def brand_app_infos(self, value):
        if isinstance(value, list):
            self._brand_app_infos = list()
            for i in value:
                if isinstance(i, BrandAppInfoOpenApi):
                    self._brand_app_infos.append(i)
                else:
                    self._brand_app_infos.append(BrandAppInfoOpenApi.from_alipay_dict(i))
    @property
    def brand_op_logo(self):
        return self._brand_op_logo

    @brand_op_logo.setter
    def brand_op_logo(self, value):
        if isinstance(value, BrandFileInfoOpenApi):
            self._brand_op_logo = value
        else:
            self._brand_op_logo = BrandFileInfoOpenApi.from_alipay_dict(value)
    @property
    def brand_use_scene(self):
        return self._brand_use_scene

    @brand_use_scene.setter
    def brand_use_scene(self, value):
        if isinstance(value, list):
            self._brand_use_scene = list()
            for i in value:
                self._brand_use_scene.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.brand_app_infos:
            if isinstance(self.brand_app_infos, list):
                for i in range(0, len(self.brand_app_infos)):
                    element = self.brand_app_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_app_infos[i] = element.to_alipay_dict()
            if hasattr(self.brand_app_infos, 'to_alipay_dict'):
                params['brand_app_infos'] = self.brand_app_infos.to_alipay_dict()
            else:
                params['brand_app_infos'] = self.brand_app_infos
        if self.brand_op_logo:
            if hasattr(self.brand_op_logo, 'to_alipay_dict'):
                params['brand_op_logo'] = self.brand_op_logo.to_alipay_dict()
            else:
                params['brand_op_logo'] = self.brand_op_logo
        if self.brand_use_scene:
            if isinstance(self.brand_use_scene, list):
                for i in range(0, len(self.brand_use_scene)):
                    element = self.brand_use_scene[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_use_scene[i] = element.to_alipay_dict()
            if hasattr(self.brand_use_scene, 'to_alipay_dict'):
                params['brand_use_scene'] = self.brand_use_scene.to_alipay_dict()
            else:
                params['brand_use_scene'] = self.brand_use_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandAuthAdditionalInfoOpenApi()
        if 'brand_app_infos' in d:
            o.brand_app_infos = d['brand_app_infos']
        if 'brand_op_logo' in d:
            o.brand_op_logo = d['brand_op_logo']
        if 'brand_use_scene' in d:
            o.brand_use_scene = d['brand_use_scene']
        return o



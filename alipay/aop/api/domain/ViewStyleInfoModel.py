#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ViewStyleInfoModel(object):

    def __init__(self):
        self._bg_color = None
        self._bg_img = None
        self._brand_name = None
        self._logo_img = None

    @property
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, value):
        self._bg_color = value
    @property
    def bg_img(self):
        return self._bg_img

    @bg_img.setter
    def bg_img(self, value):
        self._bg_img = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def logo_img(self):
        return self._logo_img

    @logo_img.setter
    def logo_img(self, value):
        self._logo_img = value


    def to_alipay_dict(self):
        params = dict()
        if self.bg_color:
            if hasattr(self.bg_color, 'to_alipay_dict'):
                params['bg_color'] = self.bg_color.to_alipay_dict()
            else:
                params['bg_color'] = self.bg_color
        if self.bg_img:
            if hasattr(self.bg_img, 'to_alipay_dict'):
                params['bg_img'] = self.bg_img.to_alipay_dict()
            else:
                params['bg_img'] = self.bg_img
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.logo_img:
            if hasattr(self.logo_img, 'to_alipay_dict'):
                params['logo_img'] = self.logo_img.to_alipay_dict()
            else:
                params['logo_img'] = self.logo_img
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ViewStyleInfoModel()
        if 'bg_color' in d:
            o.bg_color = d['bg_color']
        if 'bg_img' in d:
            o.bg_img = d['bg_img']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'logo_img' in d:
            o.logo_img = d['logo_img']
        return o



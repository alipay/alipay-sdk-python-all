#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GiftTemplateAtmosphereBox(object):

    def __init__(self):
        self._atmosphere_gif_url = None
        self._atmosphere_plus_url = None
        self._atmosphere_type = None
        self._atmosphere_url = None

    @property
    def atmosphere_gif_url(self):
        return self._atmosphere_gif_url

    @atmosphere_gif_url.setter
    def atmosphere_gif_url(self, value):
        self._atmosphere_gif_url = value
    @property
    def atmosphere_plus_url(self):
        return self._atmosphere_plus_url

    @atmosphere_plus_url.setter
    def atmosphere_plus_url(self, value):
        self._atmosphere_plus_url = value
    @property
    def atmosphere_type(self):
        return self._atmosphere_type

    @atmosphere_type.setter
    def atmosphere_type(self, value):
        self._atmosphere_type = value
    @property
    def atmosphere_url(self):
        return self._atmosphere_url

    @atmosphere_url.setter
    def atmosphere_url(self, value):
        self._atmosphere_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.atmosphere_gif_url:
            if hasattr(self.atmosphere_gif_url, 'to_alipay_dict'):
                params['atmosphere_gif_url'] = self.atmosphere_gif_url.to_alipay_dict()
            else:
                params['atmosphere_gif_url'] = self.atmosphere_gif_url
        if self.atmosphere_plus_url:
            if hasattr(self.atmosphere_plus_url, 'to_alipay_dict'):
                params['atmosphere_plus_url'] = self.atmosphere_plus_url.to_alipay_dict()
            else:
                params['atmosphere_plus_url'] = self.atmosphere_plus_url
        if self.atmosphere_type:
            if hasattr(self.atmosphere_type, 'to_alipay_dict'):
                params['atmosphere_type'] = self.atmosphere_type.to_alipay_dict()
            else:
                params['atmosphere_type'] = self.atmosphere_type
        if self.atmosphere_url:
            if hasattr(self.atmosphere_url, 'to_alipay_dict'):
                params['atmosphere_url'] = self.atmosphere_url.to_alipay_dict()
            else:
                params['atmosphere_url'] = self.atmosphere_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftTemplateAtmosphereBox()
        if 'atmosphere_gif_url' in d:
            o.atmosphere_gif_url = d['atmosphere_gif_url']
        if 'atmosphere_plus_url' in d:
            o.atmosphere_plus_url = d['atmosphere_plus_url']
        if 'atmosphere_type' in d:
            o.atmosphere_type = d['atmosphere_type']
        if 'atmosphere_url' in d:
            o.atmosphere_url = d['atmosphere_url']
        return o



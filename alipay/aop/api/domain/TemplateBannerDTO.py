#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateBannerDTO(object):

    def __init__(self):
        self._banner_img = None
        self._banner_url = None

    @property
    def banner_img(self):
        return self._banner_img

    @banner_img.setter
    def banner_img(self, value):
        self._banner_img = value
    @property
    def banner_url(self):
        return self._banner_url

    @banner_url.setter
    def banner_url(self, value):
        self._banner_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.banner_img:
            if hasattr(self.banner_img, 'to_alipay_dict'):
                params['banner_img'] = self.banner_img.to_alipay_dict()
            else:
                params['banner_img'] = self.banner_img
        if self.banner_url:
            if hasattr(self.banner_url, 'to_alipay_dict'):
                params['banner_url'] = self.banner_url.to_alipay_dict()
            else:
                params['banner_url'] = self.banner_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateBannerDTO()
        if 'banner_img' in d:
            o.banner_img = d['banner_img']
        if 'banner_url' in d:
            o.banner_url = d['banner_url']
        return o



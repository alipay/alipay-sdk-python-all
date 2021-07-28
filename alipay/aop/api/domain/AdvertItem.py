#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdvertItem(object):

    def __init__(self):
        self._img_url = None
        self._link_type = None
        self._link_url = None
        self._name = None

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def link_type(self):
        return self._link_type

    @link_type.setter
    def link_type(self, value):
        self._link_type = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.link_type:
            if hasattr(self.link_type, 'to_alipay_dict'):
                params['link_type'] = self.link_type.to_alipay_dict()
            else:
                params['link_type'] = self.link_type
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdvertItem()
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'link_type' in d:
            o.link_type = d['link_type']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'name' in d:
            o.name = d['name']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomConfigVO(object):

    def __init__(self):
        self._config_switch = None
        self._image_url = None
        self._link_url = None
        self._type = None

    @property
    def config_switch(self):
        return self._config_switch

    @config_switch.setter
    def config_switch(self, value):
        self._config_switch = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.config_switch:
            if hasattr(self.config_switch, 'to_alipay_dict'):
                params['config_switch'] = self.config_switch.to_alipay_dict()
            else:
                params['config_switch'] = self.config_switch
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomConfigVO()
        if 'config_switch' in d:
            o.config_switch = d['config_switch']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'type' in d:
            o.type = d['type']
        return o



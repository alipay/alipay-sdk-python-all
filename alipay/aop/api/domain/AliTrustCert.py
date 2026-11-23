#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AliTrustCert(object):

    def __init__(self):
        self._forward_url = None
        self._icon_url = None
        self._is_certified = None
        self._level = None
        self._message = None

    @property
    def forward_url(self):
        return self._forward_url

    @forward_url.setter
    def forward_url(self, value):
        self._forward_url = value
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def is_certified(self):
        return self._is_certified

    @is_certified.setter
    def is_certified(self, value):
        self._is_certified = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value


    def to_alipay_dict(self):
        params = dict()
        if self.forward_url:
            if hasattr(self.forward_url, 'to_alipay_dict'):
                params['forward_url'] = self.forward_url.to_alipay_dict()
            else:
                params['forward_url'] = self.forward_url
        if self.icon_url:
            if hasattr(self.icon_url, 'to_alipay_dict'):
                params['icon_url'] = self.icon_url.to_alipay_dict()
            else:
                params['icon_url'] = self.icon_url
        if self.is_certified:
            if hasattr(self.is_certified, 'to_alipay_dict'):
                params['is_certified'] = self.is_certified.to_alipay_dict()
            else:
                params['is_certified'] = self.is_certified
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AliTrustCert()
        if 'forward_url' in d:
            o.forward_url = d['forward_url']
        if 'icon_url' in d:
            o.icon_url = d['icon_url']
        if 'is_certified' in d:
            o.is_certified = d['is_certified']
        if 'level' in d:
            o.level = d['level']
        if 'message' in d:
            o.message = d['message']
        return o



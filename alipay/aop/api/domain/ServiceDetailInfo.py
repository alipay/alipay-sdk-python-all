#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceDetailInfo(object):

    def __init__(self):
        self._code = None
        self._desc = None
        self._logo = None
        self._name = None
        self._type = None
        self._url = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceDetailInfo()
        if 'code' in d:
            o.code = d['code']
        if 'desc' in d:
            o.desc = d['desc']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'type' in d:
            o.type = d['type']
        if 'url' in d:
            o.url = d['url']
        return o



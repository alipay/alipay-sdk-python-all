#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduSourceInfo(object):

    def __init__(self):
        self._logo = None
        self._mobile = None
        self._name = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
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
        o = EduSourceInfo()
        if 'logo' in d:
            o.logo = d['logo']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        return o



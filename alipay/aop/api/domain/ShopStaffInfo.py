#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopStaffInfo(object):

    def __init__(self):
        self._desc = None
        self._name = None
        self._picture = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, value):
        self._picture = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.picture:
            if hasattr(self.picture, 'to_alipay_dict'):
                params['picture'] = self.picture.to_alipay_dict()
            else:
                params['picture'] = self.picture
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopStaffInfo()
        if 'desc' in d:
            o.desc = d['desc']
        if 'name' in d:
            o.name = d['name']
        if 'picture' in d:
            o.picture = d['picture']
        return o



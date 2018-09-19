#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Picture(object):

    def __init__(self):
        self._location = None
        self._name = None

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
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
        o = Picture()
        if 'location' in d:
            o.location = d['location']
        if 'name' in d:
            o.name = d['name']
        return o



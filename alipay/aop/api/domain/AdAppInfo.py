#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdAppInfo(object):

    def __init__(self):
        self._desc = None
        self._name = None
        self._series_app_id = None

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
    def series_app_id(self):
        return self._series_app_id

    @series_app_id.setter
    def series_app_id(self, value):
        self._series_app_id = value


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
        if self.series_app_id:
            if hasattr(self.series_app_id, 'to_alipay_dict'):
                params['series_app_id'] = self.series_app_id.to_alipay_dict()
            else:
                params['series_app_id'] = self.series_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdAppInfo()
        if 'desc' in d:
            o.desc = d['desc']
        if 'name' in d:
            o.name = d['name']
        if 'series_app_id' in d:
            o.series_app_id = d['series_app_id']
        return o



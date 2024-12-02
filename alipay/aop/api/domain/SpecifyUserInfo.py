#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecifyUserInfo(object):

    def __init__(self):
        self._specify_app_id = None
        self._specify_open_id = None

    @property
    def specify_app_id(self):
        return self._specify_app_id

    @specify_app_id.setter
    def specify_app_id(self, value):
        self._specify_app_id = value
    @property
    def specify_open_id(self):
        return self._specify_open_id

    @specify_open_id.setter
    def specify_open_id(self, value):
        self._specify_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.specify_app_id:
            if hasattr(self.specify_app_id, 'to_alipay_dict'):
                params['specify_app_id'] = self.specify_app_id.to_alipay_dict()
            else:
                params['specify_app_id'] = self.specify_app_id
        if self.specify_open_id:
            if hasattr(self.specify_open_id, 'to_alipay_dict'):
                params['specify_open_id'] = self.specify_open_id.to_alipay_dict()
            else:
                params['specify_open_id'] = self.specify_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecifyUserInfo()
        if 'specify_app_id' in d:
            o.specify_app_id = d['specify_app_id']
        if 'specify_open_id' in d:
            o.specify_open_id = d['specify_open_id']
        return o



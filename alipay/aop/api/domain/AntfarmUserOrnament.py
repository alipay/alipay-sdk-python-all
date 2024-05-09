#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfarmUserOrnament(object):

    def __init__(self):
        self._ornament_name = None
        self._resource_key = None
        self._sub_type = None

    @property
    def ornament_name(self):
        return self._ornament_name

    @ornament_name.setter
    def ornament_name(self, value):
        self._ornament_name = value
    @property
    def resource_key(self):
        return self._resource_key

    @resource_key.setter
    def resource_key(self, value):
        self._resource_key = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ornament_name:
            if hasattr(self.ornament_name, 'to_alipay_dict'):
                params['ornament_name'] = self.ornament_name.to_alipay_dict()
            else:
                params['ornament_name'] = self.ornament_name
        if self.resource_key:
            if hasattr(self.resource_key, 'to_alipay_dict'):
                params['resource_key'] = self.resource_key.to_alipay_dict()
            else:
                params['resource_key'] = self.resource_key
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfarmUserOrnament()
        if 'ornament_name' in d:
            o.ornament_name = d['ornament_name']
        if 'resource_key' in d:
            o.resource_key = d['resource_key']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        return o



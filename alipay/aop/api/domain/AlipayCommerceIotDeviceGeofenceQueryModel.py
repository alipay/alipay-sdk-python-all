#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDeviceGeofenceQueryModel(object):

    def __init__(self):
        self._route_code = None

    @property
    def route_code(self):
        return self._route_code

    @route_code.setter
    def route_code(self, value):
        self._route_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.route_code:
            if hasattr(self.route_code, 'to_alipay_dict'):
                params['route_code'] = self.route_code.to_alipay_dict()
            else:
                params['route_code'] = self.route_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceGeofenceQueryModel()
        if 'route_code' in d:
            o.route_code = d['route_code']
        return o



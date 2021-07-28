#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDeviceGeofenceBindModel(object):

    def __init__(self):
        self._biz_tid = None
        self._route_code = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def route_code(self):
        return self._route_code

    @route_code.setter
    def route_code(self, value):
        self._route_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
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
        o = AlipayCommerceIotDeviceGeofenceBindModel()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'route_code' in d:
            o.route_code = d['route_code']
        return o



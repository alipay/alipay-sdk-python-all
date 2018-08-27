#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarDataserviceViolationinfoShareModel(object):

    def __init__(self):
        self._app_id = None
        self._vehicle_id = None

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, value):
        self._app_id = value
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_id:
            if hasattr(self.app_id, 'to_alipay_dict'):
                params['app_id'] = self.app_id.to_alipay_dict()
            else:
                params['app_id'] = self.app_id
        if self.vehicle_id:
            if hasattr(self.vehicle_id, 'to_alipay_dict'):
                params['vehicle_id'] = self.vehicle_id.to_alipay_dict()
            else:
                params['vehicle_id'] = self.vehicle_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarDataserviceViolationinfoShareModel()
        if 'app_id' in d:
            o.app_id = d['app_id']
        if 'vehicle_id' in d:
            o.vehicle_id = d['vehicle_id']
        return o



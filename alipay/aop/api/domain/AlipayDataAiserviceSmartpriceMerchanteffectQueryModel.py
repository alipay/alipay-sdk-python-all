#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceSmartpriceMerchanteffectQueryModel(object):

    def __init__(self):
        self._app_version = None
        self._end_time = None
        self._merchant_id = None
        self._scene_code = None
        self._service_name = None
        self._start_time = None
        self._unit_id = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def unit_id(self):
        return self._unit_id

    @unit_id.setter
    def unit_id(self, value):
        self._unit_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.unit_id:
            if hasattr(self.unit_id, 'to_alipay_dict'):
                params['unit_id'] = self.unit_id.to_alipay_dict()
            else:
                params['unit_id'] = self.unit_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceSmartpriceMerchanteffectQueryModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'unit_id' in d:
            o.unit_id = d['unit_id']
        return o



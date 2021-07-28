#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceCloudbusScheduletriptimeGetModel(object):

    def __init__(self):
        self._aggregate_type = None
        self._app_version = None
        self._city_code = None
        self._config_id = None
        self._corp_id = None
        self._time_span = None

    @property
    def aggregate_type(self):
        return self._aggregate_type

    @aggregate_type.setter
    def aggregate_type(self, value):
        self._aggregate_type = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def config_id(self):
        return self._config_id

    @config_id.setter
    def config_id(self, value):
        self._config_id = value
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def time_span(self):
        return self._time_span

    @time_span.setter
    def time_span(self, value):
        self._time_span = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggregate_type:
            if hasattr(self.aggregate_type, 'to_alipay_dict'):
                params['aggregate_type'] = self.aggregate_type.to_alipay_dict()
            else:
                params['aggregate_type'] = self.aggregate_type
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.config_id:
            if hasattr(self.config_id, 'to_alipay_dict'):
                params['config_id'] = self.config_id.to_alipay_dict()
            else:
                params['config_id'] = self.config_id
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.time_span:
            if hasattr(self.time_span, 'to_alipay_dict'):
                params['time_span'] = self.time_span.to_alipay_dict()
            else:
                params['time_span'] = self.time_span
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceCloudbusScheduletriptimeGetModel()
        if 'aggregate_type' in d:
            o.aggregate_type = d['aggregate_type']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'config_id' in d:
            o.config_id = d['config_id']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'time_span' in d:
            o.time_span = d['time_span']
        return o



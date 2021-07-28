#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceCloudbusSchedualconfigSetModel(object):

    def __init__(self):
        self._app_version = None
        self._city_code = None
        self._config_name = None
        self._corp_id = None
        self._date = None

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
    def config_name(self):
        return self._config_name

    @config_name.setter
    def config_name(self, value):
        self._config_name = value
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, list):
            self._date = list()
            for i in value:
                self._date.append(i)


    def to_alipay_dict(self):
        params = dict()
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
        if self.config_name:
            if hasattr(self.config_name, 'to_alipay_dict'):
                params['config_name'] = self.config_name.to_alipay_dict()
            else:
                params['config_name'] = self.config_name
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.date:
            if isinstance(self.date, list):
                for i in range(0, len(self.date)):
                    element = self.date[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.date[i] = element.to_alipay_dict()
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceCloudbusSchedualconfigSetModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'config_name' in d:
            o.config_name = d['config_name']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'date' in d:
            o.date = d['date']
        return o



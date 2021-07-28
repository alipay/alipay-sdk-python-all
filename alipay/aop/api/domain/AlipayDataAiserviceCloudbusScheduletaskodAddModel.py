#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InputScheduleLine import InputScheduleLine


class AlipayDataAiserviceCloudbusScheduletaskodAddModel(object):

    def __init__(self):
        self._app_version = None
        self._city_code = None
        self._config_id = None
        self._corp_id = None
        self._line_info = None
        self._task_name = None

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
    def line_info(self):
        return self._line_info

    @line_info.setter
    def line_info(self, value):
        if isinstance(value, list):
            self._line_info = list()
            for i in value:
                if isinstance(i, InputScheduleLine):
                    self._line_info.append(i)
                else:
                    self._line_info.append(InputScheduleLine.from_alipay_dict(i))
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value


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
        if self.line_info:
            if isinstance(self.line_info, list):
                for i in range(0, len(self.line_info)):
                    element = self.line_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.line_info[i] = element.to_alipay_dict()
            if hasattr(self.line_info, 'to_alipay_dict'):
                params['line_info'] = self.line_info.to_alipay_dict()
            else:
                params['line_info'] = self.line_info
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceCloudbusScheduletaskodAddModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'config_id' in d:
            o.config_id = d['config_id']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'line_info' in d:
            o.line_info = d['line_info']
        if 'task_name' in d:
            o.task_name = d['task_name']
        return o



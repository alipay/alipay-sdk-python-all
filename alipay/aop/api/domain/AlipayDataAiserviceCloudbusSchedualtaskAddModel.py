#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceCloudbusSchedualtaskAddModel(object):

    def __init__(self):
        self._app_version = None
        self._city_code = None
        self._corp_id = None
        self._down_bus_cnt = None
        self._ext_param = None
        self._line_id = None
        self._partner_id = None
        self._task_name = None
        self._time_table_pid = None
        self._up_bus_cnt = None

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
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def down_bus_cnt(self):
        return self._down_bus_cnt

    @down_bus_cnt.setter
    def down_bus_cnt(self, value):
        self._down_bus_cnt = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def time_table_pid(self):
        return self._time_table_pid

    @time_table_pid.setter
    def time_table_pid(self, value):
        self._time_table_pid = value
    @property
    def up_bus_cnt(self):
        return self._up_bus_cnt

    @up_bus_cnt.setter
    def up_bus_cnt(self, value):
        self._up_bus_cnt = value


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
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.down_bus_cnt:
            if hasattr(self.down_bus_cnt, 'to_alipay_dict'):
                params['down_bus_cnt'] = self.down_bus_cnt.to_alipay_dict()
            else:
                params['down_bus_cnt'] = self.down_bus_cnt
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.time_table_pid:
            if hasattr(self.time_table_pid, 'to_alipay_dict'):
                params['time_table_pid'] = self.time_table_pid.to_alipay_dict()
            else:
                params['time_table_pid'] = self.time_table_pid
        if self.up_bus_cnt:
            if hasattr(self.up_bus_cnt, 'to_alipay_dict'):
                params['up_bus_cnt'] = self.up_bus_cnt.to_alipay_dict()
            else:
                params['up_bus_cnt'] = self.up_bus_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceCloudbusSchedualtaskAddModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'down_bus_cnt' in d:
            o.down_bus_cnt = d['down_bus_cnt']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'time_table_pid' in d:
            o.time_table_pid = d['time_table_pid']
        if 'up_bus_cnt' in d:
            o.up_bus_cnt = d['up_bus_cnt']
        return o



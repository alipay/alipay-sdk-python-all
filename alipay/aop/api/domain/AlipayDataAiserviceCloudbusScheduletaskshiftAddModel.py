#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceCloudbusScheduletaskshiftAddModel(object):

    def __init__(self):
        self._app_version = None
        self._city_code = None
        self._corp_id = None
        self._cycle_cnt = None
        self._driver_cnt = None
        self._ext_param = None
        self._line_id = None
        self._shift_date_list = None
        self._task_name = None
        self._work_schedule_pids = None

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
    def cycle_cnt(self):
        return self._cycle_cnt

    @cycle_cnt.setter
    def cycle_cnt(self, value):
        self._cycle_cnt = value
    @property
    def driver_cnt(self):
        return self._driver_cnt

    @driver_cnt.setter
    def driver_cnt(self, value):
        self._driver_cnt = value
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
    def shift_date_list(self):
        return self._shift_date_list

    @shift_date_list.setter
    def shift_date_list(self, value):
        if isinstance(value, list):
            self._shift_date_list = list()
            for i in value:
                self._shift_date_list.append(i)
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def work_schedule_pids(self):
        return self._work_schedule_pids

    @work_schedule_pids.setter
    def work_schedule_pids(self, value):
        if isinstance(value, list):
            self._work_schedule_pids = list()
            for i in value:
                self._work_schedule_pids.append(i)


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
        if self.cycle_cnt:
            if hasattr(self.cycle_cnt, 'to_alipay_dict'):
                params['cycle_cnt'] = self.cycle_cnt.to_alipay_dict()
            else:
                params['cycle_cnt'] = self.cycle_cnt
        if self.driver_cnt:
            if hasattr(self.driver_cnt, 'to_alipay_dict'):
                params['driver_cnt'] = self.driver_cnt.to_alipay_dict()
            else:
                params['driver_cnt'] = self.driver_cnt
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
        if self.shift_date_list:
            if isinstance(self.shift_date_list, list):
                for i in range(0, len(self.shift_date_list)):
                    element = self.shift_date_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shift_date_list[i] = element.to_alipay_dict()
            if hasattr(self.shift_date_list, 'to_alipay_dict'):
                params['shift_date_list'] = self.shift_date_list.to_alipay_dict()
            else:
                params['shift_date_list'] = self.shift_date_list
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.work_schedule_pids:
            if isinstance(self.work_schedule_pids, list):
                for i in range(0, len(self.work_schedule_pids)):
                    element = self.work_schedule_pids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_schedule_pids[i] = element.to_alipay_dict()
            if hasattr(self.work_schedule_pids, 'to_alipay_dict'):
                params['work_schedule_pids'] = self.work_schedule_pids.to_alipay_dict()
            else:
                params['work_schedule_pids'] = self.work_schedule_pids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceCloudbusScheduletaskshiftAddModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'cycle_cnt' in d:
            o.cycle_cnt = d['cycle_cnt']
        if 'driver_cnt' in d:
            o.driver_cnt = d['driver_cnt']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'shift_date_list' in d:
            o.shift_date_list = d['shift_date_list']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'work_schedule_pids' in d:
            o.work_schedule_pids = d['work_schedule_pids']
        return o



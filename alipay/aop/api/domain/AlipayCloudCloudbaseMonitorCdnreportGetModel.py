#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseMonitorCdnreportGetModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._domain_names = None
        self._end_time = None
        self._report_type = None
        self._start_time = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def domain_names(self):
        return self._domain_names

    @domain_names.setter
    def domain_names(self, value):
        if isinstance(value, list):
            self._domain_names = list()
            for i in value:
                self._domain_names.append(i)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.domain_names:
            if isinstance(self.domain_names, list):
                for i in range(0, len(self.domain_names)):
                    element = self.domain_names[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.domain_names[i] = element.to_alipay_dict()
            if hasattr(self.domain_names, 'to_alipay_dict'):
                params['domain_names'] = self.domain_names.to_alipay_dict()
            else:
                params['domain_names'] = self.domain_names
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseMonitorCdnreportGetModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'domain_names' in d:
            o.domain_names = d['domain_names']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'report_type' in d:
            o.report_type = d['report_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o



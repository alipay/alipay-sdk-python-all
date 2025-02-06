#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NSalesSubActivity import NSalesSubActivity


class NSalesActivity(object):

    def __init__(self):
        self._activity_dvc_sn = None
        self._activity_id = None
        self._activity_type = None
        self._create_time = None
        self._end_time = None
        self._period_list = None
        self._skip_dates = None
        self._start_time = None
        self._status = None

    @property
    def activity_dvc_sn(self):
        return self._activity_dvc_sn

    @activity_dvc_sn.setter
    def activity_dvc_sn(self, value):
        self._activity_dvc_sn = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def period_list(self):
        return self._period_list

    @period_list.setter
    def period_list(self, value):
        if isinstance(value, list):
            self._period_list = list()
            for i in value:
                if isinstance(i, NSalesSubActivity):
                    self._period_list.append(i)
                else:
                    self._period_list.append(NSalesSubActivity.from_alipay_dict(i))
    @property
    def skip_dates(self):
        return self._skip_dates

    @skip_dates.setter
    def skip_dates(self, value):
        if isinstance(value, list):
            self._skip_dates = list()
            for i in value:
                self._skip_dates.append(i)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_dvc_sn:
            if hasattr(self.activity_dvc_sn, 'to_alipay_dict'):
                params['activity_dvc_sn'] = self.activity_dvc_sn.to_alipay_dict()
            else:
                params['activity_dvc_sn'] = self.activity_dvc_sn
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.period_list:
            if isinstance(self.period_list, list):
                for i in range(0, len(self.period_list)):
                    element = self.period_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.period_list[i] = element.to_alipay_dict()
            if hasattr(self.period_list, 'to_alipay_dict'):
                params['period_list'] = self.period_list.to_alipay_dict()
            else:
                params['period_list'] = self.period_list
        if self.skip_dates:
            if isinstance(self.skip_dates, list):
                for i in range(0, len(self.skip_dates)):
                    element = self.skip_dates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skip_dates[i] = element.to_alipay_dict()
            if hasattr(self.skip_dates, 'to_alipay_dict'):
                params['skip_dates'] = self.skip_dates.to_alipay_dict()
            else:
                params['skip_dates'] = self.skip_dates
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NSalesActivity()
        if 'activity_dvc_sn' in d:
            o.activity_dvc_sn = d['activity_dvc_sn']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'period_list' in d:
            o.period_list = d['period_list']
        if 'skip_dates' in d:
            o.skip_dates = d['skip_dates']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o



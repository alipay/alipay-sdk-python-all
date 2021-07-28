#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StressRequestItem import StressRequestItem


class AlipayEbppStressHeartbeatUploadModel(object):

    def __init__(self):
        self._exception = None
        self._job_id = None
        self._machine_status = None
        self._report_detail = None
        self._report_time = None
        self._task_id = None
        self._total_time = None

    @property
    def exception(self):
        return self._exception

    @exception.setter
    def exception(self, value):
        self._exception = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def machine_status(self):
        return self._machine_status

    @machine_status.setter
    def machine_status(self, value):
        self._machine_status = value
    @property
    def report_detail(self):
        return self._report_detail

    @report_detail.setter
    def report_detail(self, value):
        if isinstance(value, list):
            self._report_detail = list()
            for i in value:
                if isinstance(i, StressRequestItem):
                    self._report_detail.append(i)
                else:
                    self._report_detail.append(StressRequestItem.from_alipay_dict(i))
    @property
    def report_time(self):
        return self._report_time

    @report_time.setter
    def report_time(self, value):
        self._report_time = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def total_time(self):
        return self._total_time

    @total_time.setter
    def total_time(self, value):
        self._total_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.exception:
            if hasattr(self.exception, 'to_alipay_dict'):
                params['exception'] = self.exception.to_alipay_dict()
            else:
                params['exception'] = self.exception
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.machine_status:
            if hasattr(self.machine_status, 'to_alipay_dict'):
                params['machine_status'] = self.machine_status.to_alipay_dict()
            else:
                params['machine_status'] = self.machine_status
        if self.report_detail:
            if isinstance(self.report_detail, list):
                for i in range(0, len(self.report_detail)):
                    element = self.report_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.report_detail[i] = element.to_alipay_dict()
            if hasattr(self.report_detail, 'to_alipay_dict'):
                params['report_detail'] = self.report_detail.to_alipay_dict()
            else:
                params['report_detail'] = self.report_detail
        if self.report_time:
            if hasattr(self.report_time, 'to_alipay_dict'):
                params['report_time'] = self.report_time.to_alipay_dict()
            else:
                params['report_time'] = self.report_time
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.total_time:
            if hasattr(self.total_time, 'to_alipay_dict'):
                params['total_time'] = self.total_time.to_alipay_dict()
            else:
                params['total_time'] = self.total_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppStressHeartbeatUploadModel()
        if 'exception' in d:
            o.exception = d['exception']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'machine_status' in d:
            o.machine_status = d['machine_status']
        if 'report_detail' in d:
            o.report_detail = d['report_detail']
        if 'report_time' in d:
            o.report_time = d['report_time']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'total_time' in d:
            o.total_time = d['total_time']
        return o



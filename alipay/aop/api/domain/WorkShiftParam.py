#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WorkShiftParam(object):

    def __init__(self):
        self._ext_param = None
        self._optimize_type = None
        self._work_schedule_service_task_id = None
        self._work_shift_date = None

    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def optimize_type(self):
        return self._optimize_type

    @optimize_type.setter
    def optimize_type(self, value):
        self._optimize_type = value
    @property
    def work_schedule_service_task_id(self):
        return self._work_schedule_service_task_id

    @work_schedule_service_task_id.setter
    def work_schedule_service_task_id(self, value):
        self._work_schedule_service_task_id = value
    @property
    def work_shift_date(self):
        return self._work_shift_date

    @work_shift_date.setter
    def work_shift_date(self, value):
        self._work_shift_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.optimize_type:
            if hasattr(self.optimize_type, 'to_alipay_dict'):
                params['optimize_type'] = self.optimize_type.to_alipay_dict()
            else:
                params['optimize_type'] = self.optimize_type
        if self.work_schedule_service_task_id:
            if hasattr(self.work_schedule_service_task_id, 'to_alipay_dict'):
                params['work_schedule_service_task_id'] = self.work_schedule_service_task_id.to_alipay_dict()
            else:
                params['work_schedule_service_task_id'] = self.work_schedule_service_task_id
        if self.work_shift_date:
            if hasattr(self.work_shift_date, 'to_alipay_dict'):
                params['work_shift_date'] = self.work_shift_date.to_alipay_dict()
            else:
                params['work_shift_date'] = self.work_shift_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorkShiftParam()
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'optimize_type' in d:
            o.optimize_type = d['optimize_type']
        if 'work_schedule_service_task_id' in d:
            o.work_schedule_service_task_id = d['work_schedule_service_task_id']
        if 'work_shift_date' in d:
            o.work_shift_date = d['work_shift_date']
        return o



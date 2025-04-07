#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryRecruitAttendanceSyncModel(object):

    def __init__(self):
        self._attendance_type = None
        self._clock_in_real_time = None
        self._clock_in_status = None
        self._clock_in_time = None
        self._clock_out_real_time = None
        self._clock_out_status = None
        self._clock_out_time = None
        self._out_apply_id = None
        self._out_attendance_id = None
        self._out_job_id = None
        self._out_user_id = None
        self._source = None

    @property
    def attendance_type(self):
        return self._attendance_type

    @attendance_type.setter
    def attendance_type(self, value):
        self._attendance_type = value
    @property
    def clock_in_real_time(self):
        return self._clock_in_real_time

    @clock_in_real_time.setter
    def clock_in_real_time(self, value):
        self._clock_in_real_time = value
    @property
    def clock_in_status(self):
        return self._clock_in_status

    @clock_in_status.setter
    def clock_in_status(self, value):
        self._clock_in_status = value
    @property
    def clock_in_time(self):
        return self._clock_in_time

    @clock_in_time.setter
    def clock_in_time(self, value):
        self._clock_in_time = value
    @property
    def clock_out_real_time(self):
        return self._clock_out_real_time

    @clock_out_real_time.setter
    def clock_out_real_time(self, value):
        self._clock_out_real_time = value
    @property
    def clock_out_status(self):
        return self._clock_out_status

    @clock_out_status.setter
    def clock_out_status(self, value):
        self._clock_out_status = value
    @property
    def clock_out_time(self):
        return self._clock_out_time

    @clock_out_time.setter
    def clock_out_time(self, value):
        self._clock_out_time = value
    @property
    def out_apply_id(self):
        return self._out_apply_id

    @out_apply_id.setter
    def out_apply_id(self, value):
        self._out_apply_id = value
    @property
    def out_attendance_id(self):
        return self._out_attendance_id

    @out_attendance_id.setter
    def out_attendance_id(self, value):
        self._out_attendance_id = value
    @property
    def out_job_id(self):
        return self._out_job_id

    @out_job_id.setter
    def out_job_id(self, value):
        self._out_job_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.attendance_type:
            if hasattr(self.attendance_type, 'to_alipay_dict'):
                params['attendance_type'] = self.attendance_type.to_alipay_dict()
            else:
                params['attendance_type'] = self.attendance_type
        if self.clock_in_real_time:
            if hasattr(self.clock_in_real_time, 'to_alipay_dict'):
                params['clock_in_real_time'] = self.clock_in_real_time.to_alipay_dict()
            else:
                params['clock_in_real_time'] = self.clock_in_real_time
        if self.clock_in_status:
            if hasattr(self.clock_in_status, 'to_alipay_dict'):
                params['clock_in_status'] = self.clock_in_status.to_alipay_dict()
            else:
                params['clock_in_status'] = self.clock_in_status
        if self.clock_in_time:
            if hasattr(self.clock_in_time, 'to_alipay_dict'):
                params['clock_in_time'] = self.clock_in_time.to_alipay_dict()
            else:
                params['clock_in_time'] = self.clock_in_time
        if self.clock_out_real_time:
            if hasattr(self.clock_out_real_time, 'to_alipay_dict'):
                params['clock_out_real_time'] = self.clock_out_real_time.to_alipay_dict()
            else:
                params['clock_out_real_time'] = self.clock_out_real_time
        if self.clock_out_status:
            if hasattr(self.clock_out_status, 'to_alipay_dict'):
                params['clock_out_status'] = self.clock_out_status.to_alipay_dict()
            else:
                params['clock_out_status'] = self.clock_out_status
        if self.clock_out_time:
            if hasattr(self.clock_out_time, 'to_alipay_dict'):
                params['clock_out_time'] = self.clock_out_time.to_alipay_dict()
            else:
                params['clock_out_time'] = self.clock_out_time
        if self.out_apply_id:
            if hasattr(self.out_apply_id, 'to_alipay_dict'):
                params['out_apply_id'] = self.out_apply_id.to_alipay_dict()
            else:
                params['out_apply_id'] = self.out_apply_id
        if self.out_attendance_id:
            if hasattr(self.out_attendance_id, 'to_alipay_dict'):
                params['out_attendance_id'] = self.out_attendance_id.to_alipay_dict()
            else:
                params['out_attendance_id'] = self.out_attendance_id
        if self.out_job_id:
            if hasattr(self.out_job_id, 'to_alipay_dict'):
                params['out_job_id'] = self.out_job_id.to_alipay_dict()
            else:
                params['out_job_id'] = self.out_job_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryRecruitAttendanceSyncModel()
        if 'attendance_type' in d:
            o.attendance_type = d['attendance_type']
        if 'clock_in_real_time' in d:
            o.clock_in_real_time = d['clock_in_real_time']
        if 'clock_in_status' in d:
            o.clock_in_status = d['clock_in_status']
        if 'clock_in_time' in d:
            o.clock_in_time = d['clock_in_time']
        if 'clock_out_real_time' in d:
            o.clock_out_real_time = d['clock_out_real_time']
        if 'clock_out_status' in d:
            o.clock_out_status = d['clock_out_status']
        if 'clock_out_time' in d:
            o.clock_out_time = d['clock_out_time']
        if 'out_apply_id' in d:
            o.out_apply_id = d['out_apply_id']
        if 'out_attendance_id' in d:
            o.out_attendance_id = d['out_attendance_id']
        if 'out_job_id' in d:
            o.out_job_id = d['out_job_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'source' in d:
            o.source = d['source']
        return o



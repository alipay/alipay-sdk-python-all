#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SportsRunRecord(object):

    def __init__(self):
        self._department_name = None
        self._employee_no = None
        self._end_time = None
        self._gender = None
        self._is_valid = None
        self._is_valid_name = None
        self._mark = None
        self._name = None
        self._record_id = None
        self._run_distance = None
        self._run_duration = None
        self._run_speed = None
        self._start_time = None
        self._step_frequency = None

    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value):
        self._is_valid = value
    @property
    def is_valid_name(self):
        return self._is_valid_name

    @is_valid_name.setter
    def is_valid_name(self, value):
        self._is_valid_name = value
    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        self._mark = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def run_distance(self):
        return self._run_distance

    @run_distance.setter
    def run_distance(self, value):
        self._run_distance = value
    @property
    def run_duration(self):
        return self._run_duration

    @run_duration.setter
    def run_duration(self, value):
        self._run_duration = value
    @property
    def run_speed(self):
        return self._run_speed

    @run_speed.setter
    def run_speed(self, value):
        self._run_speed = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def step_frequency(self):
        return self._step_frequency

    @step_frequency.setter
    def step_frequency(self, value):
        self._step_frequency = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.is_valid:
            if hasattr(self.is_valid, 'to_alipay_dict'):
                params['is_valid'] = self.is_valid.to_alipay_dict()
            else:
                params['is_valid'] = self.is_valid
        if self.is_valid_name:
            if hasattr(self.is_valid_name, 'to_alipay_dict'):
                params['is_valid_name'] = self.is_valid_name.to_alipay_dict()
            else:
                params['is_valid_name'] = self.is_valid_name
        if self.mark:
            if hasattr(self.mark, 'to_alipay_dict'):
                params['mark'] = self.mark.to_alipay_dict()
            else:
                params['mark'] = self.mark
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.run_distance:
            if hasattr(self.run_distance, 'to_alipay_dict'):
                params['run_distance'] = self.run_distance.to_alipay_dict()
            else:
                params['run_distance'] = self.run_distance
        if self.run_duration:
            if hasattr(self.run_duration, 'to_alipay_dict'):
                params['run_duration'] = self.run_duration.to_alipay_dict()
            else:
                params['run_duration'] = self.run_duration
        if self.run_speed:
            if hasattr(self.run_speed, 'to_alipay_dict'):
                params['run_speed'] = self.run_speed.to_alipay_dict()
            else:
                params['run_speed'] = self.run_speed
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.step_frequency:
            if hasattr(self.step_frequency, 'to_alipay_dict'):
                params['step_frequency'] = self.step_frequency.to_alipay_dict()
            else:
                params['step_frequency'] = self.step_frequency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SportsRunRecord()
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'gender' in d:
            o.gender = d['gender']
        if 'is_valid' in d:
            o.is_valid = d['is_valid']
        if 'is_valid_name' in d:
            o.is_valid_name = d['is_valid_name']
        if 'mark' in d:
            o.mark = d['mark']
        if 'name' in d:
            o.name = d['name']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'run_distance' in d:
            o.run_distance = d['run_distance']
        if 'run_duration' in d:
            o.run_duration = d['run_duration']
        if 'run_speed' in d:
            o.run_speed = d['run_speed']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'step_frequency' in d:
            o.step_frequency = d['step_frequency']
        return o



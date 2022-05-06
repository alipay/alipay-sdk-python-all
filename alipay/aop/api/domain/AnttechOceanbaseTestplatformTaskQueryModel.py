#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseTestplatformTaskQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._palyer = None
        self._run_task_retry = None
        self._run_task_time_out_minutes = None
        self._start_time = None
        self._test_cases = None
        self._test_info = None
        self._test_suite = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def palyer(self):
        return self._palyer

    @palyer.setter
    def palyer(self, value):
        self._palyer = value
    @property
    def run_task_retry(self):
        return self._run_task_retry

    @run_task_retry.setter
    def run_task_retry(self, value):
        self._run_task_retry = value
    @property
    def run_task_time_out_minutes(self):
        return self._run_task_time_out_minutes

    @run_task_time_out_minutes.setter
    def run_task_time_out_minutes(self, value):
        self._run_task_time_out_minutes = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def test_cases(self):
        return self._test_cases

    @test_cases.setter
    def test_cases(self, value):
        self._test_cases = value
    @property
    def test_info(self):
        return self._test_info

    @test_info.setter
    def test_info(self, value):
        self._test_info = value
    @property
    def test_suite(self):
        return self._test_suite

    @test_suite.setter
    def test_suite(self, value):
        self._test_suite = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.palyer:
            if hasattr(self.palyer, 'to_alipay_dict'):
                params['palyer'] = self.palyer.to_alipay_dict()
            else:
                params['palyer'] = self.palyer
        if self.run_task_retry:
            if hasattr(self.run_task_retry, 'to_alipay_dict'):
                params['run_task_retry'] = self.run_task_retry.to_alipay_dict()
            else:
                params['run_task_retry'] = self.run_task_retry
        if self.run_task_time_out_minutes:
            if hasattr(self.run_task_time_out_minutes, 'to_alipay_dict'):
                params['run_task_time_out_minutes'] = self.run_task_time_out_minutes.to_alipay_dict()
            else:
                params['run_task_time_out_minutes'] = self.run_task_time_out_minutes
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.test_cases:
            if hasattr(self.test_cases, 'to_alipay_dict'):
                params['test_cases'] = self.test_cases.to_alipay_dict()
            else:
                params['test_cases'] = self.test_cases
        if self.test_info:
            if hasattr(self.test_info, 'to_alipay_dict'):
                params['test_info'] = self.test_info.to_alipay_dict()
            else:
                params['test_info'] = self.test_info
        if self.test_suite:
            if hasattr(self.test_suite, 'to_alipay_dict'):
                params['test_suite'] = self.test_suite.to_alipay_dict()
            else:
                params['test_suite'] = self.test_suite
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseTestplatformTaskQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'palyer' in d:
            o.palyer = d['palyer']
        if 'run_task_retry' in d:
            o.run_task_retry = d['run_task_retry']
        if 'run_task_time_out_minutes' in d:
            o.run_task_time_out_minutes = d['run_task_time_out_minutes']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'test_cases' in d:
            o.test_cases = d['test_cases']
        if 'test_info' in d:
            o.test_info = d['test_info']
        if 'test_suite' in d:
            o.test_suite = d['test_suite']
        return o



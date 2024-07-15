#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JobIntentionDetail(object):

    def __init__(self):
        self._city_code = None
        self._job_type = None
        self._salary_max = None
        self._salary_min = None
        self._work_nature = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, value):
        self._job_type = value
    @property
    def salary_max(self):
        return self._salary_max

    @salary_max.setter
    def salary_max(self, value):
        self._salary_max = value
    @property
    def salary_min(self):
        return self._salary_min

    @salary_min.setter
    def salary_min(self, value):
        self._salary_min = value
    @property
    def work_nature(self):
        return self._work_nature

    @work_nature.setter
    def work_nature(self, value):
        self._work_nature = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.job_type:
            if hasattr(self.job_type, 'to_alipay_dict'):
                params['job_type'] = self.job_type.to_alipay_dict()
            else:
                params['job_type'] = self.job_type
        if self.salary_max:
            if hasattr(self.salary_max, 'to_alipay_dict'):
                params['salary_max'] = self.salary_max.to_alipay_dict()
            else:
                params['salary_max'] = self.salary_max
        if self.salary_min:
            if hasattr(self.salary_min, 'to_alipay_dict'):
                params['salary_min'] = self.salary_min.to_alipay_dict()
            else:
                params['salary_min'] = self.salary_min
        if self.work_nature:
            if hasattr(self.work_nature, 'to_alipay_dict'):
                params['work_nature'] = self.work_nature.to_alipay_dict()
            else:
                params['work_nature'] = self.work_nature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JobIntentionDetail()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'job_type' in d:
            o.job_type = d['job_type']
        if 'salary_max' in d:
            o.salary_max = d['salary_max']
        if 'salary_min' in d:
            o.salary_min = d['salary_min']
        if 'work_nature' in d:
            o.work_nature = d['work_nature']
        return o



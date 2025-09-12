#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserIntentionInfo(object):

    def __init__(self):
        self._city_code = None
        self._city_name = None
        self._expect_job_code = None
        self._expect_job_type = None
        self._expect_salary_max = None
        self._expect_salary_min = None
        self._gmt_create = None
        self._gmt_modified = None
        self._work_nature = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def expect_job_code(self):
        return self._expect_job_code

    @expect_job_code.setter
    def expect_job_code(self, value):
        self._expect_job_code = value
    @property
    def expect_job_type(self):
        return self._expect_job_type

    @expect_job_type.setter
    def expect_job_type(self, value):
        self._expect_job_type = value
    @property
    def expect_salary_max(self):
        return self._expect_salary_max

    @expect_salary_max.setter
    def expect_salary_max(self, value):
        self._expect_salary_max = value
    @property
    def expect_salary_min(self):
        return self._expect_salary_min

    @expect_salary_min.setter
    def expect_salary_min(self, value):
        self._expect_salary_min = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
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
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.expect_job_code:
            if hasattr(self.expect_job_code, 'to_alipay_dict'):
                params['expect_job_code'] = self.expect_job_code.to_alipay_dict()
            else:
                params['expect_job_code'] = self.expect_job_code
        if self.expect_job_type:
            if hasattr(self.expect_job_type, 'to_alipay_dict'):
                params['expect_job_type'] = self.expect_job_type.to_alipay_dict()
            else:
                params['expect_job_type'] = self.expect_job_type
        if self.expect_salary_max:
            if hasattr(self.expect_salary_max, 'to_alipay_dict'):
                params['expect_salary_max'] = self.expect_salary_max.to_alipay_dict()
            else:
                params['expect_salary_max'] = self.expect_salary_max
        if self.expect_salary_min:
            if hasattr(self.expect_salary_min, 'to_alipay_dict'):
                params['expect_salary_min'] = self.expect_salary_min.to_alipay_dict()
            else:
                params['expect_salary_min'] = self.expect_salary_min
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
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
        o = UserIntentionInfo()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'expect_job_code' in d:
            o.expect_job_code = d['expect_job_code']
        if 'expect_job_type' in d:
            o.expect_job_type = d['expect_job_type']
        if 'expect_salary_max' in d:
            o.expect_salary_max = d['expect_salary_max']
        if 'expect_salary_min' in d:
            o.expect_salary_min = d['expect_salary_min']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'work_nature' in d:
            o.work_nature = d['work_nature']
        return o



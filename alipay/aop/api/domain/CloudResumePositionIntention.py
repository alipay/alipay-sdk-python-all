#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudResumePositionIntention(object):

    def __init__(self):
        self._intention_city = None
        self._job_id = None
        self._job_name = None
        self._profession_id = None
        self._profession_name = None
        self._salary_max = None
        self._salary_min = None
        self._salary_unit = None
        self._work_property = None

    @property
    def intention_city(self):
        return self._intention_city

    @intention_city.setter
    def intention_city(self, value):
        self._intention_city = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def profession_id(self):
        return self._profession_id

    @profession_id.setter
    def profession_id(self, value):
        self._profession_id = value
    @property
    def profession_name(self):
        return self._profession_name

    @profession_name.setter
    def profession_name(self, value):
        self._profession_name = value
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
    def salary_unit(self):
        return self._salary_unit

    @salary_unit.setter
    def salary_unit(self, value):
        self._salary_unit = value
    @property
    def work_property(self):
        return self._work_property

    @work_property.setter
    def work_property(self, value):
        self._work_property = value


    def to_alipay_dict(self):
        params = dict()
        if self.intention_city:
            if hasattr(self.intention_city, 'to_alipay_dict'):
                params['intention_city'] = self.intention_city.to_alipay_dict()
            else:
                params['intention_city'] = self.intention_city
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.profession_id:
            if hasattr(self.profession_id, 'to_alipay_dict'):
                params['profession_id'] = self.profession_id.to_alipay_dict()
            else:
                params['profession_id'] = self.profession_id
        if self.profession_name:
            if hasattr(self.profession_name, 'to_alipay_dict'):
                params['profession_name'] = self.profession_name.to_alipay_dict()
            else:
                params['profession_name'] = self.profession_name
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
        if self.salary_unit:
            if hasattr(self.salary_unit, 'to_alipay_dict'):
                params['salary_unit'] = self.salary_unit.to_alipay_dict()
            else:
                params['salary_unit'] = self.salary_unit
        if self.work_property:
            if hasattr(self.work_property, 'to_alipay_dict'):
                params['work_property'] = self.work_property.to_alipay_dict()
            else:
                params['work_property'] = self.work_property
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudResumePositionIntention()
        if 'intention_city' in d:
            o.intention_city = d['intention_city']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'profession_id' in d:
            o.profession_id = d['profession_id']
        if 'profession_name' in d:
            o.profession_name = d['profession_name']
        if 'salary_max' in d:
            o.salary_max = d['salary_max']
        if 'salary_min' in d:
            o.salary_min = d['salary_min']
        if 'salary_unit' in d:
            o.salary_unit = d['salary_unit']
        if 'work_property' in d:
            o.work_property = d['work_property']
        return o



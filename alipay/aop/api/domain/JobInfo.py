#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JobInfo(object):

    def __init__(self):
        self._address = None
        self._age_range = None
        self._apply_status = None
        self._bonus_desc = None
        self._hot_job = None
        self._introduction = None
        self._job_id = None
        self._job_key_tags = None
        self._job_name = None
        self._job_supplier_code = None
        self._job_time_type = None
        self._post = None
        self._recruit_condition = None
        self._salary = None
        self._salary_settlement_desc = None
        self._sex_range = None
        self._simple_desc = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def age_range(self):
        return self._age_range

    @age_range.setter
    def age_range(self, value):
        self._age_range = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def bonus_desc(self):
        return self._bonus_desc

    @bonus_desc.setter
    def bonus_desc(self, value):
        self._bonus_desc = value
    @property
    def hot_job(self):
        return self._hot_job

    @hot_job.setter
    def hot_job(self, value):
        self._hot_job = value
    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def job_key_tags(self):
        return self._job_key_tags

    @job_key_tags.setter
    def job_key_tags(self, value):
        self._job_key_tags = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def job_supplier_code(self):
        return self._job_supplier_code

    @job_supplier_code.setter
    def job_supplier_code(self, value):
        self._job_supplier_code = value
    @property
    def job_time_type(self):
        return self._job_time_type

    @job_time_type.setter
    def job_time_type(self, value):
        self._job_time_type = value
    @property
    def post(self):
        return self._post

    @post.setter
    def post(self, value):
        self._post = value
    @property
    def recruit_condition(self):
        return self._recruit_condition

    @recruit_condition.setter
    def recruit_condition(self, value):
        self._recruit_condition = value
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
    @property
    def salary_settlement_desc(self):
        return self._salary_settlement_desc

    @salary_settlement_desc.setter
    def salary_settlement_desc(self, value):
        self._salary_settlement_desc = value
    @property
    def sex_range(self):
        return self._sex_range

    @sex_range.setter
    def sex_range(self, value):
        self._sex_range = value
    @property
    def simple_desc(self):
        return self._simple_desc

    @simple_desc.setter
    def simple_desc(self, value):
        self._simple_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.age_range:
            if hasattr(self.age_range, 'to_alipay_dict'):
                params['age_range'] = self.age_range.to_alipay_dict()
            else:
                params['age_range'] = self.age_range
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.bonus_desc:
            if hasattr(self.bonus_desc, 'to_alipay_dict'):
                params['bonus_desc'] = self.bonus_desc.to_alipay_dict()
            else:
                params['bonus_desc'] = self.bonus_desc
        if self.hot_job:
            if hasattr(self.hot_job, 'to_alipay_dict'):
                params['hot_job'] = self.hot_job.to_alipay_dict()
            else:
                params['hot_job'] = self.hot_job
        if self.introduction:
            if hasattr(self.introduction, 'to_alipay_dict'):
                params['introduction'] = self.introduction.to_alipay_dict()
            else:
                params['introduction'] = self.introduction
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.job_key_tags:
            if hasattr(self.job_key_tags, 'to_alipay_dict'):
                params['job_key_tags'] = self.job_key_tags.to_alipay_dict()
            else:
                params['job_key_tags'] = self.job_key_tags
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.job_supplier_code:
            if hasattr(self.job_supplier_code, 'to_alipay_dict'):
                params['job_supplier_code'] = self.job_supplier_code.to_alipay_dict()
            else:
                params['job_supplier_code'] = self.job_supplier_code
        if self.job_time_type:
            if hasattr(self.job_time_type, 'to_alipay_dict'):
                params['job_time_type'] = self.job_time_type.to_alipay_dict()
            else:
                params['job_time_type'] = self.job_time_type
        if self.post:
            if hasattr(self.post, 'to_alipay_dict'):
                params['post'] = self.post.to_alipay_dict()
            else:
                params['post'] = self.post
        if self.recruit_condition:
            if hasattr(self.recruit_condition, 'to_alipay_dict'):
                params['recruit_condition'] = self.recruit_condition.to_alipay_dict()
            else:
                params['recruit_condition'] = self.recruit_condition
        if self.salary:
            if hasattr(self.salary, 'to_alipay_dict'):
                params['salary'] = self.salary.to_alipay_dict()
            else:
                params['salary'] = self.salary
        if self.salary_settlement_desc:
            if hasattr(self.salary_settlement_desc, 'to_alipay_dict'):
                params['salary_settlement_desc'] = self.salary_settlement_desc.to_alipay_dict()
            else:
                params['salary_settlement_desc'] = self.salary_settlement_desc
        if self.sex_range:
            if hasattr(self.sex_range, 'to_alipay_dict'):
                params['sex_range'] = self.sex_range.to_alipay_dict()
            else:
                params['sex_range'] = self.sex_range
        if self.simple_desc:
            if hasattr(self.simple_desc, 'to_alipay_dict'):
                params['simple_desc'] = self.simple_desc.to_alipay_dict()
            else:
                params['simple_desc'] = self.simple_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JobInfo()
        if 'address' in d:
            o.address = d['address']
        if 'age_range' in d:
            o.age_range = d['age_range']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'bonus_desc' in d:
            o.bonus_desc = d['bonus_desc']
        if 'hot_job' in d:
            o.hot_job = d['hot_job']
        if 'introduction' in d:
            o.introduction = d['introduction']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_key_tags' in d:
            o.job_key_tags = d['job_key_tags']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'job_supplier_code' in d:
            o.job_supplier_code = d['job_supplier_code']
        if 'job_time_type' in d:
            o.job_time_type = d['job_time_type']
        if 'post' in d:
            o.post = d['post']
        if 'recruit_condition' in d:
            o.recruit_condition = d['recruit_condition']
        if 'salary' in d:
            o.salary = d['salary']
        if 'salary_settlement_desc' in d:
            o.salary_settlement_desc = d['salary_settlement_desc']
        if 'sex_range' in d:
            o.sex_range = d['sex_range']
        if 'simple_desc' in d:
            o.simple_desc = d['simple_desc']
        return o



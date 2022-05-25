#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudResumeWorkExperience(object):

    def __init__(self):
        self._company_name = None
        self._job_id = None
        self._job_name = None
        self._profession_id = None
        self._profession_name = None
        self._work_desc = None
        self._work_end_time = None
        self._work_start_time = None

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
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
    def work_desc(self):
        return self._work_desc

    @work_desc.setter
    def work_desc(self, value):
        self._work_desc = value
    @property
    def work_end_time(self):
        return self._work_end_time

    @work_end_time.setter
    def work_end_time(self, value):
        self._work_end_time = value
    @property
    def work_start_time(self):
        return self._work_start_time

    @work_start_time.setter
    def work_start_time(self, value):
        self._work_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
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
        if self.work_desc:
            if hasattr(self.work_desc, 'to_alipay_dict'):
                params['work_desc'] = self.work_desc.to_alipay_dict()
            else:
                params['work_desc'] = self.work_desc
        if self.work_end_time:
            if hasattr(self.work_end_time, 'to_alipay_dict'):
                params['work_end_time'] = self.work_end_time.to_alipay_dict()
            else:
                params['work_end_time'] = self.work_end_time
        if self.work_start_time:
            if hasattr(self.work_start_time, 'to_alipay_dict'):
                params['work_start_time'] = self.work_start_time.to_alipay_dict()
            else:
                params['work_start_time'] = self.work_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudResumeWorkExperience()
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'profession_id' in d:
            o.profession_id = d['profession_id']
        if 'profession_name' in d:
            o.profession_name = d['profession_name']
        if 'work_desc' in d:
            o.work_desc = d['work_desc']
        if 'work_end_time' in d:
            o.work_end_time = d['work_end_time']
        if 'work_start_time' in d:
            o.work_start_time = d['work_start_time']
        return o



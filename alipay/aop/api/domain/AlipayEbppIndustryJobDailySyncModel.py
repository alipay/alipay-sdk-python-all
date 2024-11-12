#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JobAddress import JobAddress


class AlipayEbppIndustryJobDailySyncModel(object):

    def __init__(self):
        self._academic_require = None
        self._address = None
        self._age = None
        self._count = None
        self._employer_name = None
        self._employer_type = None
        self._expired_date = None
        self._gender = None
        self._hire_status = None
        self._job_detail = None
        self._job_detail_url = None
        self._job_features = None
        self._job_name = None
        self._job_requires = None
        self._job_type = None
        self._out_job_id = None
        self._part_time_mode = None
        self._pay_period = None
        self._salary = None
        self._source = None
        self._start_date = None
        self._work_interval_end = None
        self._work_interval_start = None
        self._work_online = None
        self._working_years = None

    @property
    def academic_require(self):
        return self._academic_require

    @academic_require.setter
    def academic_require(self, value):
        self._academic_require = value
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, JobAddress):
            self._address = value
        else:
            self._address = JobAddress.from_alipay_dict(value)
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def employer_name(self):
        return self._employer_name

    @employer_name.setter
    def employer_name(self, value):
        self._employer_name = value
    @property
    def employer_type(self):
        return self._employer_type

    @employer_type.setter
    def employer_type(self, value):
        self._employer_type = value
    @property
    def expired_date(self):
        return self._expired_date

    @expired_date.setter
    def expired_date(self, value):
        self._expired_date = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def hire_status(self):
        return self._hire_status

    @hire_status.setter
    def hire_status(self, value):
        self._hire_status = value
    @property
    def job_detail(self):
        return self._job_detail

    @job_detail.setter
    def job_detail(self, value):
        self._job_detail = value
    @property
    def job_detail_url(self):
        return self._job_detail_url

    @job_detail_url.setter
    def job_detail_url(self, value):
        self._job_detail_url = value
    @property
    def job_features(self):
        return self._job_features

    @job_features.setter
    def job_features(self, value):
        if isinstance(value, list):
            self._job_features = list()
            for i in value:
                self._job_features.append(i)
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def job_requires(self):
        return self._job_requires

    @job_requires.setter
    def job_requires(self, value):
        if isinstance(value, list):
            self._job_requires = list()
            for i in value:
                self._job_requires.append(i)
    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, value):
        self._job_type = value
    @property
    def out_job_id(self):
        return self._out_job_id

    @out_job_id.setter
    def out_job_id(self, value):
        self._out_job_id = value
    @property
    def part_time_mode(self):
        return self._part_time_mode

    @part_time_mode.setter
    def part_time_mode(self, value):
        self._part_time_mode = value
    @property
    def pay_period(self):
        return self._pay_period

    @pay_period.setter
    def pay_period(self, value):
        self._pay_period = value
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def work_interval_end(self):
        return self._work_interval_end

    @work_interval_end.setter
    def work_interval_end(self, value):
        self._work_interval_end = value
    @property
    def work_interval_start(self):
        return self._work_interval_start

    @work_interval_start.setter
    def work_interval_start(self, value):
        self._work_interval_start = value
    @property
    def work_online(self):
        return self._work_online

    @work_online.setter
    def work_online(self, value):
        self._work_online = value
    @property
    def working_years(self):
        return self._working_years

    @working_years.setter
    def working_years(self, value):
        self._working_years = value


    def to_alipay_dict(self):
        params = dict()
        if self.academic_require:
            if hasattr(self.academic_require, 'to_alipay_dict'):
                params['academic_require'] = self.academic_require.to_alipay_dict()
            else:
                params['academic_require'] = self.academic_require
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.employer_name:
            if hasattr(self.employer_name, 'to_alipay_dict'):
                params['employer_name'] = self.employer_name.to_alipay_dict()
            else:
                params['employer_name'] = self.employer_name
        if self.employer_type:
            if hasattr(self.employer_type, 'to_alipay_dict'):
                params['employer_type'] = self.employer_type.to_alipay_dict()
            else:
                params['employer_type'] = self.employer_type
        if self.expired_date:
            if hasattr(self.expired_date, 'to_alipay_dict'):
                params['expired_date'] = self.expired_date.to_alipay_dict()
            else:
                params['expired_date'] = self.expired_date
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.hire_status:
            if hasattr(self.hire_status, 'to_alipay_dict'):
                params['hire_status'] = self.hire_status.to_alipay_dict()
            else:
                params['hire_status'] = self.hire_status
        if self.job_detail:
            if hasattr(self.job_detail, 'to_alipay_dict'):
                params['job_detail'] = self.job_detail.to_alipay_dict()
            else:
                params['job_detail'] = self.job_detail
        if self.job_detail_url:
            if hasattr(self.job_detail_url, 'to_alipay_dict'):
                params['job_detail_url'] = self.job_detail_url.to_alipay_dict()
            else:
                params['job_detail_url'] = self.job_detail_url
        if self.job_features:
            if isinstance(self.job_features, list):
                for i in range(0, len(self.job_features)):
                    element = self.job_features[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.job_features[i] = element.to_alipay_dict()
            if hasattr(self.job_features, 'to_alipay_dict'):
                params['job_features'] = self.job_features.to_alipay_dict()
            else:
                params['job_features'] = self.job_features
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.job_requires:
            if isinstance(self.job_requires, list):
                for i in range(0, len(self.job_requires)):
                    element = self.job_requires[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.job_requires[i] = element.to_alipay_dict()
            if hasattr(self.job_requires, 'to_alipay_dict'):
                params['job_requires'] = self.job_requires.to_alipay_dict()
            else:
                params['job_requires'] = self.job_requires
        if self.job_type:
            if hasattr(self.job_type, 'to_alipay_dict'):
                params['job_type'] = self.job_type.to_alipay_dict()
            else:
                params['job_type'] = self.job_type
        if self.out_job_id:
            if hasattr(self.out_job_id, 'to_alipay_dict'):
                params['out_job_id'] = self.out_job_id.to_alipay_dict()
            else:
                params['out_job_id'] = self.out_job_id
        if self.part_time_mode:
            if hasattr(self.part_time_mode, 'to_alipay_dict'):
                params['part_time_mode'] = self.part_time_mode.to_alipay_dict()
            else:
                params['part_time_mode'] = self.part_time_mode
        if self.pay_period:
            if hasattr(self.pay_period, 'to_alipay_dict'):
                params['pay_period'] = self.pay_period.to_alipay_dict()
            else:
                params['pay_period'] = self.pay_period
        if self.salary:
            if hasattr(self.salary, 'to_alipay_dict'):
                params['salary'] = self.salary.to_alipay_dict()
            else:
                params['salary'] = self.salary
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.work_interval_end:
            if hasattr(self.work_interval_end, 'to_alipay_dict'):
                params['work_interval_end'] = self.work_interval_end.to_alipay_dict()
            else:
                params['work_interval_end'] = self.work_interval_end
        if self.work_interval_start:
            if hasattr(self.work_interval_start, 'to_alipay_dict'):
                params['work_interval_start'] = self.work_interval_start.to_alipay_dict()
            else:
                params['work_interval_start'] = self.work_interval_start
        if self.work_online:
            if hasattr(self.work_online, 'to_alipay_dict'):
                params['work_online'] = self.work_online.to_alipay_dict()
            else:
                params['work_online'] = self.work_online
        if self.working_years:
            if hasattr(self.working_years, 'to_alipay_dict'):
                params['working_years'] = self.working_years.to_alipay_dict()
            else:
                params['working_years'] = self.working_years
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryJobDailySyncModel()
        if 'academic_require' in d:
            o.academic_require = d['academic_require']
        if 'address' in d:
            o.address = d['address']
        if 'age' in d:
            o.age = d['age']
        if 'count' in d:
            o.count = d['count']
        if 'employer_name' in d:
            o.employer_name = d['employer_name']
        if 'employer_type' in d:
            o.employer_type = d['employer_type']
        if 'expired_date' in d:
            o.expired_date = d['expired_date']
        if 'gender' in d:
            o.gender = d['gender']
        if 'hire_status' in d:
            o.hire_status = d['hire_status']
        if 'job_detail' in d:
            o.job_detail = d['job_detail']
        if 'job_detail_url' in d:
            o.job_detail_url = d['job_detail_url']
        if 'job_features' in d:
            o.job_features = d['job_features']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'job_requires' in d:
            o.job_requires = d['job_requires']
        if 'job_type' in d:
            o.job_type = d['job_type']
        if 'out_job_id' in d:
            o.out_job_id = d['out_job_id']
        if 'part_time_mode' in d:
            o.part_time_mode = d['part_time_mode']
        if 'pay_period' in d:
            o.pay_period = d['pay_period']
        if 'salary' in d:
            o.salary = d['salary']
        if 'source' in d:
            o.source = d['source']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'work_interval_end' in d:
            o.work_interval_end = d['work_interval_end']
        if 'work_interval_start' in d:
            o.work_interval_start = d['work_interval_start']
        if 'work_online' in d:
            o.work_online = d['work_online']
        if 'working_years' in d:
            o.working_years = d['working_years']
        return o



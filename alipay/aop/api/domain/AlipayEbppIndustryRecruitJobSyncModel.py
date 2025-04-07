#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JobAddress import JobAddress


class AlipayEbppIndustryRecruitJobSyncModel(object):

    def __init__(self):
        self._academic_require = None
        self._address_info = None
        self._age = None
        self._client_job_url = None
        self._employee_welfare = None
        self._employer_name = None
        self._employer_type = None
        self._gender = None
        self._graduation_time = None
        self._hire_open_id = None
        self._hire_status = None
        self._hire_user_id = None
        self._hire_user_mobile = None
        self._hire_user_name = None
        self._job_detail = None
        self._job_end_time = None
        self._job_name = None
        self._job_off_reason = None
        self._job_type = None
        self._out_hire_user_id = None
        self._out_job_id = None
        self._part_time_mode = None
        self._performance_bonus = None
        self._recruit_count = None
        self._salary_max = None
        self._salary_min = None
        self._salary_unit = None
        self._server_job_url = None
        self._source = None
        self._work_end_date = None
        self._work_end_time = None
        self._work_require = None
        self._work_start_date = None
        self._work_start_time = None
        self._working_years = None

    @property
    def academic_require(self):
        return self._academic_require

    @academic_require.setter
    def academic_require(self, value):
        self._academic_require = value
    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, JobAddress):
            self._address_info = value
        else:
            self._address_info = JobAddress.from_alipay_dict(value)
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def client_job_url(self):
        return self._client_job_url

    @client_job_url.setter
    def client_job_url(self, value):
        self._client_job_url = value
    @property
    def employee_welfare(self):
        return self._employee_welfare

    @employee_welfare.setter
    def employee_welfare(self, value):
        if isinstance(value, list):
            self._employee_welfare = list()
            for i in value:
                self._employee_welfare.append(i)
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
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def graduation_time(self):
        return self._graduation_time

    @graduation_time.setter
    def graduation_time(self, value):
        self._graduation_time = value
    @property
    def hire_open_id(self):
        return self._hire_open_id

    @hire_open_id.setter
    def hire_open_id(self, value):
        self._hire_open_id = value
    @property
    def hire_status(self):
        return self._hire_status

    @hire_status.setter
    def hire_status(self, value):
        self._hire_status = value
    @property
    def hire_user_id(self):
        return self._hire_user_id

    @hire_user_id.setter
    def hire_user_id(self, value):
        self._hire_user_id = value
    @property
    def hire_user_mobile(self):
        return self._hire_user_mobile

    @hire_user_mobile.setter
    def hire_user_mobile(self, value):
        self._hire_user_mobile = value
    @property
    def hire_user_name(self):
        return self._hire_user_name

    @hire_user_name.setter
    def hire_user_name(self, value):
        self._hire_user_name = value
    @property
    def job_detail(self):
        return self._job_detail

    @job_detail.setter
    def job_detail(self, value):
        self._job_detail = value
    @property
    def job_end_time(self):
        return self._job_end_time

    @job_end_time.setter
    def job_end_time(self, value):
        self._job_end_time = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def job_off_reason(self):
        return self._job_off_reason

    @job_off_reason.setter
    def job_off_reason(self, value):
        self._job_off_reason = value
    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, value):
        self._job_type = value
    @property
    def out_hire_user_id(self):
        return self._out_hire_user_id

    @out_hire_user_id.setter
    def out_hire_user_id(self, value):
        self._out_hire_user_id = value
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
    def performance_bonus(self):
        return self._performance_bonus

    @performance_bonus.setter
    def performance_bonus(self, value):
        self._performance_bonus = value
    @property
    def recruit_count(self):
        return self._recruit_count

    @recruit_count.setter
    def recruit_count(self, value):
        self._recruit_count = value
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
    def server_job_url(self):
        return self._server_job_url

    @server_job_url.setter
    def server_job_url(self, value):
        self._server_job_url = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def work_end_date(self):
        return self._work_end_date

    @work_end_date.setter
    def work_end_date(self, value):
        self._work_end_date = value
    @property
    def work_end_time(self):
        return self._work_end_time

    @work_end_time.setter
    def work_end_time(self, value):
        self._work_end_time = value
    @property
    def work_require(self):
        return self._work_require

    @work_require.setter
    def work_require(self, value):
        if isinstance(value, list):
            self._work_require = list()
            for i in value:
                self._work_require.append(i)
    @property
    def work_start_date(self):
        return self._work_start_date

    @work_start_date.setter
    def work_start_date(self, value):
        self._work_start_date = value
    @property
    def work_start_time(self):
        return self._work_start_time

    @work_start_time.setter
    def work_start_time(self, value):
        self._work_start_time = value
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
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.client_job_url:
            if hasattr(self.client_job_url, 'to_alipay_dict'):
                params['client_job_url'] = self.client_job_url.to_alipay_dict()
            else:
                params['client_job_url'] = self.client_job_url
        if self.employee_welfare:
            if isinstance(self.employee_welfare, list):
                for i in range(0, len(self.employee_welfare)):
                    element = self.employee_welfare[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.employee_welfare[i] = element.to_alipay_dict()
            if hasattr(self.employee_welfare, 'to_alipay_dict'):
                params['employee_welfare'] = self.employee_welfare.to_alipay_dict()
            else:
                params['employee_welfare'] = self.employee_welfare
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
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.graduation_time:
            if hasattr(self.graduation_time, 'to_alipay_dict'):
                params['graduation_time'] = self.graduation_time.to_alipay_dict()
            else:
                params['graduation_time'] = self.graduation_time
        if self.hire_open_id:
            if hasattr(self.hire_open_id, 'to_alipay_dict'):
                params['hire_open_id'] = self.hire_open_id.to_alipay_dict()
            else:
                params['hire_open_id'] = self.hire_open_id
        if self.hire_status:
            if hasattr(self.hire_status, 'to_alipay_dict'):
                params['hire_status'] = self.hire_status.to_alipay_dict()
            else:
                params['hire_status'] = self.hire_status
        if self.hire_user_id:
            if hasattr(self.hire_user_id, 'to_alipay_dict'):
                params['hire_user_id'] = self.hire_user_id.to_alipay_dict()
            else:
                params['hire_user_id'] = self.hire_user_id
        if self.hire_user_mobile:
            if hasattr(self.hire_user_mobile, 'to_alipay_dict'):
                params['hire_user_mobile'] = self.hire_user_mobile.to_alipay_dict()
            else:
                params['hire_user_mobile'] = self.hire_user_mobile
        if self.hire_user_name:
            if hasattr(self.hire_user_name, 'to_alipay_dict'):
                params['hire_user_name'] = self.hire_user_name.to_alipay_dict()
            else:
                params['hire_user_name'] = self.hire_user_name
        if self.job_detail:
            if hasattr(self.job_detail, 'to_alipay_dict'):
                params['job_detail'] = self.job_detail.to_alipay_dict()
            else:
                params['job_detail'] = self.job_detail
        if self.job_end_time:
            if hasattr(self.job_end_time, 'to_alipay_dict'):
                params['job_end_time'] = self.job_end_time.to_alipay_dict()
            else:
                params['job_end_time'] = self.job_end_time
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.job_off_reason:
            if hasattr(self.job_off_reason, 'to_alipay_dict'):
                params['job_off_reason'] = self.job_off_reason.to_alipay_dict()
            else:
                params['job_off_reason'] = self.job_off_reason
        if self.job_type:
            if hasattr(self.job_type, 'to_alipay_dict'):
                params['job_type'] = self.job_type.to_alipay_dict()
            else:
                params['job_type'] = self.job_type
        if self.out_hire_user_id:
            if hasattr(self.out_hire_user_id, 'to_alipay_dict'):
                params['out_hire_user_id'] = self.out_hire_user_id.to_alipay_dict()
            else:
                params['out_hire_user_id'] = self.out_hire_user_id
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
        if self.performance_bonus:
            if hasattr(self.performance_bonus, 'to_alipay_dict'):
                params['performance_bonus'] = self.performance_bonus.to_alipay_dict()
            else:
                params['performance_bonus'] = self.performance_bonus
        if self.recruit_count:
            if hasattr(self.recruit_count, 'to_alipay_dict'):
                params['recruit_count'] = self.recruit_count.to_alipay_dict()
            else:
                params['recruit_count'] = self.recruit_count
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
        if self.server_job_url:
            if hasattr(self.server_job_url, 'to_alipay_dict'):
                params['server_job_url'] = self.server_job_url.to_alipay_dict()
            else:
                params['server_job_url'] = self.server_job_url
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.work_end_date:
            if hasattr(self.work_end_date, 'to_alipay_dict'):
                params['work_end_date'] = self.work_end_date.to_alipay_dict()
            else:
                params['work_end_date'] = self.work_end_date
        if self.work_end_time:
            if hasattr(self.work_end_time, 'to_alipay_dict'):
                params['work_end_time'] = self.work_end_time.to_alipay_dict()
            else:
                params['work_end_time'] = self.work_end_time
        if self.work_require:
            if isinstance(self.work_require, list):
                for i in range(0, len(self.work_require)):
                    element = self.work_require[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_require[i] = element.to_alipay_dict()
            if hasattr(self.work_require, 'to_alipay_dict'):
                params['work_require'] = self.work_require.to_alipay_dict()
            else:
                params['work_require'] = self.work_require
        if self.work_start_date:
            if hasattr(self.work_start_date, 'to_alipay_dict'):
                params['work_start_date'] = self.work_start_date.to_alipay_dict()
            else:
                params['work_start_date'] = self.work_start_date
        if self.work_start_time:
            if hasattr(self.work_start_time, 'to_alipay_dict'):
                params['work_start_time'] = self.work_start_time.to_alipay_dict()
            else:
                params['work_start_time'] = self.work_start_time
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
        o = AlipayEbppIndustryRecruitJobSyncModel()
        if 'academic_require' in d:
            o.academic_require = d['academic_require']
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'age' in d:
            o.age = d['age']
        if 'client_job_url' in d:
            o.client_job_url = d['client_job_url']
        if 'employee_welfare' in d:
            o.employee_welfare = d['employee_welfare']
        if 'employer_name' in d:
            o.employer_name = d['employer_name']
        if 'employer_type' in d:
            o.employer_type = d['employer_type']
        if 'gender' in d:
            o.gender = d['gender']
        if 'graduation_time' in d:
            o.graduation_time = d['graduation_time']
        if 'hire_open_id' in d:
            o.hire_open_id = d['hire_open_id']
        if 'hire_status' in d:
            o.hire_status = d['hire_status']
        if 'hire_user_id' in d:
            o.hire_user_id = d['hire_user_id']
        if 'hire_user_mobile' in d:
            o.hire_user_mobile = d['hire_user_mobile']
        if 'hire_user_name' in d:
            o.hire_user_name = d['hire_user_name']
        if 'job_detail' in d:
            o.job_detail = d['job_detail']
        if 'job_end_time' in d:
            o.job_end_time = d['job_end_time']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'job_off_reason' in d:
            o.job_off_reason = d['job_off_reason']
        if 'job_type' in d:
            o.job_type = d['job_type']
        if 'out_hire_user_id' in d:
            o.out_hire_user_id = d['out_hire_user_id']
        if 'out_job_id' in d:
            o.out_job_id = d['out_job_id']
        if 'part_time_mode' in d:
            o.part_time_mode = d['part_time_mode']
        if 'performance_bonus' in d:
            o.performance_bonus = d['performance_bonus']
        if 'recruit_count' in d:
            o.recruit_count = d['recruit_count']
        if 'salary_max' in d:
            o.salary_max = d['salary_max']
        if 'salary_min' in d:
            o.salary_min = d['salary_min']
        if 'salary_unit' in d:
            o.salary_unit = d['salary_unit']
        if 'server_job_url' in d:
            o.server_job_url = d['server_job_url']
        if 'source' in d:
            o.source = d['source']
        if 'work_end_date' in d:
            o.work_end_date = d['work_end_date']
        if 'work_end_time' in d:
            o.work_end_time = d['work_end_time']
        if 'work_require' in d:
            o.work_require = d['work_require']
        if 'work_start_date' in d:
            o.work_start_date = d['work_start_date']
        if 'work_start_time' in d:
            o.work_start_time = d['work_start_time']
        if 'working_years' in d:
            o.working_years = d['working_years']
        return o



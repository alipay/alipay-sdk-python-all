#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JobWorthJobdata(object):

    def __init__(self):
        self._certificate_id = None
        self._certificate_name = None
        self._certificate_pic_id = None
        self._company_name = None
        self._degree = None
        self._education_status = None
        self._intention_city = None
        self._job_id = None
        self._job_name = None
        self._ka_job_id = None
        self._ka_job_name = None
        self._ka_profession_id = None
        self._ka_profession_name = None
        self._location = None
        self._month = None
        self._profession_id = None
        self._profession_name = None
        self._salary_max = None
        self._salary_min = None
        self._salary_unit = None
        self._school_name = None
        self._skill_name = None
        self._start_time = None
        self._type = None
        self._work_desc = None
        self._work_end_time = None
        self._work_property = None
        self._work_start_time = None
        self._year = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_name(self):
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, value):
        self._certificate_name = value
    @property
    def certificate_pic_id(self):
        return self._certificate_pic_id

    @certificate_pic_id.setter
    def certificate_pic_id(self, value):
        self._certificate_pic_id = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        self._degree = value
    @property
    def education_status(self):
        return self._education_status

    @education_status.setter
    def education_status(self, value):
        self._education_status = value
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
    def ka_job_id(self):
        return self._ka_job_id

    @ka_job_id.setter
    def ka_job_id(self, value):
        self._ka_job_id = value
    @property
    def ka_job_name(self):
        return self._ka_job_name

    @ka_job_name.setter
    def ka_job_name(self, value):
        self._ka_job_name = value
    @property
    def ka_profession_id(self):
        return self._ka_profession_id

    @ka_profession_id.setter
    def ka_profession_id(self, value):
        self._ka_profession_id = value
    @property
    def ka_profession_name(self):
        return self._ka_profession_name

    @ka_profession_name.setter
    def ka_profession_name(self, value):
        self._ka_profession_name = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
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
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def skill_name(self):
        return self._skill_name

    @skill_name.setter
    def skill_name(self, value):
        self._skill_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
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
    def work_property(self):
        return self._work_property

    @work_property.setter
    def work_property(self, value):
        self._work_property = value
    @property
    def work_start_time(self):
        return self._work_start_time

    @work_start_time.setter
    def work_start_time(self, value):
        self._work_start_time = value
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_name:
            if hasattr(self.certificate_name, 'to_alipay_dict'):
                params['certificate_name'] = self.certificate_name.to_alipay_dict()
            else:
                params['certificate_name'] = self.certificate_name
        if self.certificate_pic_id:
            if hasattr(self.certificate_pic_id, 'to_alipay_dict'):
                params['certificate_pic_id'] = self.certificate_pic_id.to_alipay_dict()
            else:
                params['certificate_pic_id'] = self.certificate_pic_id
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.degree:
            if hasattr(self.degree, 'to_alipay_dict'):
                params['degree'] = self.degree.to_alipay_dict()
            else:
                params['degree'] = self.degree
        if self.education_status:
            if hasattr(self.education_status, 'to_alipay_dict'):
                params['education_status'] = self.education_status.to_alipay_dict()
            else:
                params['education_status'] = self.education_status
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
        if self.ka_job_id:
            if hasattr(self.ka_job_id, 'to_alipay_dict'):
                params['ka_job_id'] = self.ka_job_id.to_alipay_dict()
            else:
                params['ka_job_id'] = self.ka_job_id
        if self.ka_job_name:
            if hasattr(self.ka_job_name, 'to_alipay_dict'):
                params['ka_job_name'] = self.ka_job_name.to_alipay_dict()
            else:
                params['ka_job_name'] = self.ka_job_name
        if self.ka_profession_id:
            if hasattr(self.ka_profession_id, 'to_alipay_dict'):
                params['ka_profession_id'] = self.ka_profession_id.to_alipay_dict()
            else:
                params['ka_profession_id'] = self.ka_profession_id
        if self.ka_profession_name:
            if hasattr(self.ka_profession_name, 'to_alipay_dict'):
                params['ka_profession_name'] = self.ka_profession_name.to_alipay_dict()
            else:
                params['ka_profession_name'] = self.ka_profession_name
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
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
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.skill_name:
            if hasattr(self.skill_name, 'to_alipay_dict'):
                params['skill_name'] = self.skill_name.to_alipay_dict()
            else:
                params['skill_name'] = self.skill_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        if self.work_property:
            if hasattr(self.work_property, 'to_alipay_dict'):
                params['work_property'] = self.work_property.to_alipay_dict()
            else:
                params['work_property'] = self.work_property
        if self.work_start_time:
            if hasattr(self.work_start_time, 'to_alipay_dict'):
                params['work_start_time'] = self.work_start_time.to_alipay_dict()
            else:
                params['work_start_time'] = self.work_start_time
        if self.year:
            if hasattr(self.year, 'to_alipay_dict'):
                params['year'] = self.year.to_alipay_dict()
            else:
                params['year'] = self.year
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JobWorthJobdata()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_name' in d:
            o.certificate_name = d['certificate_name']
        if 'certificate_pic_id' in d:
            o.certificate_pic_id = d['certificate_pic_id']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'degree' in d:
            o.degree = d['degree']
        if 'education_status' in d:
            o.education_status = d['education_status']
        if 'intention_city' in d:
            o.intention_city = d['intention_city']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'ka_job_id' in d:
            o.ka_job_id = d['ka_job_id']
        if 'ka_job_name' in d:
            o.ka_job_name = d['ka_job_name']
        if 'ka_profession_id' in d:
            o.ka_profession_id = d['ka_profession_id']
        if 'ka_profession_name' in d:
            o.ka_profession_name = d['ka_profession_name']
        if 'location' in d:
            o.location = d['location']
        if 'month' in d:
            o.month = d['month']
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
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'skill_name' in d:
            o.skill_name = d['skill_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'type' in d:
            o.type = d['type']
        if 'work_desc' in d:
            o.work_desc = d['work_desc']
        if 'work_end_time' in d:
            o.work_end_time = d['work_end_time']
        if 'work_property' in d:
            o.work_property = d['work_property']
        if 'work_start_time' in d:
            o.work_start_time = d['work_start_time']
        if 'year' in d:
            o.year = d['year']
        return o



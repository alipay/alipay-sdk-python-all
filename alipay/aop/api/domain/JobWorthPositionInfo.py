#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JobWorthPositionInfo(object):

    def __init__(self):
        self._age = None
        self._benefit = None
        self._certifications = None
        self._company_certificate = None
        self._company_name = None
        self._count = None
        self._education = None
        self._gender = None
        self._ka_position_id = None
        self._position_desc = None
        self._position_id = None
        self._position_job_id = None
        self._position_job_name = None
        self._position_profession_id = None
        self._position_property = None
        self._position_status = None
        self._position_title = None
        self._salary_max = None
        self._salary_min = None
        self._salary_type = None
        self._salary_unit = None
        self._skill_tag = None
        self._skip_url = None
        self._work_city = None
        self._work_longitude = None
        self._work_region = None
        self._work_year = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def benefit(self):
        return self._benefit

    @benefit.setter
    def benefit(self, value):
        self._benefit = value
    @property
    def certifications(self):
        return self._certifications

    @certifications.setter
    def certifications(self, value):
        self._certifications = value
    @property
    def company_certificate(self):
        return self._company_certificate

    @company_certificate.setter
    def company_certificate(self, value):
        self._company_certificate = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def education(self):
        return self._education

    @education.setter
    def education(self, value):
        self._education = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def ka_position_id(self):
        return self._ka_position_id

    @ka_position_id.setter
    def ka_position_id(self, value):
        self._ka_position_id = value
    @property
    def position_desc(self):
        return self._position_desc

    @position_desc.setter
    def position_desc(self, value):
        self._position_desc = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value
    @property
    def position_job_id(self):
        return self._position_job_id

    @position_job_id.setter
    def position_job_id(self, value):
        self._position_job_id = value
    @property
    def position_job_name(self):
        return self._position_job_name

    @position_job_name.setter
    def position_job_name(self, value):
        self._position_job_name = value
    @property
    def position_profession_id(self):
        return self._position_profession_id

    @position_profession_id.setter
    def position_profession_id(self, value):
        self._position_profession_id = value
    @property
    def position_property(self):
        return self._position_property

    @position_property.setter
    def position_property(self, value):
        self._position_property = value
    @property
    def position_status(self):
        return self._position_status

    @position_status.setter
    def position_status(self, value):
        self._position_status = value
    @property
    def position_title(self):
        return self._position_title

    @position_title.setter
    def position_title(self, value):
        self._position_title = value
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
    def salary_type(self):
        return self._salary_type

    @salary_type.setter
    def salary_type(self, value):
        self._salary_type = value
    @property
    def salary_unit(self):
        return self._salary_unit

    @salary_unit.setter
    def salary_unit(self, value):
        self._salary_unit = value
    @property
    def skill_tag(self):
        return self._skill_tag

    @skill_tag.setter
    def skill_tag(self, value):
        self._skill_tag = value
    @property
    def skip_url(self):
        return self._skip_url

    @skip_url.setter
    def skip_url(self, value):
        self._skip_url = value
    @property
    def work_city(self):
        return self._work_city

    @work_city.setter
    def work_city(self, value):
        self._work_city = value
    @property
    def work_longitude(self):
        return self._work_longitude

    @work_longitude.setter
    def work_longitude(self, value):
        self._work_longitude = value
    @property
    def work_region(self):
        return self._work_region

    @work_region.setter
    def work_region(self, value):
        self._work_region = value
    @property
    def work_year(self):
        return self._work_year

    @work_year.setter
    def work_year(self, value):
        self._work_year = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.benefit:
            if hasattr(self.benefit, 'to_alipay_dict'):
                params['benefit'] = self.benefit.to_alipay_dict()
            else:
                params['benefit'] = self.benefit
        if self.certifications:
            if hasattr(self.certifications, 'to_alipay_dict'):
                params['certifications'] = self.certifications.to_alipay_dict()
            else:
                params['certifications'] = self.certifications
        if self.company_certificate:
            if hasattr(self.company_certificate, 'to_alipay_dict'):
                params['company_certificate'] = self.company_certificate.to_alipay_dict()
            else:
                params['company_certificate'] = self.company_certificate
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.education:
            if hasattr(self.education, 'to_alipay_dict'):
                params['education'] = self.education.to_alipay_dict()
            else:
                params['education'] = self.education
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.ka_position_id:
            if hasattr(self.ka_position_id, 'to_alipay_dict'):
                params['ka_position_id'] = self.ka_position_id.to_alipay_dict()
            else:
                params['ka_position_id'] = self.ka_position_id
        if self.position_desc:
            if hasattr(self.position_desc, 'to_alipay_dict'):
                params['position_desc'] = self.position_desc.to_alipay_dict()
            else:
                params['position_desc'] = self.position_desc
        if self.position_id:
            if hasattr(self.position_id, 'to_alipay_dict'):
                params['position_id'] = self.position_id.to_alipay_dict()
            else:
                params['position_id'] = self.position_id
        if self.position_job_id:
            if hasattr(self.position_job_id, 'to_alipay_dict'):
                params['position_job_id'] = self.position_job_id.to_alipay_dict()
            else:
                params['position_job_id'] = self.position_job_id
        if self.position_job_name:
            if hasattr(self.position_job_name, 'to_alipay_dict'):
                params['position_job_name'] = self.position_job_name.to_alipay_dict()
            else:
                params['position_job_name'] = self.position_job_name
        if self.position_profession_id:
            if hasattr(self.position_profession_id, 'to_alipay_dict'):
                params['position_profession_id'] = self.position_profession_id.to_alipay_dict()
            else:
                params['position_profession_id'] = self.position_profession_id
        if self.position_property:
            if hasattr(self.position_property, 'to_alipay_dict'):
                params['position_property'] = self.position_property.to_alipay_dict()
            else:
                params['position_property'] = self.position_property
        if self.position_status:
            if hasattr(self.position_status, 'to_alipay_dict'):
                params['position_status'] = self.position_status.to_alipay_dict()
            else:
                params['position_status'] = self.position_status
        if self.position_title:
            if hasattr(self.position_title, 'to_alipay_dict'):
                params['position_title'] = self.position_title.to_alipay_dict()
            else:
                params['position_title'] = self.position_title
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
        if self.salary_type:
            if hasattr(self.salary_type, 'to_alipay_dict'):
                params['salary_type'] = self.salary_type.to_alipay_dict()
            else:
                params['salary_type'] = self.salary_type
        if self.salary_unit:
            if hasattr(self.salary_unit, 'to_alipay_dict'):
                params['salary_unit'] = self.salary_unit.to_alipay_dict()
            else:
                params['salary_unit'] = self.salary_unit
        if self.skill_tag:
            if hasattr(self.skill_tag, 'to_alipay_dict'):
                params['skill_tag'] = self.skill_tag.to_alipay_dict()
            else:
                params['skill_tag'] = self.skill_tag
        if self.skip_url:
            if hasattr(self.skip_url, 'to_alipay_dict'):
                params['skip_url'] = self.skip_url.to_alipay_dict()
            else:
                params['skip_url'] = self.skip_url
        if self.work_city:
            if hasattr(self.work_city, 'to_alipay_dict'):
                params['work_city'] = self.work_city.to_alipay_dict()
            else:
                params['work_city'] = self.work_city
        if self.work_longitude:
            if hasattr(self.work_longitude, 'to_alipay_dict'):
                params['work_longitude'] = self.work_longitude.to_alipay_dict()
            else:
                params['work_longitude'] = self.work_longitude
        if self.work_region:
            if hasattr(self.work_region, 'to_alipay_dict'):
                params['work_region'] = self.work_region.to_alipay_dict()
            else:
                params['work_region'] = self.work_region
        if self.work_year:
            if hasattr(self.work_year, 'to_alipay_dict'):
                params['work_year'] = self.work_year.to_alipay_dict()
            else:
                params['work_year'] = self.work_year
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JobWorthPositionInfo()
        if 'age' in d:
            o.age = d['age']
        if 'benefit' in d:
            o.benefit = d['benefit']
        if 'certifications' in d:
            o.certifications = d['certifications']
        if 'company_certificate' in d:
            o.company_certificate = d['company_certificate']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'count' in d:
            o.count = d['count']
        if 'education' in d:
            o.education = d['education']
        if 'gender' in d:
            o.gender = d['gender']
        if 'ka_position_id' in d:
            o.ka_position_id = d['ka_position_id']
        if 'position_desc' in d:
            o.position_desc = d['position_desc']
        if 'position_id' in d:
            o.position_id = d['position_id']
        if 'position_job_id' in d:
            o.position_job_id = d['position_job_id']
        if 'position_job_name' in d:
            o.position_job_name = d['position_job_name']
        if 'position_profession_id' in d:
            o.position_profession_id = d['position_profession_id']
        if 'position_property' in d:
            o.position_property = d['position_property']
        if 'position_status' in d:
            o.position_status = d['position_status']
        if 'position_title' in d:
            o.position_title = d['position_title']
        if 'salary_max' in d:
            o.salary_max = d['salary_max']
        if 'salary_min' in d:
            o.salary_min = d['salary_min']
        if 'salary_type' in d:
            o.salary_type = d['salary_type']
        if 'salary_unit' in d:
            o.salary_unit = d['salary_unit']
        if 'skill_tag' in d:
            o.skill_tag = d['skill_tag']
        if 'skip_url' in d:
            o.skip_url = d['skip_url']
        if 'work_city' in d:
            o.work_city = d['work_city']
        if 'work_longitude' in d:
            o.work_longitude = d['work_longitude']
        if 'work_region' in d:
            o.work_region = d['work_region']
        if 'work_year' in d:
            o.work_year = d['work_year']
        return o



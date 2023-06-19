#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JobWorthJobdata(object):

    def __init__(self):
        self._certificate_grant_institution = None
        self._certificate_id = None
        self._certificate_level = None
        self._certificate_name = None
        self._certificate_pic_id = None
        self._company_name = None
        self._degree = None
        self._delivery_position_id = None
        self._delivery_time = None
        self._education_status = None
        self._entry_no = None
        self._exam_score = None
        self._head_pic_id = None
        self._intention_city = None
        self._intention_city_name = None
        self._issue_date = None
        self._job_id = None
        self._job_name = None
        self._ka_job_id = None
        self._ka_job_name = None
        self._ka_profession_id = None
        self._ka_profession_name = None
        self._location = None
        self._month = None
        self._once_token = None
        self._profession_id = None
        self._profession_name = None
        self._salary_max = None
        self._salary_min = None
        self._salary_unit = None
        self._school_name = None
        self._skill_name = None
        self._start_time = None
        self._type = None
        self._valid_date_end = None
        self._valid_date_start = None
        self._verify_status = None
        self._work_desc = None
        self._work_end_time = None
        self._work_place = None
        self._work_property = None
        self._work_start_time = None
        self._year = None

    @property
    def certificate_grant_institution(self):
        return self._certificate_grant_institution

    @certificate_grant_institution.setter
    def certificate_grant_institution(self, value):
        self._certificate_grant_institution = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_level(self):
        return self._certificate_level

    @certificate_level.setter
    def certificate_level(self, value):
        self._certificate_level = value
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
    def delivery_position_id(self):
        return self._delivery_position_id

    @delivery_position_id.setter
    def delivery_position_id(self, value):
        self._delivery_position_id = value
    @property
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, value):
        self._delivery_time = value
    @property
    def education_status(self):
        return self._education_status

    @education_status.setter
    def education_status(self, value):
        self._education_status = value
    @property
    def entry_no(self):
        return self._entry_no

    @entry_no.setter
    def entry_no(self, value):
        self._entry_no = value
    @property
    def exam_score(self):
        return self._exam_score

    @exam_score.setter
    def exam_score(self, value):
        self._exam_score = value
    @property
    def head_pic_id(self):
        return self._head_pic_id

    @head_pic_id.setter
    def head_pic_id(self, value):
        self._head_pic_id = value
    @property
    def intention_city(self):
        return self._intention_city

    @intention_city.setter
    def intention_city(self, value):
        self._intention_city = value
    @property
    def intention_city_name(self):
        return self._intention_city_name

    @intention_city_name.setter
    def intention_city_name(self, value):
        self._intention_city_name = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
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
    def once_token(self):
        return self._once_token

    @once_token.setter
    def once_token(self, value):
        self._once_token = value
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
    def valid_date_end(self):
        return self._valid_date_end

    @valid_date_end.setter
    def valid_date_end(self, value):
        self._valid_date_end = value
    @property
    def valid_date_start(self):
        return self._valid_date_start

    @valid_date_start.setter
    def valid_date_start(self, value):
        self._valid_date_start = value
    @property
    def verify_status(self):
        return self._verify_status

    @verify_status.setter
    def verify_status(self, value):
        self._verify_status = value
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
    def work_place(self):
        return self._work_place

    @work_place.setter
    def work_place(self, value):
        self._work_place = value
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
        if self.certificate_grant_institution:
            if hasattr(self.certificate_grant_institution, 'to_alipay_dict'):
                params['certificate_grant_institution'] = self.certificate_grant_institution.to_alipay_dict()
            else:
                params['certificate_grant_institution'] = self.certificate_grant_institution
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_level:
            if hasattr(self.certificate_level, 'to_alipay_dict'):
                params['certificate_level'] = self.certificate_level.to_alipay_dict()
            else:
                params['certificate_level'] = self.certificate_level
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
        if self.delivery_position_id:
            if hasattr(self.delivery_position_id, 'to_alipay_dict'):
                params['delivery_position_id'] = self.delivery_position_id.to_alipay_dict()
            else:
                params['delivery_position_id'] = self.delivery_position_id
        if self.delivery_time:
            if hasattr(self.delivery_time, 'to_alipay_dict'):
                params['delivery_time'] = self.delivery_time.to_alipay_dict()
            else:
                params['delivery_time'] = self.delivery_time
        if self.education_status:
            if hasattr(self.education_status, 'to_alipay_dict'):
                params['education_status'] = self.education_status.to_alipay_dict()
            else:
                params['education_status'] = self.education_status
        if self.entry_no:
            if hasattr(self.entry_no, 'to_alipay_dict'):
                params['entry_no'] = self.entry_no.to_alipay_dict()
            else:
                params['entry_no'] = self.entry_no
        if self.exam_score:
            if hasattr(self.exam_score, 'to_alipay_dict'):
                params['exam_score'] = self.exam_score.to_alipay_dict()
            else:
                params['exam_score'] = self.exam_score
        if self.head_pic_id:
            if hasattr(self.head_pic_id, 'to_alipay_dict'):
                params['head_pic_id'] = self.head_pic_id.to_alipay_dict()
            else:
                params['head_pic_id'] = self.head_pic_id
        if self.intention_city:
            if hasattr(self.intention_city, 'to_alipay_dict'):
                params['intention_city'] = self.intention_city.to_alipay_dict()
            else:
                params['intention_city'] = self.intention_city
        if self.intention_city_name:
            if hasattr(self.intention_city_name, 'to_alipay_dict'):
                params['intention_city_name'] = self.intention_city_name.to_alipay_dict()
            else:
                params['intention_city_name'] = self.intention_city_name
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
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
        if self.once_token:
            if hasattr(self.once_token, 'to_alipay_dict'):
                params['once_token'] = self.once_token.to_alipay_dict()
            else:
                params['once_token'] = self.once_token
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
        if self.valid_date_end:
            if hasattr(self.valid_date_end, 'to_alipay_dict'):
                params['valid_date_end'] = self.valid_date_end.to_alipay_dict()
            else:
                params['valid_date_end'] = self.valid_date_end
        if self.valid_date_start:
            if hasattr(self.valid_date_start, 'to_alipay_dict'):
                params['valid_date_start'] = self.valid_date_start.to_alipay_dict()
            else:
                params['valid_date_start'] = self.valid_date_start
        if self.verify_status:
            if hasattr(self.verify_status, 'to_alipay_dict'):
                params['verify_status'] = self.verify_status.to_alipay_dict()
            else:
                params['verify_status'] = self.verify_status
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
        if self.work_place:
            if hasattr(self.work_place, 'to_alipay_dict'):
                params['work_place'] = self.work_place.to_alipay_dict()
            else:
                params['work_place'] = self.work_place
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
        if 'certificate_grant_institution' in d:
            o.certificate_grant_institution = d['certificate_grant_institution']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_level' in d:
            o.certificate_level = d['certificate_level']
        if 'certificate_name' in d:
            o.certificate_name = d['certificate_name']
        if 'certificate_pic_id' in d:
            o.certificate_pic_id = d['certificate_pic_id']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'degree' in d:
            o.degree = d['degree']
        if 'delivery_position_id' in d:
            o.delivery_position_id = d['delivery_position_id']
        if 'delivery_time' in d:
            o.delivery_time = d['delivery_time']
        if 'education_status' in d:
            o.education_status = d['education_status']
        if 'entry_no' in d:
            o.entry_no = d['entry_no']
        if 'exam_score' in d:
            o.exam_score = d['exam_score']
        if 'head_pic_id' in d:
            o.head_pic_id = d['head_pic_id']
        if 'intention_city' in d:
            o.intention_city = d['intention_city']
        if 'intention_city_name' in d:
            o.intention_city_name = d['intention_city_name']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
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
        if 'once_token' in d:
            o.once_token = d['once_token']
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
        if 'valid_date_end' in d:
            o.valid_date_end = d['valid_date_end']
        if 'valid_date_start' in d:
            o.valid_date_start = d['valid_date_start']
        if 'verify_status' in d:
            o.verify_status = d['verify_status']
        if 'work_desc' in d:
            o.work_desc = d['work_desc']
        if 'work_end_time' in d:
            o.work_end_time = d['work_end_time']
        if 'work_place' in d:
            o.work_place = d['work_place']
        if 'work_property' in d:
            o.work_property = d['work_property']
        if 'work_start_time' in d:
            o.work_start_time = d['work_start_time']
        if 'year' in d:
            o.year = d['year']
        return o



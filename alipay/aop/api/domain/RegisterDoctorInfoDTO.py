#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegisterNumberCountDTO import RegisterNumberCountDTO


class RegisterDoctorInfoDTO(object):

    def __init__(self):
        self._address = None
        self._book_date = None
        self._date = None
        self._department_id = None
        self._department_name = None
        self._detail_url = None
        self._distance = None
        self._doctor_gender = None
        self._doctor_id = None
        self._doctor_inner_id = None
        self._doctor_logo = None
        self._doctor_name = None
        self._earliest_date = None
        self._education_title = None
        self._hos_grade = None
        self._hos_uinq_code = None
        self._hospital_address = None
        self._hospital_dep_feature_tags = None
        self._hospital_id = None
        self._hospital_name = None
        self._number_count_list = None
        self._number_status = None
        self._platform_code = None
        self._proficiency = None
        self._register_date = None
        self._schedule_status = None
        self._title = None
        self._week_num = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def book_date(self):
        return self._book_date

    @book_date.setter
    def book_date(self, value):
        self._book_date = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def doctor_gender(self):
        return self._doctor_gender

    @doctor_gender.setter
    def doctor_gender(self, value):
        self._doctor_gender = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_inner_id(self):
        return self._doctor_inner_id

    @doctor_inner_id.setter
    def doctor_inner_id(self, value):
        self._doctor_inner_id = value
    @property
    def doctor_logo(self):
        return self._doctor_logo

    @doctor_logo.setter
    def doctor_logo(self, value):
        self._doctor_logo = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def earliest_date(self):
        return self._earliest_date

    @earliest_date.setter
    def earliest_date(self, value):
        self._earliest_date = value
    @property
    def education_title(self):
        return self._education_title

    @education_title.setter
    def education_title(self, value):
        self._education_title = value
    @property
    def hos_grade(self):
        return self._hos_grade

    @hos_grade.setter
    def hos_grade(self, value):
        self._hos_grade = value
    @property
    def hos_uinq_code(self):
        return self._hos_uinq_code

    @hos_uinq_code.setter
    def hos_uinq_code(self, value):
        self._hos_uinq_code = value
    @property
    def hospital_address(self):
        return self._hospital_address

    @hospital_address.setter
    def hospital_address(self, value):
        self._hospital_address = value
    @property
    def hospital_dep_feature_tags(self):
        return self._hospital_dep_feature_tags

    @hospital_dep_feature_tags.setter
    def hospital_dep_feature_tags(self, value):
        if isinstance(value, list):
            self._hospital_dep_feature_tags = list()
            for i in value:
                self._hospital_dep_feature_tags.append(i)
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def number_count_list(self):
        return self._number_count_list

    @number_count_list.setter
    def number_count_list(self, value):
        if isinstance(value, list):
            self._number_count_list = list()
            for i in value:
                if isinstance(i, RegisterNumberCountDTO):
                    self._number_count_list.append(i)
                else:
                    self._number_count_list.append(RegisterNumberCountDTO.from_alipay_dict(i))
    @property
    def number_status(self):
        return self._number_status

    @number_status.setter
    def number_status(self, value):
        self._number_status = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def proficiency(self):
        return self._proficiency

    @proficiency.setter
    def proficiency(self, value):
        self._proficiency = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def schedule_status(self):
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, value):
        self._schedule_status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def week_num(self):
        return self._week_num

    @week_num.setter
    def week_num(self, value):
        self._week_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.book_date:
            if hasattr(self.book_date, 'to_alipay_dict'):
                params['book_date'] = self.book_date.to_alipay_dict()
            else:
                params['book_date'] = self.book_date
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.doctor_gender:
            if hasattr(self.doctor_gender, 'to_alipay_dict'):
                params['doctor_gender'] = self.doctor_gender.to_alipay_dict()
            else:
                params['doctor_gender'] = self.doctor_gender
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_inner_id:
            if hasattr(self.doctor_inner_id, 'to_alipay_dict'):
                params['doctor_inner_id'] = self.doctor_inner_id.to_alipay_dict()
            else:
                params['doctor_inner_id'] = self.doctor_inner_id
        if self.doctor_logo:
            if hasattr(self.doctor_logo, 'to_alipay_dict'):
                params['doctor_logo'] = self.doctor_logo.to_alipay_dict()
            else:
                params['doctor_logo'] = self.doctor_logo
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.earliest_date:
            if hasattr(self.earliest_date, 'to_alipay_dict'):
                params['earliest_date'] = self.earliest_date.to_alipay_dict()
            else:
                params['earliest_date'] = self.earliest_date
        if self.education_title:
            if hasattr(self.education_title, 'to_alipay_dict'):
                params['education_title'] = self.education_title.to_alipay_dict()
            else:
                params['education_title'] = self.education_title
        if self.hos_grade:
            if hasattr(self.hos_grade, 'to_alipay_dict'):
                params['hos_grade'] = self.hos_grade.to_alipay_dict()
            else:
                params['hos_grade'] = self.hos_grade
        if self.hos_uinq_code:
            if hasattr(self.hos_uinq_code, 'to_alipay_dict'):
                params['hos_uinq_code'] = self.hos_uinq_code.to_alipay_dict()
            else:
                params['hos_uinq_code'] = self.hos_uinq_code
        if self.hospital_address:
            if hasattr(self.hospital_address, 'to_alipay_dict'):
                params['hospital_address'] = self.hospital_address.to_alipay_dict()
            else:
                params['hospital_address'] = self.hospital_address
        if self.hospital_dep_feature_tags:
            if isinstance(self.hospital_dep_feature_tags, list):
                for i in range(0, len(self.hospital_dep_feature_tags)):
                    element = self.hospital_dep_feature_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hospital_dep_feature_tags[i] = element.to_alipay_dict()
            if hasattr(self.hospital_dep_feature_tags, 'to_alipay_dict'):
                params['hospital_dep_feature_tags'] = self.hospital_dep_feature_tags.to_alipay_dict()
            else:
                params['hospital_dep_feature_tags'] = self.hospital_dep_feature_tags
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.number_count_list:
            if isinstance(self.number_count_list, list):
                for i in range(0, len(self.number_count_list)):
                    element = self.number_count_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.number_count_list[i] = element.to_alipay_dict()
            if hasattr(self.number_count_list, 'to_alipay_dict'):
                params['number_count_list'] = self.number_count_list.to_alipay_dict()
            else:
                params['number_count_list'] = self.number_count_list
        if self.number_status:
            if hasattr(self.number_status, 'to_alipay_dict'):
                params['number_status'] = self.number_status.to_alipay_dict()
            else:
                params['number_status'] = self.number_status
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.proficiency:
            if hasattr(self.proficiency, 'to_alipay_dict'):
                params['proficiency'] = self.proficiency.to_alipay_dict()
            else:
                params['proficiency'] = self.proficiency
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.schedule_status:
            if hasattr(self.schedule_status, 'to_alipay_dict'):
                params['schedule_status'] = self.schedule_status.to_alipay_dict()
            else:
                params['schedule_status'] = self.schedule_status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.week_num:
            if hasattr(self.week_num, 'to_alipay_dict'):
                params['week_num'] = self.week_num.to_alipay_dict()
            else:
                params['week_num'] = self.week_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterDoctorInfoDTO()
        if 'address' in d:
            o.address = d['address']
        if 'book_date' in d:
            o.book_date = d['book_date']
        if 'date' in d:
            o.date = d['date']
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'distance' in d:
            o.distance = d['distance']
        if 'doctor_gender' in d:
            o.doctor_gender = d['doctor_gender']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_inner_id' in d:
            o.doctor_inner_id = d['doctor_inner_id']
        if 'doctor_logo' in d:
            o.doctor_logo = d['doctor_logo']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'earliest_date' in d:
            o.earliest_date = d['earliest_date']
        if 'education_title' in d:
            o.education_title = d['education_title']
        if 'hos_grade' in d:
            o.hos_grade = d['hos_grade']
        if 'hos_uinq_code' in d:
            o.hos_uinq_code = d['hos_uinq_code']
        if 'hospital_address' in d:
            o.hospital_address = d['hospital_address']
        if 'hospital_dep_feature_tags' in d:
            o.hospital_dep_feature_tags = d['hospital_dep_feature_tags']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'number_count_list' in d:
            o.number_count_list = d['number_count_list']
        if 'number_status' in d:
            o.number_status = d['number_status']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'proficiency' in d:
            o.proficiency = d['proficiency']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'schedule_status' in d:
            o.schedule_status = d['schedule_status']
        if 'title' in d:
            o.title = d['title']
        if 'week_num' in d:
            o.week_num = d['week_num']
        return o



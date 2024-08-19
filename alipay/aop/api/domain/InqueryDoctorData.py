#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InqueryDoctorData(object):

    def __init__(self):
        self._auth_status = None
        self._avator = None
        self._change_type = None
        self._department_name = None
        self._doctor_desc = None
        self._doctor_name = None
        self._educate_grade = None
        self._ext_depart_id = None
        self._ext_disease_id_list = None
        self._ext_doctor_id = None
        self._ext_hospital_id = None
        self._gender = None
        self._hospital_name = None
        self._id_no = None
        self._practice_year = None
        self._practicing_doctor_certificate_no = None
        self._skilled_desc = None
        self._skilled_disease = None
        self._special_tags = None
        self._title = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def avator(self):
        return self._avator

    @avator.setter
    def avator(self, value):
        self._avator = value
    @property
    def change_type(self):
        return self._change_type

    @change_type.setter
    def change_type(self, value):
        self._change_type = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def doctor_desc(self):
        return self._doctor_desc

    @doctor_desc.setter
    def doctor_desc(self, value):
        self._doctor_desc = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def educate_grade(self):
        return self._educate_grade

    @educate_grade.setter
    def educate_grade(self, value):
        self._educate_grade = value
    @property
    def ext_depart_id(self):
        return self._ext_depart_id

    @ext_depart_id.setter
    def ext_depart_id(self, value):
        self._ext_depart_id = value
    @property
    def ext_disease_id_list(self):
        return self._ext_disease_id_list

    @ext_disease_id_list.setter
    def ext_disease_id_list(self, value):
        if isinstance(value, list):
            self._ext_disease_id_list = list()
            for i in value:
                self._ext_disease_id_list.append(i)
    @property
    def ext_doctor_id(self):
        return self._ext_doctor_id

    @ext_doctor_id.setter
    def ext_doctor_id(self, value):
        self._ext_doctor_id = value
    @property
    def ext_hospital_id(self):
        return self._ext_hospital_id

    @ext_hospital_id.setter
    def ext_hospital_id(self, value):
        self._ext_hospital_id = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def id_no(self):
        return self._id_no

    @id_no.setter
    def id_no(self, value):
        self._id_no = value
    @property
    def practice_year(self):
        return self._practice_year

    @practice_year.setter
    def practice_year(self, value):
        self._practice_year = value
    @property
    def practicing_doctor_certificate_no(self):
        return self._practicing_doctor_certificate_no

    @practicing_doctor_certificate_no.setter
    def practicing_doctor_certificate_no(self, value):
        self._practicing_doctor_certificate_no = value
    @property
    def skilled_desc(self):
        return self._skilled_desc

    @skilled_desc.setter
    def skilled_desc(self, value):
        self._skilled_desc = value
    @property
    def skilled_disease(self):
        return self._skilled_disease

    @skilled_disease.setter
    def skilled_disease(self, value):
        self._skilled_disease = value
    @property
    def special_tags(self):
        return self._special_tags

    @special_tags.setter
    def special_tags(self, value):
        self._special_tags = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        if self.avator:
            if hasattr(self.avator, 'to_alipay_dict'):
                params['avator'] = self.avator.to_alipay_dict()
            else:
                params['avator'] = self.avator
        if self.change_type:
            if hasattr(self.change_type, 'to_alipay_dict'):
                params['change_type'] = self.change_type.to_alipay_dict()
            else:
                params['change_type'] = self.change_type
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.doctor_desc:
            if hasattr(self.doctor_desc, 'to_alipay_dict'):
                params['doctor_desc'] = self.doctor_desc.to_alipay_dict()
            else:
                params['doctor_desc'] = self.doctor_desc
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.educate_grade:
            if hasattr(self.educate_grade, 'to_alipay_dict'):
                params['educate_grade'] = self.educate_grade.to_alipay_dict()
            else:
                params['educate_grade'] = self.educate_grade
        if self.ext_depart_id:
            if hasattr(self.ext_depart_id, 'to_alipay_dict'):
                params['ext_depart_id'] = self.ext_depart_id.to_alipay_dict()
            else:
                params['ext_depart_id'] = self.ext_depart_id
        if self.ext_disease_id_list:
            if isinstance(self.ext_disease_id_list, list):
                for i in range(0, len(self.ext_disease_id_list)):
                    element = self.ext_disease_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_disease_id_list[i] = element.to_alipay_dict()
            if hasattr(self.ext_disease_id_list, 'to_alipay_dict'):
                params['ext_disease_id_list'] = self.ext_disease_id_list.to_alipay_dict()
            else:
                params['ext_disease_id_list'] = self.ext_disease_id_list
        if self.ext_doctor_id:
            if hasattr(self.ext_doctor_id, 'to_alipay_dict'):
                params['ext_doctor_id'] = self.ext_doctor_id.to_alipay_dict()
            else:
                params['ext_doctor_id'] = self.ext_doctor_id
        if self.ext_hospital_id:
            if hasattr(self.ext_hospital_id, 'to_alipay_dict'):
                params['ext_hospital_id'] = self.ext_hospital_id.to_alipay_dict()
            else:
                params['ext_hospital_id'] = self.ext_hospital_id
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.id_no:
            if hasattr(self.id_no, 'to_alipay_dict'):
                params['id_no'] = self.id_no.to_alipay_dict()
            else:
                params['id_no'] = self.id_no
        if self.practice_year:
            if hasattr(self.practice_year, 'to_alipay_dict'):
                params['practice_year'] = self.practice_year.to_alipay_dict()
            else:
                params['practice_year'] = self.practice_year
        if self.practicing_doctor_certificate_no:
            if hasattr(self.practicing_doctor_certificate_no, 'to_alipay_dict'):
                params['practicing_doctor_certificate_no'] = self.practicing_doctor_certificate_no.to_alipay_dict()
            else:
                params['practicing_doctor_certificate_no'] = self.practicing_doctor_certificate_no
        if self.skilled_desc:
            if hasattr(self.skilled_desc, 'to_alipay_dict'):
                params['skilled_desc'] = self.skilled_desc.to_alipay_dict()
            else:
                params['skilled_desc'] = self.skilled_desc
        if self.skilled_disease:
            if hasattr(self.skilled_disease, 'to_alipay_dict'):
                params['skilled_disease'] = self.skilled_disease.to_alipay_dict()
            else:
                params['skilled_disease'] = self.skilled_disease
        if self.special_tags:
            if hasattr(self.special_tags, 'to_alipay_dict'):
                params['special_tags'] = self.special_tags.to_alipay_dict()
            else:
                params['special_tags'] = self.special_tags
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InqueryDoctorData()
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'avator' in d:
            o.avator = d['avator']
        if 'change_type' in d:
            o.change_type = d['change_type']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'doctor_desc' in d:
            o.doctor_desc = d['doctor_desc']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'educate_grade' in d:
            o.educate_grade = d['educate_grade']
        if 'ext_depart_id' in d:
            o.ext_depart_id = d['ext_depart_id']
        if 'ext_disease_id_list' in d:
            o.ext_disease_id_list = d['ext_disease_id_list']
        if 'ext_doctor_id' in d:
            o.ext_doctor_id = d['ext_doctor_id']
        if 'ext_hospital_id' in d:
            o.ext_hospital_id = d['ext_hospital_id']
        if 'gender' in d:
            o.gender = d['gender']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'id_no' in d:
            o.id_no = d['id_no']
        if 'practice_year' in d:
            o.practice_year = d['practice_year']
        if 'practicing_doctor_certificate_no' in d:
            o.practicing_doctor_certificate_no = d['practicing_doctor_certificate_no']
        if 'skilled_desc' in d:
            o.skilled_desc = d['skilled_desc']
        if 'skilled_disease' in d:
            o.skilled_disease = d['skilled_disease']
        if 'special_tags' in d:
            o.special_tags = d['special_tags']
        if 'title' in d:
            o.title = d['title']
        return o



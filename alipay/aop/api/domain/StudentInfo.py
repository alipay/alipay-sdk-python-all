#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StudentInfo(object):

    def __init__(self):
        self._city_no = None
        self._class_name = None
        self._college_name = None
        self._college_no = None
        self._degree = None
        self._departments = None
        self._gmt_enrollment = None
        self._gmt_graduation = None
        self._major = None
        self._student_id = None

    @property
    def city_no(self):
        return self._city_no

    @city_no.setter
    def city_no(self, value):
        self._city_no = value
    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = value
    @property
    def college_name(self):
        return self._college_name

    @college_name.setter
    def college_name(self, value):
        self._college_name = value
    @property
    def college_no(self):
        return self._college_no

    @college_no.setter
    def college_no(self, value):
        self._college_no = value
    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        self._degree = value
    @property
    def departments(self):
        return self._departments

    @departments.setter
    def departments(self, value):
        self._departments = value
    @property
    def gmt_enrollment(self):
        return self._gmt_enrollment

    @gmt_enrollment.setter
    def gmt_enrollment(self, value):
        self._gmt_enrollment = value
    @property
    def gmt_graduation(self):
        return self._gmt_graduation

    @gmt_graduation.setter
    def gmt_graduation(self, value):
        self._gmt_graduation = value
    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_no:
            if hasattr(self.city_no, 'to_alipay_dict'):
                params['city_no'] = self.city_no.to_alipay_dict()
            else:
                params['city_no'] = self.city_no
        if self.class_name:
            if hasattr(self.class_name, 'to_alipay_dict'):
                params['class_name'] = self.class_name.to_alipay_dict()
            else:
                params['class_name'] = self.class_name
        if self.college_name:
            if hasattr(self.college_name, 'to_alipay_dict'):
                params['college_name'] = self.college_name.to_alipay_dict()
            else:
                params['college_name'] = self.college_name
        if self.college_no:
            if hasattr(self.college_no, 'to_alipay_dict'):
                params['college_no'] = self.college_no.to_alipay_dict()
            else:
                params['college_no'] = self.college_no
        if self.degree:
            if hasattr(self.degree, 'to_alipay_dict'):
                params['degree'] = self.degree.to_alipay_dict()
            else:
                params['degree'] = self.degree
        if self.departments:
            if hasattr(self.departments, 'to_alipay_dict'):
                params['departments'] = self.departments.to_alipay_dict()
            else:
                params['departments'] = self.departments
        if self.gmt_enrollment:
            if hasattr(self.gmt_enrollment, 'to_alipay_dict'):
                params['gmt_enrollment'] = self.gmt_enrollment.to_alipay_dict()
            else:
                params['gmt_enrollment'] = self.gmt_enrollment
        if self.gmt_graduation:
            if hasattr(self.gmt_graduation, 'to_alipay_dict'):
                params['gmt_graduation'] = self.gmt_graduation.to_alipay_dict()
            else:
                params['gmt_graduation'] = self.gmt_graduation
        if self.major:
            if hasattr(self.major, 'to_alipay_dict'):
                params['major'] = self.major.to_alipay_dict()
            else:
                params['major'] = self.major
        if self.student_id:
            if hasattr(self.student_id, 'to_alipay_dict'):
                params['student_id'] = self.student_id.to_alipay_dict()
            else:
                params['student_id'] = self.student_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StudentInfo()
        if 'city_no' in d:
            o.city_no = d['city_no']
        if 'class_name' in d:
            o.class_name = d['class_name']
        if 'college_name' in d:
            o.college_name = d['college_name']
        if 'college_no' in d:
            o.college_no = d['college_no']
        if 'degree' in d:
            o.degree = d['degree']
        if 'departments' in d:
            o.departments = d['departments']
        if 'gmt_enrollment' in d:
            o.gmt_enrollment = d['gmt_enrollment']
        if 'gmt_graduation' in d:
            o.gmt_graduation = d['gmt_graduation']
        if 'major' in d:
            o.major = d['major']
        if 'student_id' in d:
            o.student_id = d['student_id']
        return o



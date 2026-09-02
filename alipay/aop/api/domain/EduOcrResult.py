#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduOcrResult(object):

    def __init__(self):
        self._birthday = None
        self._cert_no = None
        self._edu_category = None
        self._edu_level = None
        self._enroll_date = None
        self._gender = None
        self._graduate_conclusion = None
        self._graduate_date = None
        self._major = None
        self._name = None
        self._school = None
        self._study_duration = None
        self._training_mode = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def edu_category(self):
        return self._edu_category

    @edu_category.setter
    def edu_category(self, value):
        self._edu_category = value
    @property
    def edu_level(self):
        return self._edu_level

    @edu_level.setter
    def edu_level(self, value):
        self._edu_level = value
    @property
    def enroll_date(self):
        return self._enroll_date

    @enroll_date.setter
    def enroll_date(self, value):
        self._enroll_date = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def graduate_conclusion(self):
        return self._graduate_conclusion

    @graduate_conclusion.setter
    def graduate_conclusion(self, value):
        self._graduate_conclusion = value
    @property
    def graduate_date(self):
        return self._graduate_date

    @graduate_date.setter
    def graduate_date(self, value):
        self._graduate_date = value
    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, value):
        self._school = value
    @property
    def study_duration(self):
        return self._study_duration

    @study_duration.setter
    def study_duration(self, value):
        self._study_duration = value
    @property
    def training_mode(self):
        return self._training_mode

    @training_mode.setter
    def training_mode(self, value):
        self._training_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.edu_category:
            if hasattr(self.edu_category, 'to_alipay_dict'):
                params['edu_category'] = self.edu_category.to_alipay_dict()
            else:
                params['edu_category'] = self.edu_category
        if self.edu_level:
            if hasattr(self.edu_level, 'to_alipay_dict'):
                params['edu_level'] = self.edu_level.to_alipay_dict()
            else:
                params['edu_level'] = self.edu_level
        if self.enroll_date:
            if hasattr(self.enroll_date, 'to_alipay_dict'):
                params['enroll_date'] = self.enroll_date.to_alipay_dict()
            else:
                params['enroll_date'] = self.enroll_date
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.graduate_conclusion:
            if hasattr(self.graduate_conclusion, 'to_alipay_dict'):
                params['graduate_conclusion'] = self.graduate_conclusion.to_alipay_dict()
            else:
                params['graduate_conclusion'] = self.graduate_conclusion
        if self.graduate_date:
            if hasattr(self.graduate_date, 'to_alipay_dict'):
                params['graduate_date'] = self.graduate_date.to_alipay_dict()
            else:
                params['graduate_date'] = self.graduate_date
        if self.major:
            if hasattr(self.major, 'to_alipay_dict'):
                params['major'] = self.major.to_alipay_dict()
            else:
                params['major'] = self.major
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.school:
            if hasattr(self.school, 'to_alipay_dict'):
                params['school'] = self.school.to_alipay_dict()
            else:
                params['school'] = self.school
        if self.study_duration:
            if hasattr(self.study_duration, 'to_alipay_dict'):
                params['study_duration'] = self.study_duration.to_alipay_dict()
            else:
                params['study_duration'] = self.study_duration
        if self.training_mode:
            if hasattr(self.training_mode, 'to_alipay_dict'):
                params['training_mode'] = self.training_mode.to_alipay_dict()
            else:
                params['training_mode'] = self.training_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduOcrResult()
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'edu_category' in d:
            o.edu_category = d['edu_category']
        if 'edu_level' in d:
            o.edu_level = d['edu_level']
        if 'enroll_date' in d:
            o.enroll_date = d['enroll_date']
        if 'gender' in d:
            o.gender = d['gender']
        if 'graduate_conclusion' in d:
            o.graduate_conclusion = d['graduate_conclusion']
        if 'graduate_date' in d:
            o.graduate_date = d['graduate_date']
        if 'major' in d:
            o.major = d['major']
        if 'name' in d:
            o.name = d['name']
        if 'school' in d:
            o.school = d['school']
        if 'study_duration' in d:
            o.study_duration = d['study_duration']
        if 'training_mode' in d:
            o.training_mode = d['training_mode']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JobworthAdapter(object):

    def __init__(self):
        self._age = None
        self._city = None
        self._edu_level = None
        self._gender = None
        self._recommend = None
        self._skill_certificate = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def edu_level(self):
        return self._edu_level

    @edu_level.setter
    def edu_level(self, value):
        self._edu_level = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def recommend(self):
        return self._recommend

    @recommend.setter
    def recommend(self, value):
        self._recommend = value
    @property
    def skill_certificate(self):
        return self._skill_certificate

    @skill_certificate.setter
    def skill_certificate(self, value):
        self._skill_certificate = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.edu_level:
            if hasattr(self.edu_level, 'to_alipay_dict'):
                params['edu_level'] = self.edu_level.to_alipay_dict()
            else:
                params['edu_level'] = self.edu_level
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.recommend:
            if hasattr(self.recommend, 'to_alipay_dict'):
                params['recommend'] = self.recommend.to_alipay_dict()
            else:
                params['recommend'] = self.recommend
        if self.skill_certificate:
            if hasattr(self.skill_certificate, 'to_alipay_dict'):
                params['skill_certificate'] = self.skill_certificate.to_alipay_dict()
            else:
                params['skill_certificate'] = self.skill_certificate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JobworthAdapter()
        if 'age' in d:
            o.age = d['age']
        if 'city' in d:
            o.city = d['city']
        if 'edu_level' in d:
            o.edu_level = d['edu_level']
        if 'gender' in d:
            o.gender = d['gender']
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'skill_certificate' in d:
            o.skill_certificate = d['skill_certificate']
        return o



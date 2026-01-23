#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BingLiInfo(object):

    def __init__(self):
        self._age = None
        self._birthday = None
        self._disease_detail = None
        self._disease_name = None
        self._gender = None
        self._name = None
        self._report_type = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def disease_detail(self):
        return self._disease_detail

    @disease_detail.setter
    def disease_detail(self, value):
        self._disease_detail = value
    @property
    def disease_name(self):
        return self._disease_name

    @disease_name.setter
    def disease_name(self, value):
        self._disease_name = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.disease_detail:
            if hasattr(self.disease_detail, 'to_alipay_dict'):
                params['disease_detail'] = self.disease_detail.to_alipay_dict()
            else:
                params['disease_detail'] = self.disease_detail
        if self.disease_name:
            if hasattr(self.disease_name, 'to_alipay_dict'):
                params['disease_name'] = self.disease_name.to_alipay_dict()
            else:
                params['disease_name'] = self.disease_name
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BingLiInfo()
        if 'age' in d:
            o.age = d['age']
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'disease_detail' in d:
            o.disease_detail = d['disease_detail']
        if 'disease_name' in d:
            o.disease_name = d['disease_name']
        if 'gender' in d:
            o.gender = d['gender']
        if 'name' in d:
            o.name = d['name']
        if 'report_type' in d:
            o.report_type = d['report_type']
        return o



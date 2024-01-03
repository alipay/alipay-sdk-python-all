#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CissExerciseReportRecord import CissExerciseReportRecord
from alipay.aop.api.domain.CissSportsGuidance import CissSportsGuidance


class AlipayUserSportshealthCissexerciseSubmitModel(object):

    def __init__(self):
        self._age = None
        self._age_group = None
        self._date = None
        self._exercise_data = None
        self._identification_number = None
        self._openid = None
        self._sex = None
        self._sports_guidance = None
        self._user_id = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def age_group(self):
        return self._age_group

    @age_group.setter
    def age_group(self, value):
        self._age_group = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def exercise_data(self):
        return self._exercise_data

    @exercise_data.setter
    def exercise_data(self, value):
        if isinstance(value, list):
            self._exercise_data = list()
            for i in value:
                if isinstance(i, CissExerciseReportRecord):
                    self._exercise_data.append(i)
                else:
                    self._exercise_data.append(CissExerciseReportRecord.from_alipay_dict(i))
    @property
    def identification_number(self):
        return self._identification_number

    @identification_number.setter
    def identification_number(self, value):
        self._identification_number = value
    @property
    def openid(self):
        return self._openid

    @openid.setter
    def openid(self, value):
        self._openid = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def sports_guidance(self):
        return self._sports_guidance

    @sports_guidance.setter
    def sports_guidance(self, value):
        if isinstance(value, list):
            self._sports_guidance = list()
            for i in value:
                if isinstance(i, CissSportsGuidance):
                    self._sports_guidance.append(i)
                else:
                    self._sports_guidance.append(CissSportsGuidance.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.age_group:
            if hasattr(self.age_group, 'to_alipay_dict'):
                params['age_group'] = self.age_group.to_alipay_dict()
            else:
                params['age_group'] = self.age_group
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.exercise_data:
            if isinstance(self.exercise_data, list):
                for i in range(0, len(self.exercise_data)):
                    element = self.exercise_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exercise_data[i] = element.to_alipay_dict()
            if hasattr(self.exercise_data, 'to_alipay_dict'):
                params['exercise_data'] = self.exercise_data.to_alipay_dict()
            else:
                params['exercise_data'] = self.exercise_data
        if self.identification_number:
            if hasattr(self.identification_number, 'to_alipay_dict'):
                params['identification_number'] = self.identification_number.to_alipay_dict()
            else:
                params['identification_number'] = self.identification_number
        if self.openid:
            if hasattr(self.openid, 'to_alipay_dict'):
                params['openid'] = self.openid.to_alipay_dict()
            else:
                params['openid'] = self.openid
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        if self.sports_guidance:
            if isinstance(self.sports_guidance, list):
                for i in range(0, len(self.sports_guidance)):
                    element = self.sports_guidance[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sports_guidance[i] = element.to_alipay_dict()
            if hasattr(self.sports_guidance, 'to_alipay_dict'):
                params['sports_guidance'] = self.sports_guidance.to_alipay_dict()
            else:
                params['sports_guidance'] = self.sports_guidance
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserSportshealthCissexerciseSubmitModel()
        if 'age' in d:
            o.age = d['age']
        if 'age_group' in d:
            o.age_group = d['age_group']
        if 'date' in d:
            o.date = d['date']
        if 'exercise_data' in d:
            o.exercise_data = d['exercise_data']
        if 'identification_number' in d:
            o.identification_number = d['identification_number']
        if 'openid' in d:
            o.openid = d['openid']
        if 'sex' in d:
            o.sex = d['sex']
        if 'sports_guidance' in d:
            o.sports_guidance = d['sports_guidance']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



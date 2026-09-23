#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BasicInfo(object):

    def __init__(self):
        self._age = None
        self._completed_time = None
        self._completed_type = None
        self._gender = None
        self._id_card = None
        self._interview_duration = None
        self._name = None
        self._phone = None
        self._position_name = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def completed_time(self):
        return self._completed_time

    @completed_time.setter
    def completed_time(self, value):
        self._completed_time = value
    @property
    def completed_type(self):
        return self._completed_type

    @completed_type.setter
    def completed_type(self, value):
        self._completed_type = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def interview_duration(self):
        return self._interview_duration

    @interview_duration.setter
    def interview_duration(self, value):
        self._interview_duration = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def position_name(self):
        return self._position_name

    @position_name.setter
    def position_name(self, value):
        self._position_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.completed_time:
            if hasattr(self.completed_time, 'to_alipay_dict'):
                params['completed_time'] = self.completed_time.to_alipay_dict()
            else:
                params['completed_time'] = self.completed_time
        if self.completed_type:
            if hasattr(self.completed_type, 'to_alipay_dict'):
                params['completed_type'] = self.completed_type.to_alipay_dict()
            else:
                params['completed_type'] = self.completed_type
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.interview_duration:
            if hasattr(self.interview_duration, 'to_alipay_dict'):
                params['interview_duration'] = self.interview_duration.to_alipay_dict()
            else:
                params['interview_duration'] = self.interview_duration
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.position_name:
            if hasattr(self.position_name, 'to_alipay_dict'):
                params['position_name'] = self.position_name.to_alipay_dict()
            else:
                params['position_name'] = self.position_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BasicInfo()
        if 'age' in d:
            o.age = d['age']
        if 'completed_time' in d:
            o.completed_time = d['completed_time']
        if 'completed_type' in d:
            o.completed_type = d['completed_type']
        if 'gender' in d:
            o.gender = d['gender']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'interview_duration' in d:
            o.interview_duration = d['interview_duration']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'position_name' in d:
            o.position_name = d['position_name']
        return o



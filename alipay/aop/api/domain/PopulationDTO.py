#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserConsumeLevelTagDTO import UserConsumeLevelTagDTO
from alipay.aop.api.domain.UserOccupationTagDTO import UserOccupationTagDTO
from alipay.aop.api.domain.UserAgeTagDTO import UserAgeTagDTO
from alipay.aop.api.domain.UserGenderTagDTO import UserGenderTagDTO


class PopulationDTO(object):

    def __init__(self):
        self._consume_level = None
        self._occupation = None
        self._user_age = None
        self._user_gender = None

    @property
    def consume_level(self):
        return self._consume_level

    @consume_level.setter
    def consume_level(self, value):
        if isinstance(value, list):
            self._consume_level = list()
            for i in value:
                if isinstance(i, UserConsumeLevelTagDTO):
                    self._consume_level.append(i)
                else:
                    self._consume_level.append(UserConsumeLevelTagDTO.from_alipay_dict(i))
    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, value):
        if isinstance(value, list):
            self._occupation = list()
            for i in value:
                if isinstance(i, UserOccupationTagDTO):
                    self._occupation.append(i)
                else:
                    self._occupation.append(UserOccupationTagDTO.from_alipay_dict(i))
    @property
    def user_age(self):
        return self._user_age

    @user_age.setter
    def user_age(self, value):
        if isinstance(value, list):
            self._user_age = list()
            for i in value:
                if isinstance(i, UserAgeTagDTO):
                    self._user_age.append(i)
                else:
                    self._user_age.append(UserAgeTagDTO.from_alipay_dict(i))
    @property
    def user_gender(self):
        return self._user_gender

    @user_gender.setter
    def user_gender(self, value):
        if isinstance(value, list):
            self._user_gender = list()
            for i in value:
                if isinstance(i, UserGenderTagDTO):
                    self._user_gender.append(i)
                else:
                    self._user_gender.append(UserGenderTagDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.consume_level:
            if isinstance(self.consume_level, list):
                for i in range(0, len(self.consume_level)):
                    element = self.consume_level[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.consume_level[i] = element.to_alipay_dict()
            if hasattr(self.consume_level, 'to_alipay_dict'):
                params['consume_level'] = self.consume_level.to_alipay_dict()
            else:
                params['consume_level'] = self.consume_level
        if self.occupation:
            if isinstance(self.occupation, list):
                for i in range(0, len(self.occupation)):
                    element = self.occupation[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.occupation[i] = element.to_alipay_dict()
            if hasattr(self.occupation, 'to_alipay_dict'):
                params['occupation'] = self.occupation.to_alipay_dict()
            else:
                params['occupation'] = self.occupation
        if self.user_age:
            if isinstance(self.user_age, list):
                for i in range(0, len(self.user_age)):
                    element = self.user_age[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_age[i] = element.to_alipay_dict()
            if hasattr(self.user_age, 'to_alipay_dict'):
                params['user_age'] = self.user_age.to_alipay_dict()
            else:
                params['user_age'] = self.user_age
        if self.user_gender:
            if isinstance(self.user_gender, list):
                for i in range(0, len(self.user_gender)):
                    element = self.user_gender[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_gender[i] = element.to_alipay_dict()
            if hasattr(self.user_gender, 'to_alipay_dict'):
                params['user_gender'] = self.user_gender.to_alipay_dict()
            else:
                params['user_gender'] = self.user_gender
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PopulationDTO()
        if 'consume_level' in d:
            o.consume_level = d['consume_level']
        if 'occupation' in d:
            o.occupation = d['occupation']
        if 'user_age' in d:
            o.user_age = d['user_age']
        if 'user_gender' in d:
            o.user_gender = d['user_gender']
        return o



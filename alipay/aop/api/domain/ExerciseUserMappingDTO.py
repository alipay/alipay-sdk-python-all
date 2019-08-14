#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExerciseUserMappingDTO(object):

    def __init__(self):
        self._fitness_id = None
        self._phone = None

    @property
    def fitness_id(self):
        return self._fitness_id

    @fitness_id.setter
    def fitness_id(self, value):
        self._fitness_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.fitness_id:
            if hasattr(self.fitness_id, 'to_alipay_dict'):
                params['fitness_id'] = self.fitness_id.to_alipay_dict()
            else:
                params['fitness_id'] = self.fitness_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExerciseUserMappingDTO()
        if 'fitness_id' in d:
            o.fitness_id = d['fitness_id']
        if 'phone' in d:
            o.phone = d['phone']
        return o



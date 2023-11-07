#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiUserServeInfo(object):

    def __init__(self):
        self._ability_grade = None
        self._service_capacity = None

    @property
    def ability_grade(self):
        return self._ability_grade

    @ability_grade.setter
    def ability_grade(self, value):
        self._ability_grade = value
    @property
    def service_capacity(self):
        return self._service_capacity

    @service_capacity.setter
    def service_capacity(self, value):
        self._service_capacity = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_grade:
            if hasattr(self.ability_grade, 'to_alipay_dict'):
                params['ability_grade'] = self.ability_grade.to_alipay_dict()
            else:
                params['ability_grade'] = self.ability_grade
        if self.service_capacity:
            if hasattr(self.service_capacity, 'to_alipay_dict'):
                params['service_capacity'] = self.service_capacity.to_alipay_dict()
            else:
                params['service_capacity'] = self.service_capacity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiUserServeInfo()
        if 'ability_grade' in d:
            o.ability_grade = d['ability_grade']
        if 'service_capacity' in d:
            o.service_capacity = d['service_capacity']
        return o



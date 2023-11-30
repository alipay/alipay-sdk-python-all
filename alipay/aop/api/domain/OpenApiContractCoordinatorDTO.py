#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO


class OpenApiContractCoordinatorDTO(object):

    def __init__(self):
        self._people = None
        self._role = None

    @property
    def people(self):
        return self._people

    @people.setter
    def people(self, value):
        if isinstance(value, OpenApiPersonSaDTO):
            self._people = value
        else:
            self._people = OpenApiPersonSaDTO.from_alipay_dict(value)
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value


    def to_alipay_dict(self):
        params = dict()
        if self.people:
            if hasattr(self.people, 'to_alipay_dict'):
                params['people'] = self.people.to_alipay_dict()
            else:
                params['people'] = self.people
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiContractCoordinatorDTO()
        if 'people' in d:
            o.people = d['people']
        if 'role' in d:
            o.role = d['role']
        return o



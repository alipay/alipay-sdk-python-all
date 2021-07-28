#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PetProfile import PetProfile


class PetProfiles(object):

    def __init__(self):
        self._pet_profile_list = None
        self._pet_type = None

    @property
    def pet_profile_list(self):
        return self._pet_profile_list

    @pet_profile_list.setter
    def pet_profile_list(self, value):
        if isinstance(value, list):
            self._pet_profile_list = list()
            for i in value:
                if isinstance(i, PetProfile):
                    self._pet_profile_list.append(i)
                else:
                    self._pet_profile_list.append(PetProfile.from_alipay_dict(i))
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        self._pet_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.pet_profile_list:
            if isinstance(self.pet_profile_list, list):
                for i in range(0, len(self.pet_profile_list)):
                    element = self.pet_profile_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pet_profile_list[i] = element.to_alipay_dict()
            if hasattr(self.pet_profile_list, 'to_alipay_dict'):
                params['pet_profile_list'] = self.pet_profile_list.to_alipay_dict()
            else:
                params['pet_profile_list'] = self.pet_profile_list
        if self.pet_type:
            if hasattr(self.pet_type, 'to_alipay_dict'):
                params['pet_type'] = self.pet_type.to_alipay_dict()
            else:
                params['pet_type'] = self.pet_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PetProfiles()
        if 'pet_profile_list' in d:
            o.pet_profile_list = d['pet_profile_list']
        if 'pet_type' in d:
            o.pet_type = d['pet_type']
        return o



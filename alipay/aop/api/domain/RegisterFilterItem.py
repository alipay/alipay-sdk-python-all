#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegisterFilterItem(object):

    def __init__(self):
        self._district_code_list = None
        self._hospital_level = None

    @property
    def district_code_list(self):
        return self._district_code_list

    @district_code_list.setter
    def district_code_list(self, value):
        if isinstance(value, list):
            self._district_code_list = list()
            for i in value:
                self._district_code_list.append(i)
    @property
    def hospital_level(self):
        return self._hospital_level

    @hospital_level.setter
    def hospital_level(self, value):
        if isinstance(value, list):
            self._hospital_level = list()
            for i in value:
                self._hospital_level.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.district_code_list:
            if isinstance(self.district_code_list, list):
                for i in range(0, len(self.district_code_list)):
                    element = self.district_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.district_code_list[i] = element.to_alipay_dict()
            if hasattr(self.district_code_list, 'to_alipay_dict'):
                params['district_code_list'] = self.district_code_list.to_alipay_dict()
            else:
                params['district_code_list'] = self.district_code_list
        if self.hospital_level:
            if isinstance(self.hospital_level, list):
                for i in range(0, len(self.hospital_level)):
                    element = self.hospital_level[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hospital_level[i] = element.to_alipay_dict()
            if hasattr(self.hospital_level, 'to_alipay_dict'):
                params['hospital_level'] = self.hospital_level.to_alipay_dict()
            else:
                params['hospital_level'] = self.hospital_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterFilterItem()
        if 'district_code_list' in d:
            o.district_code_list = d['district_code_list']
        if 'hospital_level' in d:
            o.hospital_level = d['hospital_level']
        return o



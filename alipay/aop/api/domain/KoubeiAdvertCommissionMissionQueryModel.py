#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiAdvertCommissionMissionQueryModel(object):

    def __init__(self):
        self._identify_list = None
        self._identify_type = None

    @property
    def identify_list(self):
        return self._identify_list

    @identify_list.setter
    def identify_list(self, value):
        if isinstance(value, list):
            self._identify_list = list()
            for i in value:
                self._identify_list.append(i)
    @property
    def identify_type(self):
        return self._identify_type

    @identify_type.setter
    def identify_type(self, value):
        self._identify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.identify_list:
            if isinstance(self.identify_list, list):
                for i in range(0, len(self.identify_list)):
                    element = self.identify_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.identify_list[i] = element.to_alipay_dict()
            if hasattr(self.identify_list, 'to_alipay_dict'):
                params['identify_list'] = self.identify_list.to_alipay_dict()
            else:
                params['identify_list'] = self.identify_list
        if self.identify_type:
            if hasattr(self.identify_type, 'to_alipay_dict'):
                params['identify_type'] = self.identify_type.to_alipay_dict()
            else:
                params['identify_type'] = self.identify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionMissionQueryModel()
        if 'identify_list' in d:
            o.identify_list = d['identify_list']
        if 'identify_type' in d:
            o.identify_type = d['identify_type']
        return o



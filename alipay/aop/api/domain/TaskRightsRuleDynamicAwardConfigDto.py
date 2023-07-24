#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DynamicAwardConfigDataDto import DynamicAwardConfigDataDto


class TaskRightsRuleDynamicAwardConfigDto(object):

    def __init__(self):
        self._data_list = None
        self._reach_always_award_count = None
        self._reach_type = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, DynamicAwardConfigDataDto):
                    self._data_list.append(i)
                else:
                    self._data_list.append(DynamicAwardConfigDataDto.from_alipay_dict(i))
    @property
    def reach_always_award_count(self):
        return self._reach_always_award_count

    @reach_always_award_count.setter
    def reach_always_award_count(self, value):
        self._reach_always_award_count = value
    @property
    def reach_type(self):
        return self._reach_type

    @reach_type.setter
    def reach_type(self, value):
        self._reach_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        if self.reach_always_award_count:
            if hasattr(self.reach_always_award_count, 'to_alipay_dict'):
                params['reach_always_award_count'] = self.reach_always_award_count.to_alipay_dict()
            else:
                params['reach_always_award_count'] = self.reach_always_award_count
        if self.reach_type:
            if hasattr(self.reach_type, 'to_alipay_dict'):
                params['reach_type'] = self.reach_type.to_alipay_dict()
            else:
                params['reach_type'] = self.reach_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskRightsRuleDynamicAwardConfigDto()
        if 'data_list' in d:
            o.data_list = d['data_list']
        if 'reach_always_award_count' in d:
            o.reach_always_award_count = d['reach_always_award_count']
        if 'reach_type' in d:
            o.reach_type = d['reach_type']
        return o



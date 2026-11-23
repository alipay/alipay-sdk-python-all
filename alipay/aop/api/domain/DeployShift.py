#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DtdeployShift import DtdeployShift


class DeployShift(object):

    def __init__(self):
        self._shift_list = None
        self._skill_group_id = None

    @property
    def shift_list(self):
        return self._shift_list

    @shift_list.setter
    def shift_list(self, value):
        if isinstance(value, list):
            self._shift_list = list()
            for i in value:
                if isinstance(i, DtdeployShift):
                    self._shift_list.append(i)
                else:
                    self._shift_list.append(DtdeployShift.from_alipay_dict(i))
    @property
    def skill_group_id(self):
        return self._skill_group_id

    @skill_group_id.setter
    def skill_group_id(self, value):
        self._skill_group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.shift_list:
            if isinstance(self.shift_list, list):
                for i in range(0, len(self.shift_list)):
                    element = self.shift_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shift_list[i] = element.to_alipay_dict()
            if hasattr(self.shift_list, 'to_alipay_dict'):
                params['shift_list'] = self.shift_list.to_alipay_dict()
            else:
                params['shift_list'] = self.shift_list
        if self.skill_group_id:
            if hasattr(self.skill_group_id, 'to_alipay_dict'):
                params['skill_group_id'] = self.skill_group_id.to_alipay_dict()
            else:
                params['skill_group_id'] = self.skill_group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeployShift()
        if 'shift_list' in d:
            o.shift_list = d['shift_list']
        if 'skill_group_id' in d:
            o.skill_group_id = d['skill_group_id']
        return o



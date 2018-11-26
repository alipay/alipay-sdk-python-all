#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AddPlanGroupResult(object):

    def __init__(self):
        self._group_id_list = None
        self._plan_id = None

    @property
    def group_id_list(self):
        return self._group_id_list

    @group_id_list.setter
    def group_id_list(self, value):
        if isinstance(value, list):
            self._group_id_list = list()
            for i in value:
                self._group_id_list.append(i)
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_id_list:
            if isinstance(self.group_id_list, list):
                for i in range(0, len(self.group_id_list)):
                    element = self.group_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_id_list[i] = element.to_alipay_dict()
            if hasattr(self.group_id_list, 'to_alipay_dict'):
                params['group_id_list'] = self.group_id_list.to_alipay_dict()
            else:
                params['group_id_list'] = self.group_id_list
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AddPlanGroupResult()
        if 'group_id_list' in d:
            o.group_id_list = d['group_id_list']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AvailableSeatModel import AvailableSeatModel


class AvailableResourceModel(object):

    def __init__(self):
        self._error_msg = None
        self._resources = None
        self._skill_group_code = None
        self._skill_group_name = None

    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        if isinstance(value, list):
            self._resources = list()
            for i in value:
                if isinstance(i, AvailableSeatModel):
                    self._resources.append(i)
                else:
                    self._resources.append(AvailableSeatModel.from_alipay_dict(i))
    @property
    def skill_group_code(self):
        return self._skill_group_code

    @skill_group_code.setter
    def skill_group_code(self, value):
        self._skill_group_code = value
    @property
    def skill_group_name(self):
        return self._skill_group_name

    @skill_group_name.setter
    def skill_group_name(self, value):
        self._skill_group_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.resources:
            if isinstance(self.resources, list):
                for i in range(0, len(self.resources)):
                    element = self.resources[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.resources[i] = element.to_alipay_dict()
            if hasattr(self.resources, 'to_alipay_dict'):
                params['resources'] = self.resources.to_alipay_dict()
            else:
                params['resources'] = self.resources
        if self.skill_group_code:
            if hasattr(self.skill_group_code, 'to_alipay_dict'):
                params['skill_group_code'] = self.skill_group_code.to_alipay_dict()
            else:
                params['skill_group_code'] = self.skill_group_code
        if self.skill_group_name:
            if hasattr(self.skill_group_name, 'to_alipay_dict'):
                params['skill_group_name'] = self.skill_group_name.to_alipay_dict()
            else:
                params['skill_group_name'] = self.skill_group_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AvailableResourceModel()
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'resources' in d:
            o.resources = d['resources']
        if 'skill_group_code' in d:
            o.skill_group_code = d['skill_group_code']
        if 'skill_group_name' in d:
            o.skill_group_name = d['skill_group_name']
        return o



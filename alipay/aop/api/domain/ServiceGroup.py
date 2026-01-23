#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgentServiceInfo import AgentServiceInfo


class ServiceGroup(object):

    def __init__(self):
        self._group_id = None
        self._group_name = None
        self._position_code = None
        self._service_list = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        self._position_code = value
    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                if isinstance(i, AgentServiceInfo):
                    self._service_list.append(i)
                else:
                    self._service_list.append(AgentServiceInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.position_code:
            if hasattr(self.position_code, 'to_alipay_dict'):
                params['position_code'] = self.position_code.to_alipay_dict()
            else:
                params['position_code'] = self.position_code
        if self.service_list:
            if isinstance(self.service_list, list):
                for i in range(0, len(self.service_list)):
                    element = self.service_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_list[i] = element.to_alipay_dict()
            if hasattr(self.service_list, 'to_alipay_dict'):
                params['service_list'] = self.service_list.to_alipay_dict()
            else:
                params['service_list'] = self.service_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceGroup()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'position_code' in d:
            o.position_code = d['position_code']
        if 'service_list' in d:
            o.service_list = d['service_list']
        return o



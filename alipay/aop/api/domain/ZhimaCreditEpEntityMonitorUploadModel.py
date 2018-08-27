#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpEntityMonitorUploadModel(object):

    def __init__(self):
        self._entity_list = None
        self._entity_type = None
        self._solution_id = None
        self._zhima_pid = None

    @property
    def entity_list(self):
        return self._entity_list

    @entity_list.setter
    def entity_list(self, value):
        self._entity_list = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value
    @property
    def zhima_pid(self):
        return self._zhima_pid

    @zhima_pid.setter
    def zhima_pid(self, value):
        self._zhima_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_list:
            if hasattr(self.entity_list, 'to_alipay_dict'):
                params['entity_list'] = self.entity_list.to_alipay_dict()
            else:
                params['entity_list'] = self.entity_list
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        if self.zhima_pid:
            if hasattr(self.zhima_pid, 'to_alipay_dict'):
                params['zhima_pid'] = self.zhima_pid.to_alipay_dict()
            else:
                params['zhima_pid'] = self.zhima_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpEntityMonitorUploadModel()
        if 'entity_list' in d:
            o.entity_list = d['entity_list']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        if 'zhima_pid' in d:
            o.zhima_pid = d['zhima_pid']
        return o



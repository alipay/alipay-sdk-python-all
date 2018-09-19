#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpEntityMonitorSetModel(object):

    def __init__(self):
        self._contact_list = None
        self._solution_id = None

    @property
    def contact_list(self):
        return self._contact_list

    @contact_list.setter
    def contact_list(self, value):
        self._contact_list = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_list:
            if hasattr(self.contact_list, 'to_alipay_dict'):
                params['contact_list'] = self.contact_list.to_alipay_dict()
            else:
                params['contact_list'] = self.contact_list
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpEntityMonitorSetModel()
        if 'contact_list' in d:
            o.contact_list = d['contact_list']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        return o



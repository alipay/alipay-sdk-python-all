#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InpatientNursingStaffInfo(object):

    def __init__(self):
        self._assignee_name = None

    @property
    def assignee_name(self):
        return self._assignee_name

    @assignee_name.setter
    def assignee_name(self, value):
        self._assignee_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.assignee_name:
            if hasattr(self.assignee_name, 'to_alipay_dict'):
                params['assignee_name'] = self.assignee_name.to_alipay_dict()
            else:
                params['assignee_name'] = self.assignee_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InpatientNursingStaffInfo()
        if 'assignee_name' in d:
            o.assignee_name = d['assignee_name']
        return o



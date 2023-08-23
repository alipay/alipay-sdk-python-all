#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AliEmployeeDTO(object):

    def __init__(self):
        self._name = None
        self._nick_name = None
        self._work_no = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AliEmployeeDTO()
        if 'name' in d:
            o.name = d['name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o



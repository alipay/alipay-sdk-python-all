#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Operator(object):

    def __init__(self):
        self._emp_id = None
        self._nick_name = None

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.emp_id:
            if hasattr(self.emp_id, 'to_alipay_dict'):
                params['emp_id'] = self.emp_id.to_alipay_dict()
            else:
                params['emp_id'] = self.emp_id
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Operator()
        if 'emp_id' in d:
            o.emp_id = d['emp_id']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        return o



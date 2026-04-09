#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Faculty(object):

    def __init__(self):
        self._faculty_id = None
        self._faculty_name = None

    @property
    def faculty_id(self):
        return self._faculty_id

    @faculty_id.setter
    def faculty_id(self, value):
        self._faculty_id = value
    @property
    def faculty_name(self):
        return self._faculty_name

    @faculty_name.setter
    def faculty_name(self, value):
        self._faculty_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.faculty_id:
            if hasattr(self.faculty_id, 'to_alipay_dict'):
                params['faculty_id'] = self.faculty_id.to_alipay_dict()
            else:
                params['faculty_id'] = self.faculty_id
        if self.faculty_name:
            if hasattr(self.faculty_name, 'to_alipay_dict'):
                params['faculty_name'] = self.faculty_name.to_alipay_dict()
            else:
                params['faculty_name'] = self.faculty_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Faculty()
        if 'faculty_id' in d:
            o.faculty_id = d['faculty_id']
        if 'faculty_name' in d:
            o.faculty_name = d['faculty_name']
        return o



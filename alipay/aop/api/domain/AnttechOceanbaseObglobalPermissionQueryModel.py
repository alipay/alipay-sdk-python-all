#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalPermissionQueryModel(object):

    def __init__(self):
        self._permission_code = None
        self._work_no = None

    @property
    def permission_code(self):
        return self._permission_code

    @permission_code.setter
    def permission_code(self, value):
        self._permission_code = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.permission_code:
            if hasattr(self.permission_code, 'to_alipay_dict'):
                params['permission_code'] = self.permission_code.to_alipay_dict()
            else:
                params['permission_code'] = self.permission_code
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
        o = AnttechOceanbaseObglobalPermissionQueryModel()
        if 'permission_code' in d:
            o.permission_code = d['permission_code']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HSchoolInfo(object):

    def __init__(self):
        self._campus_no = None
        self._school_std_code = None

    @property
    def campus_no(self):
        return self._campus_no

    @campus_no.setter
    def campus_no(self, value):
        self._campus_no = value
    @property
    def school_std_code(self):
        return self._school_std_code

    @school_std_code.setter
    def school_std_code(self, value):
        self._school_std_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.campus_no:
            if hasattr(self.campus_no, 'to_alipay_dict'):
                params['campus_no'] = self.campus_no.to_alipay_dict()
            else:
                params['campus_no'] = self.campus_no
        if self.school_std_code:
            if hasattr(self.school_std_code, 'to_alipay_dict'):
                params['school_std_code'] = self.school_std_code.to_alipay_dict()
            else:
                params['school_std_code'] = self.school_std_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HSchoolInfo()
        if 'campus_no' in d:
            o.campus_no = d['campus_no']
        if 'school_std_code' in d:
            o.school_std_code = d['school_std_code']
        return o



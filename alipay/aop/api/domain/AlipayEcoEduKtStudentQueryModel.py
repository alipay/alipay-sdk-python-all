#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduKtStudentQueryModel(object):

    def __init__(self):
        self._isv_pid = None
        self._school_no = None
        self._school_pid = None
        self._student_no = None

    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def school_no(self):
        return self._school_no

    @school_no.setter
    def school_no(self, value):
        self._school_no = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value
    @property
    def student_no(self):
        return self._student_no

    @student_no.setter
    def student_no(self, value):
        self._student_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.school_no:
            if hasattr(self.school_no, 'to_alipay_dict'):
                params['school_no'] = self.school_no.to_alipay_dict()
            else:
                params['school_no'] = self.school_no
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        if self.student_no:
            if hasattr(self.student_no, 'to_alipay_dict'):
                params['student_no'] = self.student_no.to_alipay_dict()
            else:
                params['student_no'] = self.student_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduKtStudentQueryModel()
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'school_no' in d:
            o.school_no = d['school_no']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        if 'student_no' in d:
            o.student_no = d['student_no']
        return o



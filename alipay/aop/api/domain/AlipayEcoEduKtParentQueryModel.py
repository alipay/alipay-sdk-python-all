#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduKtParentQueryModel(object):

    def __init__(self):
        self._child_name = None
        self._partner_id = None
        self._school_no = None
        self._school_pid = None
        self._student_code = None
        self._student_identify = None
        self._user_mobile = None

    @property
    def child_name(self):
        return self._child_name

    @child_name.setter
    def child_name(self, value):
        self._child_name = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
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
    def student_code(self):
        return self._student_code

    @student_code.setter
    def student_code(self, value):
        self._student_code = value
    @property
    def student_identify(self):
        return self._student_identify

    @student_identify.setter
    def student_identify(self, value):
        self._student_identify = value
    @property
    def user_mobile(self):
        return self._user_mobile

    @user_mobile.setter
    def user_mobile(self, value):
        self._user_mobile = value


    def to_alipay_dict(self):
        params = dict()
        if self.child_name:
            if hasattr(self.child_name, 'to_alipay_dict'):
                params['child_name'] = self.child_name.to_alipay_dict()
            else:
                params['child_name'] = self.child_name
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
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
        if self.student_code:
            if hasattr(self.student_code, 'to_alipay_dict'):
                params['student_code'] = self.student_code.to_alipay_dict()
            else:
                params['student_code'] = self.student_code
        if self.student_identify:
            if hasattr(self.student_identify, 'to_alipay_dict'):
                params['student_identify'] = self.student_identify.to_alipay_dict()
            else:
                params['student_identify'] = self.student_identify
        if self.user_mobile:
            if hasattr(self.user_mobile, 'to_alipay_dict'):
                params['user_mobile'] = self.user_mobile.to_alipay_dict()
            else:
                params['user_mobile'] = self.user_mobile
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduKtParentQueryModel()
        if 'child_name' in d:
            o.child_name = d['child_name']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'school_no' in d:
            o.school_no = d['school_no']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        if 'student_code' in d:
            o.student_code = d['student_code']
        if 'student_identify' in d:
            o.student_identify = d['student_identify']
        if 'user_mobile' in d:
            o.user_mobile = d['user_mobile']
        return o



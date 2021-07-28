#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SchoolCardSimpleInfo(object):

    def __init__(self):
        self._school_id = None
        self._school_name = None
        self._school_stdcode = None
        self._short_code = None
        self._status = None

    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def school_stdcode(self):
        return self._school_stdcode

    @school_stdcode.setter
    def school_stdcode(self, value):
        self._school_stdcode = value
    @property
    def short_code(self):
        return self._short_code

    @short_code.setter
    def short_code(self, value):
        self._short_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.school_id:
            if hasattr(self.school_id, 'to_alipay_dict'):
                params['school_id'] = self.school_id.to_alipay_dict()
            else:
                params['school_id'] = self.school_id
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.school_stdcode:
            if hasattr(self.school_stdcode, 'to_alipay_dict'):
                params['school_stdcode'] = self.school_stdcode.to_alipay_dict()
            else:
                params['school_stdcode'] = self.school_stdcode
        if self.short_code:
            if hasattr(self.short_code, 'to_alipay_dict'):
                params['short_code'] = self.short_code.to_alipay_dict()
            else:
                params['short_code'] = self.short_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SchoolCardSimpleInfo()
        if 'school_id' in d:
            o.school_id = d['school_id']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'school_stdcode' in d:
            o.school_stdcode = d['school_stdcode']
        if 'short_code' in d:
            o.short_code = d['short_code']
        if 'status' in d:
            o.status = d['status']
        return o



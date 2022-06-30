#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SchoolCard(object):

    def __init__(self):
        self._name = None
        self._protocol_status = None
        self._schema_url = None
        self._school_id = None
        self._student_id = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def protocol_status(self):
        return self._protocol_status

    @protocol_status.setter
    def protocol_status(self, value):
        self._protocol_status = value
    @property
    def schema_url(self):
        return self._schema_url

    @schema_url.setter
    def schema_url(self, value):
        self._schema_url = value
    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.protocol_status:
            if hasattr(self.protocol_status, 'to_alipay_dict'):
                params['protocol_status'] = self.protocol_status.to_alipay_dict()
            else:
                params['protocol_status'] = self.protocol_status
        if self.schema_url:
            if hasattr(self.schema_url, 'to_alipay_dict'):
                params['schema_url'] = self.schema_url.to_alipay_dict()
            else:
                params['schema_url'] = self.schema_url
        if self.school_id:
            if hasattr(self.school_id, 'to_alipay_dict'):
                params['school_id'] = self.school_id.to_alipay_dict()
            else:
                params['school_id'] = self.school_id
        if self.student_id:
            if hasattr(self.student_id, 'to_alipay_dict'):
                params['student_id'] = self.student_id.to_alipay_dict()
            else:
                params['student_id'] = self.student_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SchoolCard()
        if 'name' in d:
            o.name = d['name']
        if 'protocol_status' in d:
            o.protocol_status = d['protocol_status']
        if 'schema_url' in d:
            o.schema_url = d['schema_url']
        if 'school_id' in d:
            o.school_id = d['school_id']
        if 'student_id' in d:
            o.student_id = d['student_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryOfflinelaborProjectCreateModel(object):

    def __init__(self):
        self._edu_level = None
        self._experience_level = None
        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._project_id = None
        self._project_name = None

    @property
    def edu_level(self):
        return self._edu_level

    @edu_level.setter
    def edu_level(self, value):
        self._edu_level = value
    @property
    def experience_level(self):
        return self._experience_level

    @experience_level.setter
    def experience_level(self, value):
        self._experience_level = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, value):
        self._job_type = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.edu_level:
            if hasattr(self.edu_level, 'to_alipay_dict'):
                params['edu_level'] = self.edu_level.to_alipay_dict()
            else:
                params['edu_level'] = self.edu_level
        if self.experience_level:
            if hasattr(self.experience_level, 'to_alipay_dict'):
                params['experience_level'] = self.experience_level.to_alipay_dict()
            else:
                params['experience_level'] = self.experience_level
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.job_type:
            if hasattr(self.job_type, 'to_alipay_dict'):
                params['job_type'] = self.job_type.to_alipay_dict()
            else:
                params['job_type'] = self.job_type
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryOfflinelaborProjectCreateModel()
        if 'edu_level' in d:
            o.edu_level = d['edu_level']
        if 'experience_level' in d:
            o.experience_level = d['experience_level']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'job_type' in d:
            o.job_type = d['job_type']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_name' in d:
            o.project_name = d['project_name']
        return o



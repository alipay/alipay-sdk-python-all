#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenapiInterviewJobInfoDTO(object):

    def __init__(self):
        self._job_description = None
        self._job_name = None
        self._job_requirement = None

    @property
    def job_description(self):
        return self._job_description

    @job_description.setter
    def job_description(self, value):
        self._job_description = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def job_requirement(self):
        return self._job_requirement

    @job_requirement.setter
    def job_requirement(self, value):
        self._job_requirement = value


    def to_alipay_dict(self):
        params = dict()
        if self.job_description:
            if hasattr(self.job_description, 'to_alipay_dict'):
                params['job_description'] = self.job_description.to_alipay_dict()
            else:
                params['job_description'] = self.job_description
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.job_requirement:
            if hasattr(self.job_requirement, 'to_alipay_dict'):
                params['job_requirement'] = self.job_requirement.to_alipay_dict()
            else:
                params['job_requirement'] = self.job_requirement
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenapiInterviewJobInfoDTO()
        if 'job_description' in d:
            o.job_description = d['job_description']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'job_requirement' in d:
            o.job_requirement = d['job_requirement']
        return o



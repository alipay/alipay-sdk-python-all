#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceMindvJobCreateModel(object):

    def __init__(self):
        self._job_domain = None
        self._staff_no = None
        self._title = None
        self._type = None

    @property
    def job_domain(self):
        return self._job_domain

    @job_domain.setter
    def job_domain(self, value):
        self._job_domain = value
    @property
    def staff_no(self):
        return self._staff_no

    @staff_no.setter
    def staff_no(self, value):
        self._staff_no = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.job_domain:
            if hasattr(self.job_domain, 'to_alipay_dict'):
                params['job_domain'] = self.job_domain.to_alipay_dict()
            else:
                params['job_domain'] = self.job_domain
        if self.staff_no:
            if hasattr(self.staff_no, 'to_alipay_dict'):
                params['staff_no'] = self.staff_no.to_alipay_dict()
            else:
                params['staff_no'] = self.staff_no
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceMindvJobCreateModel()
        if 'job_domain' in d:
            o.job_domain = d['job_domain']
        if 'staff_no' in d:
            o.staff_no = d['staff_no']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o



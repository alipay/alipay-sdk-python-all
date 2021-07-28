#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitPlanLight(object):

    def __init__(self):
        self._description = None
        self._enroll_end_time = None
        self._enroll_start_time = None
        self._logo = None
        self._plan_id = None
        self._plan_name = None
        self._status = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def enroll_end_time(self):
        return self._enroll_end_time

    @enroll_end_time.setter
    def enroll_end_time(self, value):
        self._enroll_end_time = value
    @property
    def enroll_start_time(self):
        return self._enroll_start_time

    @enroll_start_time.setter
    def enroll_start_time(self, value):
        self._enroll_start_time = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.enroll_end_time:
            if hasattr(self.enroll_end_time, 'to_alipay_dict'):
                params['enroll_end_time'] = self.enroll_end_time.to_alipay_dict()
            else:
                params['enroll_end_time'] = self.enroll_end_time
        if self.enroll_start_time:
            if hasattr(self.enroll_start_time, 'to_alipay_dict'):
                params['enroll_start_time'] = self.enroll_start_time.to_alipay_dict()
            else:
                params['enroll_start_time'] = self.enroll_start_time
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
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
        o = RecruitPlanLight()
        if 'description' in d:
            o.description = d['description']
        if 'enroll_end_time' in d:
            o.enroll_end_time = d['enroll_end_time']
        if 'enroll_start_time' in d:
            o.enroll_start_time = d['enroll_start_time']
        if 'logo' in d:
            o.logo = d['logo']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'status' in d:
            o.status = d['status']
        return o



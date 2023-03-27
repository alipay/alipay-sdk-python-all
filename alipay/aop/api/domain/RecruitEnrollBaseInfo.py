#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitEnrollBaseInfo(object):

    def __init__(self):
        self._create_time = None
        self._enroll_id = None
        self._plan_id = None
        self._status = None
        self._status_description = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def enroll_id(self):
        return self._enroll_id

    @enroll_id.setter
    def enroll_id(self, value):
        self._enroll_id = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_description(self):
        return self._status_description

    @status_description.setter
    def status_description(self, value):
        self._status_description = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.enroll_id:
            if hasattr(self.enroll_id, 'to_alipay_dict'):
                params['enroll_id'] = self.enroll_id.to_alipay_dict()
            else:
                params['enroll_id'] = self.enroll_id
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_description:
            if hasattr(self.status_description, 'to_alipay_dict'):
                params['status_description'] = self.status_description.to_alipay_dict()
            else:
                params['status_description'] = self.status_description
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitEnrollBaseInfo()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'enroll_id' in d:
            o.enroll_id = d['enroll_id']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'status' in d:
            o.status = d['status']
        if 'status_description' in d:
            o.status_description = d['status_description']
        return o



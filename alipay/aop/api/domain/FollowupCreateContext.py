#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FollowupCreateContext(object):

    def __init__(self):
        self._candidate_name = None
        self._candidate_phone = None
        self._company = None
        self._job_title = None
        self._order_no = None
        self._stage_key = None
        self._task_deadline = None
        self._work_location = None
        self._work_time = None

    @property
    def candidate_name(self):
        return self._candidate_name

    @candidate_name.setter
    def candidate_name(self, value):
        self._candidate_name = value
    @property
    def candidate_phone(self):
        return self._candidate_phone

    @candidate_phone.setter
    def candidate_phone(self, value):
        self._candidate_phone = value
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value
    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, value):
        self._job_title = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def stage_key(self):
        return self._stage_key

    @stage_key.setter
    def stage_key(self, value):
        self._stage_key = value
    @property
    def task_deadline(self):
        return self._task_deadline

    @task_deadline.setter
    def task_deadline(self, value):
        self._task_deadline = value
    @property
    def work_location(self):
        return self._work_location

    @work_location.setter
    def work_location(self, value):
        self._work_location = value
    @property
    def work_time(self):
        return self._work_time

    @work_time.setter
    def work_time(self, value):
        self._work_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.candidate_name:
            if hasattr(self.candidate_name, 'to_alipay_dict'):
                params['candidate_name'] = self.candidate_name.to_alipay_dict()
            else:
                params['candidate_name'] = self.candidate_name
        if self.candidate_phone:
            if hasattr(self.candidate_phone, 'to_alipay_dict'):
                params['candidate_phone'] = self.candidate_phone.to_alipay_dict()
            else:
                params['candidate_phone'] = self.candidate_phone
        if self.company:
            if hasattr(self.company, 'to_alipay_dict'):
                params['company'] = self.company.to_alipay_dict()
            else:
                params['company'] = self.company
        if self.job_title:
            if hasattr(self.job_title, 'to_alipay_dict'):
                params['job_title'] = self.job_title.to_alipay_dict()
            else:
                params['job_title'] = self.job_title
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.stage_key:
            if hasattr(self.stage_key, 'to_alipay_dict'):
                params['stage_key'] = self.stage_key.to_alipay_dict()
            else:
                params['stage_key'] = self.stage_key
        if self.task_deadline:
            if hasattr(self.task_deadline, 'to_alipay_dict'):
                params['task_deadline'] = self.task_deadline.to_alipay_dict()
            else:
                params['task_deadline'] = self.task_deadline
        if self.work_location:
            if hasattr(self.work_location, 'to_alipay_dict'):
                params['work_location'] = self.work_location.to_alipay_dict()
            else:
                params['work_location'] = self.work_location
        if self.work_time:
            if hasattr(self.work_time, 'to_alipay_dict'):
                params['work_time'] = self.work_time.to_alipay_dict()
            else:
                params['work_time'] = self.work_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FollowupCreateContext()
        if 'candidate_name' in d:
            o.candidate_name = d['candidate_name']
        if 'candidate_phone' in d:
            o.candidate_phone = d['candidate_phone']
        if 'company' in d:
            o.company = d['company']
        if 'job_title' in d:
            o.job_title = d['job_title']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'stage_key' in d:
            o.stage_key = d['stage_key']
        if 'task_deadline' in d:
            o.task_deadline = d['task_deadline']
        if 'work_location' in d:
            o.work_location = d['work_location']
        if 'work_time' in d:
            o.work_time = d['work_time']
        return o



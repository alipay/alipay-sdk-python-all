#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZMGOObligationConfig(object):

    def __init__(self):
        self._benefit_url = None
        self._obligation_amount = None
        self._obligation_template = None
        self._obligation_times = None
        self._promise_type_desc = None
        self._task_progress_redirect_schema = None

    @property
    def benefit_url(self):
        return self._benefit_url

    @benefit_url.setter
    def benefit_url(self, value):
        self._benefit_url = value
    @property
    def obligation_amount(self):
        return self._obligation_amount

    @obligation_amount.setter
    def obligation_amount(self, value):
        self._obligation_amount = value
    @property
    def obligation_template(self):
        return self._obligation_template

    @obligation_template.setter
    def obligation_template(self, value):
        self._obligation_template = value
    @property
    def obligation_times(self):
        return self._obligation_times

    @obligation_times.setter
    def obligation_times(self, value):
        self._obligation_times = value
    @property
    def promise_type_desc(self):
        return self._promise_type_desc

    @promise_type_desc.setter
    def promise_type_desc(self, value):
        self._promise_type_desc = value
    @property
    def task_progress_redirect_schema(self):
        return self._task_progress_redirect_schema

    @task_progress_redirect_schema.setter
    def task_progress_redirect_schema(self, value):
        self._task_progress_redirect_schema = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_url:
            if hasattr(self.benefit_url, 'to_alipay_dict'):
                params['benefit_url'] = self.benefit_url.to_alipay_dict()
            else:
                params['benefit_url'] = self.benefit_url
        if self.obligation_amount:
            if hasattr(self.obligation_amount, 'to_alipay_dict'):
                params['obligation_amount'] = self.obligation_amount.to_alipay_dict()
            else:
                params['obligation_amount'] = self.obligation_amount
        if self.obligation_template:
            if hasattr(self.obligation_template, 'to_alipay_dict'):
                params['obligation_template'] = self.obligation_template.to_alipay_dict()
            else:
                params['obligation_template'] = self.obligation_template
        if self.obligation_times:
            if hasattr(self.obligation_times, 'to_alipay_dict'):
                params['obligation_times'] = self.obligation_times.to_alipay_dict()
            else:
                params['obligation_times'] = self.obligation_times
        if self.promise_type_desc:
            if hasattr(self.promise_type_desc, 'to_alipay_dict'):
                params['promise_type_desc'] = self.promise_type_desc.to_alipay_dict()
            else:
                params['promise_type_desc'] = self.promise_type_desc
        if self.task_progress_redirect_schema:
            if hasattr(self.task_progress_redirect_schema, 'to_alipay_dict'):
                params['task_progress_redirect_schema'] = self.task_progress_redirect_schema.to_alipay_dict()
            else:
                params['task_progress_redirect_schema'] = self.task_progress_redirect_schema
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZMGOObligationConfig()
        if 'benefit_url' in d:
            o.benefit_url = d['benefit_url']
        if 'obligation_amount' in d:
            o.obligation_amount = d['obligation_amount']
        if 'obligation_template' in d:
            o.obligation_template = d['obligation_template']
        if 'obligation_times' in d:
            o.obligation_times = d['obligation_times']
        if 'promise_type_desc' in d:
            o.promise_type_desc = d['promise_type_desc']
        if 'task_progress_redirect_schema' in d:
            o.task_progress_redirect_schema = d['task_progress_redirect_schema']
        return o



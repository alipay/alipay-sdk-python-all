#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FollowupExecutionResultParams import FollowupExecutionResultParams


class FollowupExecution(object):

    def __init__(self):
        self._billable_minutes = None
        self._call_status = None
        self._execution_no = None
        self._occurred_at = None
        self._record_url = None
        self._result_params = None

    @property
    def billable_minutes(self):
        return self._billable_minutes

    @billable_minutes.setter
    def billable_minutes(self, value):
        self._billable_minutes = value
    @property
    def call_status(self):
        return self._call_status

    @call_status.setter
    def call_status(self, value):
        self._call_status = value
    @property
    def execution_no(self):
        return self._execution_no

    @execution_no.setter
    def execution_no(self, value):
        self._execution_no = value
    @property
    def occurred_at(self):
        return self._occurred_at

    @occurred_at.setter
    def occurred_at(self, value):
        self._occurred_at = value
    @property
    def record_url(self):
        return self._record_url

    @record_url.setter
    def record_url(self, value):
        self._record_url = value
    @property
    def result_params(self):
        return self._result_params

    @result_params.setter
    def result_params(self, value):
        if isinstance(value, FollowupExecutionResultParams):
            self._result_params = value
        else:
            self._result_params = FollowupExecutionResultParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.billable_minutes:
            if hasattr(self.billable_minutes, 'to_alipay_dict'):
                params['billable_minutes'] = self.billable_minutes.to_alipay_dict()
            else:
                params['billable_minutes'] = self.billable_minutes
        if self.call_status:
            if hasattr(self.call_status, 'to_alipay_dict'):
                params['call_status'] = self.call_status.to_alipay_dict()
            else:
                params['call_status'] = self.call_status
        if self.execution_no:
            if hasattr(self.execution_no, 'to_alipay_dict'):
                params['execution_no'] = self.execution_no.to_alipay_dict()
            else:
                params['execution_no'] = self.execution_no
        if self.occurred_at:
            if hasattr(self.occurred_at, 'to_alipay_dict'):
                params['occurred_at'] = self.occurred_at.to_alipay_dict()
            else:
                params['occurred_at'] = self.occurred_at
        if self.record_url:
            if hasattr(self.record_url, 'to_alipay_dict'):
                params['record_url'] = self.record_url.to_alipay_dict()
            else:
                params['record_url'] = self.record_url
        if self.result_params:
            if hasattr(self.result_params, 'to_alipay_dict'):
                params['result_params'] = self.result_params.to_alipay_dict()
            else:
                params['result_params'] = self.result_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FollowupExecution()
        if 'billable_minutes' in d:
            o.billable_minutes = d['billable_minutes']
        if 'call_status' in d:
            o.call_status = d['call_status']
        if 'execution_no' in d:
            o.execution_no = d['execution_no']
        if 'occurred_at' in d:
            o.occurred_at = d['occurred_at']
        if 'record_url' in d:
            o.record_url = d['record_url']
        if 'result_params' in d:
            o.result_params = d['result_params']
        return o



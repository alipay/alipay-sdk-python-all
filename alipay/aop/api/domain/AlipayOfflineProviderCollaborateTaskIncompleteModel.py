#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderCollaborateTaskIncompleteModel(object):

    def __init__(self):
        self._biz_time = None
        self._out_biz_no = None
        self._reason_code = None
        self._reason_desc = None
        self._reason_sub_code = None
        self._task_no = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def reason_desc(self):
        return self._reason_desc

    @reason_desc.setter
    def reason_desc(self, value):
        self._reason_desc = value
    @property
    def reason_sub_code(self):
        return self._reason_sub_code

    @reason_sub_code.setter
    def reason_sub_code(self, value):
        self._reason_sub_code = value
    @property
    def task_no(self):
        return self._task_no

    @task_no.setter
    def task_no(self, value):
        self._task_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.reason_desc:
            if hasattr(self.reason_desc, 'to_alipay_dict'):
                params['reason_desc'] = self.reason_desc.to_alipay_dict()
            else:
                params['reason_desc'] = self.reason_desc
        if self.reason_sub_code:
            if hasattr(self.reason_sub_code, 'to_alipay_dict'):
                params['reason_sub_code'] = self.reason_sub_code.to_alipay_dict()
            else:
                params['reason_sub_code'] = self.reason_sub_code
        if self.task_no:
            if hasattr(self.task_no, 'to_alipay_dict'):
                params['task_no'] = self.task_no.to_alipay_dict()
            else:
                params['task_no'] = self.task_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderCollaborateTaskIncompleteModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'reason_desc' in d:
            o.reason_desc = d['reason_desc']
        if 'reason_sub_code' in d:
            o.reason_sub_code = d['reason_sub_code']
        if 'task_no' in d:
            o.task_no = d['task_no']
        return o



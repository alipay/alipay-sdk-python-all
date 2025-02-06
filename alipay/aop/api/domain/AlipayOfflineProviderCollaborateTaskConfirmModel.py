#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderCollaborateTaskConfirmModel(object):

    def __init__(self):
        self._biz_time = None
        self._confirm_result = None
        self._out_biz_no = None
        self._task_no = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def confirm_result(self):
        return self._confirm_result

    @confirm_result.setter
    def confirm_result(self, value):
        self._confirm_result = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
        if self.confirm_result:
            if hasattr(self.confirm_result, 'to_alipay_dict'):
                params['confirm_result'] = self.confirm_result.to_alipay_dict()
            else:
                params['confirm_result'] = self.confirm_result
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayOfflineProviderCollaborateTaskConfirmModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'confirm_result' in d:
            o.confirm_result = d['confirm_result']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'task_no' in d:
            o.task_no = d['task_no']
        return o



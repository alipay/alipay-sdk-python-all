#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RobbyOpenTaskCancelModel(object):

    def __init__(self):
        self._sn = None
        self._sub_biz_no = None
        self._task_no = None

    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def sub_biz_no(self):
        return self._sub_biz_no

    @sub_biz_no.setter
    def sub_biz_no(self, value):
        self._sub_biz_no = value
    @property
    def task_no(self):
        return self._task_no

    @task_no.setter
    def task_no(self, value):
        self._task_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.sub_biz_no:
            if hasattr(self.sub_biz_no, 'to_alipay_dict'):
                params['sub_biz_no'] = self.sub_biz_no.to_alipay_dict()
            else:
                params['sub_biz_no'] = self.sub_biz_no
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
        o = RobbyOpenTaskCancelModel()
        if 'sn' in d:
            o.sn = d['sn']
        if 'sub_biz_no' in d:
            o.sub_biz_no = d['sub_biz_no']
        if 'task_no' in d:
            o.task_no = d['task_no']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CollaborateTaskCompleteContent import CollaborateTaskCompleteContent


class AlipayOfflineProviderCollaborateTaskCompleteModel(object):

    def __init__(self):
        self._biz_time = None
        self._contents = None
        self._out_biz_no = None
        self._task_no = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        if isinstance(value, list):
            self._contents = list()
            for i in value:
                if isinstance(i, CollaborateTaskCompleteContent):
                    self._contents.append(i)
                else:
                    self._contents.append(CollaborateTaskCompleteContent.from_alipay_dict(i))
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
        if self.contents:
            if isinstance(self.contents, list):
                for i in range(0, len(self.contents)):
                    element = self.contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contents[i] = element.to_alipay_dict()
            if hasattr(self.contents, 'to_alipay_dict'):
                params['contents'] = self.contents.to_alipay_dict()
            else:
                params['contents'] = self.contents
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
        o = AlipayOfflineProviderCollaborateTaskCompleteModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'contents' in d:
            o.contents = d['contents']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'task_no' in d:
            o.task_no = d['task_no']
        return o



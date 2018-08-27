#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsClaimReportProgress(object):

    def __init__(self):
        self._progress_update_content = None
        self._progress_update_time = None
        self._status = None

    @property
    def progress_update_content(self):
        return self._progress_update_content

    @progress_update_content.setter
    def progress_update_content(self, value):
        self._progress_update_content = value
    @property
    def progress_update_time(self):
        return self._progress_update_time

    @progress_update_time.setter
    def progress_update_time(self, value):
        self._progress_update_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.progress_update_content:
            if hasattr(self.progress_update_content, 'to_alipay_dict'):
                params['progress_update_content'] = self.progress_update_content.to_alipay_dict()
            else:
                params['progress_update_content'] = self.progress_update_content
        if self.progress_update_time:
            if hasattr(self.progress_update_time, 'to_alipay_dict'):
                params['progress_update_time'] = self.progress_update_time.to_alipay_dict()
            else:
                params['progress_update_time'] = self.progress_update_time
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
        o = InsClaimReportProgress()
        if 'progress_update_content' in d:
            o.progress_update_content = d['progress_update_content']
        if 'progress_update_time' in d:
            o.progress_update_time = d['progress_update_time']
        if 'status' in d:
            o.status = d['status']
        return o



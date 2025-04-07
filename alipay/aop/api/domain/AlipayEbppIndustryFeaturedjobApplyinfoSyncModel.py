#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryFeaturedjobApplyinfoSyncModel(object):

    def __init__(self):
        self._apply_change_time = None
        self._apply_id = None
        self._apply_status = None
        self._apply_time = None
        self._job_id = None

    @property
    def apply_change_time(self):
        return self._apply_change_time

    @apply_change_time.setter
    def apply_change_time(self, value):
        self._apply_change_time = value
    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_change_time:
            if hasattr(self.apply_change_time, 'to_alipay_dict'):
                params['apply_change_time'] = self.apply_change_time.to_alipay_dict()
            else:
                params['apply_change_time'] = self.apply_change_time
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryFeaturedjobApplyinfoSyncModel()
        if 'apply_change_time' in d:
            o.apply_change_time = d['apply_change_time']
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'job_id' in d:
            o.job_id = d['job_id']
        return o



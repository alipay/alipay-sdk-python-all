#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryJobApplySyncModel(object):

    def __init__(self):
        self._apply_change_time = None
        self._apply_info_url = None
        self._apply_status = None
        self._apply_time = None
        self._out_apply_id = None
        self._out_job_id = None

    @property
    def apply_change_time(self):
        return self._apply_change_time

    @apply_change_time.setter
    def apply_change_time(self, value):
        self._apply_change_time = value
    @property
    def apply_info_url(self):
        return self._apply_info_url

    @apply_info_url.setter
    def apply_info_url(self, value):
        self._apply_info_url = value
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
    def out_apply_id(self):
        return self._out_apply_id

    @out_apply_id.setter
    def out_apply_id(self, value):
        self._out_apply_id = value
    @property
    def out_job_id(self):
        return self._out_job_id

    @out_job_id.setter
    def out_job_id(self, value):
        self._out_job_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_change_time:
            if hasattr(self.apply_change_time, 'to_alipay_dict'):
                params['apply_change_time'] = self.apply_change_time.to_alipay_dict()
            else:
                params['apply_change_time'] = self.apply_change_time
        if self.apply_info_url:
            if hasattr(self.apply_info_url, 'to_alipay_dict'):
                params['apply_info_url'] = self.apply_info_url.to_alipay_dict()
            else:
                params['apply_info_url'] = self.apply_info_url
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
        if self.out_apply_id:
            if hasattr(self.out_apply_id, 'to_alipay_dict'):
                params['out_apply_id'] = self.out_apply_id.to_alipay_dict()
            else:
                params['out_apply_id'] = self.out_apply_id
        if self.out_job_id:
            if hasattr(self.out_job_id, 'to_alipay_dict'):
                params['out_job_id'] = self.out_job_id.to_alipay_dict()
            else:
                params['out_job_id'] = self.out_job_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryJobApplySyncModel()
        if 'apply_change_time' in d:
            o.apply_change_time = d['apply_change_time']
        if 'apply_info_url' in d:
            o.apply_info_url = d['apply_info_url']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'out_apply_id' in d:
            o.out_apply_id = d['out_apply_id']
        if 'out_job_id' in d:
            o.out_job_id = d['out_job_id']
        return o



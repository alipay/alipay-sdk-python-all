#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePropertyCheckinConfigSetModel(object):

    def __init__(self):
        self._clock_url = None
        self._job_id = None

    @property
    def clock_url(self):
        return self._clock_url

    @clock_url.setter
    def clock_url(self, value):
        self._clock_url = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.clock_url:
            if hasattr(self.clock_url, 'to_alipay_dict'):
                params['clock_url'] = self.clock_url.to_alipay_dict()
            else:
                params['clock_url'] = self.clock_url
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
        o = AlipayCommercePropertyCheckinConfigSetModel()
        if 'clock_url' in d:
            o.clock_url = d['clock_url']
        if 'job_id' in d:
            o.job_id = d['job_id']
        return o



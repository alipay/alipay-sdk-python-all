#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceUsedMetric(object):

    def __init__(self):
        self._service_name = None
        self._service_used_cnt = None

    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_used_cnt(self):
        return self._service_used_cnt

    @service_used_cnt.setter
    def service_used_cnt(self, value):
        self._service_used_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_used_cnt:
            if hasattr(self.service_used_cnt, 'to_alipay_dict'):
                params['service_used_cnt'] = self.service_used_cnt.to_alipay_dict()
            else:
                params['service_used_cnt'] = self.service_used_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceUsedMetric()
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_used_cnt' in d:
            o.service_used_cnt = d['service_used_cnt']
        return o



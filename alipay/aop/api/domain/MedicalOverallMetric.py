#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalOverallMetric(object):

    def __init__(self):
        self._avg_service_pv_30d = None

    @property
    def avg_service_pv_30d(self):
        return self._avg_service_pv_30d

    @avg_service_pv_30d.setter
    def avg_service_pv_30d(self, value):
        self._avg_service_pv_30d = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_service_pv_30d:
            if hasattr(self.avg_service_pv_30d, 'to_alipay_dict'):
                params['avg_service_pv_30d'] = self.avg_service_pv_30d.to_alipay_dict()
            else:
                params['avg_service_pv_30d'] = self.avg_service_pv_30d
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalOverallMetric()
        if 'avg_service_pv_30d' in d:
            o.avg_service_pv_30d = d['avg_service_pv_30d']
        return o



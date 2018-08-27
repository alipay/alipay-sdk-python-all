#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingDataDashboardApplyModel(object):

    def __init__(self):
        self._dashboard_ids = None

    @property
    def dashboard_ids(self):
        return self._dashboard_ids

    @dashboard_ids.setter
    def dashboard_ids(self, value):
        if isinstance(value, list):
            self._dashboard_ids = list()
            for i in value:
                self._dashboard_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.dashboard_ids:
            if isinstance(self.dashboard_ids, list):
                for i in range(0, len(self.dashboard_ids)):
                    element = self.dashboard_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dashboard_ids[i] = element.to_alipay_dict()
            if hasattr(self.dashboard_ids, 'to_alipay_dict'):
                params['dashboard_ids'] = self.dashboard_ids.to_alipay_dict()
            else:
                params['dashboard_ids'] = self.dashboard_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingDataDashboardApplyModel()
        if 'dashboard_ids' in d:
            o.dashboard_ids = d['dashboard_ids']
        return o



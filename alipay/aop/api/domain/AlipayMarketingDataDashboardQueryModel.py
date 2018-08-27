#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DashboardParam import DashboardParam


class AlipayMarketingDataDashboardQueryModel(object):

    def __init__(self):
        self._dashboard_id = None
        self._param = None

    @property
    def dashboard_id(self):
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, value):
        self._dashboard_id = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        if isinstance(value, list):
            self._param = list()
            for i in value:
                if isinstance(i, DashboardParam):
                    self._param.append(i)
                else:
                    self._param.append(DashboardParam.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.dashboard_id:
            if hasattr(self.dashboard_id, 'to_alipay_dict'):
                params['dashboard_id'] = self.dashboard_id.to_alipay_dict()
            else:
                params['dashboard_id'] = self.dashboard_id
        if self.param:
            if isinstance(self.param, list):
                for i in range(0, len(self.param)):
                    element = self.param[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.param[i] = element.to_alipay_dict()
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingDataDashboardQueryModel()
        if 'dashboard_id' in d:
            o.dashboard_id = d['dashboard_id']
        if 'param' in d:
            o.param = d['param']
        return o



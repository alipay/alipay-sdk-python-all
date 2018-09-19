#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ISVLogSync import ISVLogSync


class AlipayOfflineProviderMonitorLogSyncModel(object):

    def __init__(self):
        self._logs = None

    @property
    def logs(self):
        return self._logs

    @logs.setter
    def logs(self, value):
        if isinstance(value, list):
            self._logs = list()
            for i in value:
                if isinstance(i, ISVLogSync):
                    self._logs.append(i)
                else:
                    self._logs.append(ISVLogSync.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.logs:
            if isinstance(self.logs, list):
                for i in range(0, len(self.logs)):
                    element = self.logs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logs[i] = element.to_alipay_dict()
            if hasattr(self.logs, 'to_alipay_dict'):
                params['logs'] = self.logs.to_alipay_dict()
            else:
                params['logs'] = self.logs
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderMonitorLogSyncModel()
        if 'logs' in d:
            o.logs = d['logs']
        return o



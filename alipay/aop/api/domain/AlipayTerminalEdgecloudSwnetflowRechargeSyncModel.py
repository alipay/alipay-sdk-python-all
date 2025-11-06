#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTerminalEdgecloudSwnetflowRechargeSyncModel(object):

    def __init__(self):
        self._status = None
        self._trace_no = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trace_no(self):
        return self._trace_no

    @trace_no.setter
    def trace_no(self, value):
        self._trace_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trace_no:
            if hasattr(self.trace_no, 'to_alipay_dict'):
                params['trace_no'] = self.trace_no.to_alipay_dict()
            else:
                params['trace_no'] = self.trace_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTerminalEdgecloudSwnetflowRechargeSyncModel()
        if 'status' in d:
            o.status = d['status']
        if 'trace_no' in d:
            o.trace_no = d['trace_no']
        return o



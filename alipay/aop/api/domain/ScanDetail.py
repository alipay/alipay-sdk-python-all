#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScanDetail(object):

    def __init__(self):
        self._scan_report = None
        self._scan_state = None
        self._scan_type = None

    @property
    def scan_report(self):
        return self._scan_report

    @scan_report.setter
    def scan_report(self, value):
        self._scan_report = value
    @property
    def scan_state(self):
        return self._scan_state

    @scan_state.setter
    def scan_state(self, value):
        self._scan_state = value
    @property
    def scan_type(self):
        return self._scan_type

    @scan_type.setter
    def scan_type(self, value):
        self._scan_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.scan_report:
            if hasattr(self.scan_report, 'to_alipay_dict'):
                params['scan_report'] = self.scan_report.to_alipay_dict()
            else:
                params['scan_report'] = self.scan_report
        if self.scan_state:
            if hasattr(self.scan_state, 'to_alipay_dict'):
                params['scan_state'] = self.scan_state.to_alipay_dict()
            else:
                params['scan_state'] = self.scan_state
        if self.scan_type:
            if hasattr(self.scan_type, 'to_alipay_dict'):
                params['scan_type'] = self.scan_type.to_alipay_dict()
            else:
                params['scan_type'] = self.scan_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScanDetail()
        if 'scan_report' in d:
            o.scan_report = d['scan_report']
        if 'scan_state' in d:
            o.scan_state = d['scan_state']
        if 'scan_type' in d:
            o.scan_type = d['scan_type']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportResult(object):

    def __init__(self):
        self._case_summary = None
        self._kv = None
        self._report_type = None
        self._sub_type = None

    @property
    def case_summary(self):
        return self._case_summary

    @case_summary.setter
    def case_summary(self, value):
        self._case_summary = value
    @property
    def kv(self):
        return self._kv

    @kv.setter
    def kv(self, value):
        self._kv = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_summary:
            if hasattr(self.case_summary, 'to_alipay_dict'):
                params['case_summary'] = self.case_summary.to_alipay_dict()
            else:
                params['case_summary'] = self.case_summary
        if self.kv:
            if hasattr(self.kv, 'to_alipay_dict'):
                params['kv'] = self.kv.to_alipay_dict()
            else:
                params['kv'] = self.kv
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportResult()
        if 'case_summary' in d:
            o.case_summary = d['case_summary']
        if 'kv' in d:
            o.kv = d['kv']
        if 'report_type' in d:
            o.report_type = d['report_type']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        return o



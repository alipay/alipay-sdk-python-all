#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportConfig(object):

    def __init__(self):
        self._job_codes = None
        self._link_url = None
        self._report_type = None

    @property
    def job_codes(self):
        return self._job_codes

    @job_codes.setter
    def job_codes(self, value):
        if isinstance(value, list):
            self._job_codes = list()
            for i in value:
                self._job_codes.append(i)
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.job_codes:
            if isinstance(self.job_codes, list):
                for i in range(0, len(self.job_codes)):
                    element = self.job_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.job_codes[i] = element.to_alipay_dict()
            if hasattr(self.job_codes, 'to_alipay_dict'):
                params['job_codes'] = self.job_codes.to_alipay_dict()
            else:
                params['job_codes'] = self.job_codes
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportConfig()
        if 'job_codes' in d:
            o.job_codes = d['job_codes']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'report_type' in d:
            o.report_type = d['report_type']
        return o



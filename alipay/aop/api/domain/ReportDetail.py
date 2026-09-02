#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportDetail(object):

    def __init__(self):
        self._report_detail_url = None
        self._report_ori_url = None

    @property
    def report_detail_url(self):
        return self._report_detail_url

    @report_detail_url.setter
    def report_detail_url(self, value):
        self._report_detail_url = value
    @property
    def report_ori_url(self):
        return self._report_ori_url

    @report_ori_url.setter
    def report_ori_url(self, value):
        self._report_ori_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.report_detail_url:
            if hasattr(self.report_detail_url, 'to_alipay_dict'):
                params['report_detail_url'] = self.report_detail_url.to_alipay_dict()
            else:
                params['report_detail_url'] = self.report_detail_url
        if self.report_ori_url:
            if hasattr(self.report_ori_url, 'to_alipay_dict'):
                params['report_ori_url'] = self.report_ori_url.to_alipay_dict()
            else:
                params['report_ori_url'] = self.report_ori_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportDetail()
        if 'report_detail_url' in d:
            o.report_detail_url = d['report_detail_url']
        if 'report_ori_url' in d:
            o.report_ori_url = d['report_ori_url']
        return o



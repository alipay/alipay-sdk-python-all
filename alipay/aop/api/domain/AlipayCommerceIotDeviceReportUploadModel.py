#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDeviceReportUploadModel(object):

    def __init__(self):
        self._report_content = None
        self._sn = None

    @property
    def report_content(self):
        return self._report_content

    @report_content.setter
    def report_content(self, value):
        self._report_content = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.report_content:
            if hasattr(self.report_content, 'to_alipay_dict'):
                params['report_content'] = self.report_content.to_alipay_dict()
            else:
                params['report_content'] = self.report_content
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceReportUploadModel()
        if 'report_content' in d:
            o.report_content = d['report_content']
        if 'sn' in d:
            o.sn = d['sn']
        return o



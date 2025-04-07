#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedagentReportIdentifyModel(object):

    def __init__(self):
        self._report_pic_url = None

    @property
    def report_pic_url(self):
        return self._report_pic_url

    @report_pic_url.setter
    def report_pic_url(self, value):
        self._report_pic_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.report_pic_url:
            if hasattr(self.report_pic_url, 'to_alipay_dict'):
                params['report_pic_url'] = self.report_pic_url.to_alipay_dict()
            else:
                params['report_pic_url'] = self.report_pic_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedagentReportIdentifyModel()
        if 'report_pic_url' in d:
            o.report_pic_url = d['report_pic_url']
        return o



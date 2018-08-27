#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomReportCondition import CustomReportCondition


class KoubeiMarketingDataCustomreportSaveModel(object):

    def __init__(self):
        self._report_condition_info = None

    @property
    def report_condition_info(self):
        return self._report_condition_info

    @report_condition_info.setter
    def report_condition_info(self, value):
        if isinstance(value, CustomReportCondition):
            self._report_condition_info = value
        else:
            self._report_condition_info = CustomReportCondition.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.report_condition_info:
            if hasattr(self.report_condition_info, 'to_alipay_dict'):
                params['report_condition_info'] = self.report_condition_info.to_alipay_dict()
            else:
                params['report_condition_info'] = self.report_condition_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataCustomreportSaveModel()
        if 'report_condition_info' in d:
            o.report_condition_info = d['report_condition_info']
        return o



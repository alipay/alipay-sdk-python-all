#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReportInfoDTO import ReportInfoDTO
from alipay.aop.api.domain.ReportInfoDTO import ReportInfoDTO


class AlipayCommerceMedicalReportSametypeGetModel(object):

    def __init__(self):
        self._main_report = None
        self._other_reports = None

    @property
    def main_report(self):
        return self._main_report

    @main_report.setter
    def main_report(self, value):
        if isinstance(value, ReportInfoDTO):
            self._main_report = value
        else:
            self._main_report = ReportInfoDTO.from_alipay_dict(value)
    @property
    def other_reports(self):
        return self._other_reports

    @other_reports.setter
    def other_reports(self, value):
        if isinstance(value, list):
            self._other_reports = list()
            for i in value:
                if isinstance(i, ReportInfoDTO):
                    self._other_reports.append(i)
                else:
                    self._other_reports.append(ReportInfoDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.main_report:
            if hasattr(self.main_report, 'to_alipay_dict'):
                params['main_report'] = self.main_report.to_alipay_dict()
            else:
                params['main_report'] = self.main_report
        if self.other_reports:
            if isinstance(self.other_reports, list):
                for i in range(0, len(self.other_reports)):
                    element = self.other_reports[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_reports[i] = element.to_alipay_dict()
            if hasattr(self.other_reports, 'to_alipay_dict'):
                params['other_reports'] = self.other_reports.to_alipay_dict()
            else:
                params['other_reports'] = self.other_reports
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalReportSametypeGetModel()
        if 'main_report' in d:
            o.main_report = d['main_report']
        if 'other_reports' in d:
            o.other_reports = d['other_reports']
        return o



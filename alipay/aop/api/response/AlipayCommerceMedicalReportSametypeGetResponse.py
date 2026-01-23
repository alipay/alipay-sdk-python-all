#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReportInfoDTO import ReportInfoDTO
from alipay.aop.api.domain.SameTypeReportInfoDTO import SameTypeReportInfoDTO


class AlipayCommerceMedicalReportSametypeGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalReportSametypeGetResponse, self).__init__()
        self._main_report = None
        self._same_type_report = None

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
    def same_type_report(self):
        return self._same_type_report

    @same_type_report.setter
    def same_type_report(self, value):
        if isinstance(value, list):
            self._same_type_report = list()
            for i in value:
                if isinstance(i, SameTypeReportInfoDTO):
                    self._same_type_report.append(i)
                else:
                    self._same_type_report.append(SameTypeReportInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalReportSametypeGetResponse, self).parse_response_content(response_content)
        if 'main_report' in response:
            self.main_report = response['main_report']
        if 'same_type_report' in response:
            self.same_type_report = response['same_type_report']

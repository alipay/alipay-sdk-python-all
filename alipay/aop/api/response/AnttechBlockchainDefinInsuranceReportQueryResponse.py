#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReportInfo import ReportInfo


class AnttechBlockchainDefinInsuranceReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinInsuranceReportQueryResponse, self).__init__()
        self._parm = None
        self._report_info_list = None
        self._trade_no = None

    @property
    def parm(self):
        return self._parm

    @parm.setter
    def parm(self, value):
        self._parm = value
    @property
    def report_info_list(self):
        return self._report_info_list

    @report_info_list.setter
    def report_info_list(self, value):
        if isinstance(value, list):
            self._report_info_list = list()
            for i in value:
                if isinstance(i, ReportInfo):
                    self._report_info_list.append(i)
                else:
                    self._report_info_list.append(ReportInfo.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinInsuranceReportQueryResponse, self).parse_response_content(response_content)
        if 'parm' in response:
            self.parm = response['parm']
        if 'report_info_list' in response:
            self.report_info_list = response['report_info_list']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']

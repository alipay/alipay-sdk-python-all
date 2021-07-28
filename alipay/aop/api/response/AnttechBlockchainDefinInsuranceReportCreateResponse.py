#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinInsuranceReportCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinInsuranceReportCreateResponse, self).__init__()
        self._parm = None
        self._report_no = None
        self._trade_no = None

    @property
    def parm(self):
        return self._parm

    @parm.setter
    def parm(self, value):
        self._parm = value
    @property
    def report_no(self):
        return self._report_no

    @report_no.setter
    def report_no(self, value):
        self._report_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinInsuranceReportCreateResponse, self).parse_response_content(response_content)
        if 'parm' in response:
            self.parm = response['parm']
        if 'report_no' in response:
            self.report_no = response['report_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']

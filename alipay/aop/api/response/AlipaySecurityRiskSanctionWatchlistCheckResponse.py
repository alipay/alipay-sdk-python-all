#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PBCScanResult import PBCScanResult


class AlipaySecurityRiskSanctionWatchlistCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskSanctionWatchlistCheckResponse, self).__init__()
        self._open_trace_id = None
        self._pbc_scan_result = None

    @property
    def open_trace_id(self):
        return self._open_trace_id

    @open_trace_id.setter
    def open_trace_id(self, value):
        self._open_trace_id = value
    @property
    def pbc_scan_result(self):
        return self._pbc_scan_result

    @pbc_scan_result.setter
    def pbc_scan_result(self, value):
        if isinstance(value, PBCScanResult):
            self._pbc_scan_result = value
        else:
            self._pbc_scan_result = PBCScanResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskSanctionWatchlistCheckResponse, self).parse_response_content(response_content)
        if 'open_trace_id' in response:
            self.open_trace_id = response['open_trace_id']
        if 'pbc_scan_result' in response:
            self.pbc_scan_result = response['pbc_scan_result']

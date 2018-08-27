#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiagnoseResult import DiagnoseResult


class KoubeiMarketingDataSmartmanagementDiagnoseResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataSmartmanagementDiagnoseResponse, self).__init__()
        self._diagnose_result = None

    @property
    def diagnose_result(self):
        return self._diagnose_result

    @diagnose_result.setter
    def diagnose_result(self, value):
        if isinstance(value, list):
            self._diagnose_result = list()
            for i in value:
                if isinstance(i, DiagnoseResult):
                    self._diagnose_result.append(i)
                else:
                    self._diagnose_result.append(DiagnoseResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataSmartmanagementDiagnoseResponse, self).parse_response_content(response_content)
        if 'diagnose_result' in response:
            self.diagnose_result = response['diagnose_result']

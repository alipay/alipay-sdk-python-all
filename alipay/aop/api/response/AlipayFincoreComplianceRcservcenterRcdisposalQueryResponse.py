#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PunishStatusResult import PunishStatusResult


class AlipayFincoreComplianceRcservcenterRcdisposalQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceRcservcenterRcdisposalQueryResponse, self).__init__()
        self._punish_status_result = None

    @property
    def punish_status_result(self):
        return self._punish_status_result

    @punish_status_result.setter
    def punish_status_result(self, value):
        if isinstance(value, PunishStatusResult):
            self._punish_status_result = value
        else:
            self._punish_status_result = PunishStatusResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceRcservcenterRcdisposalQueryResponse, self).parse_response_content(response_content)
        if 'punish_status_result' in response:
            self.punish_status_result = response['punish_status_result']

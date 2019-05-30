#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiagnosisInfo import DiagnosisInfo


class AlipayBossOrderDiagnosisGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossOrderDiagnosisGetResponse, self).__init__()
        self._diagnosis_result = None

    @property
    def diagnosis_result(self):
        return self._diagnosis_result

    @diagnosis_result.setter
    def diagnosis_result(self, value):
        if isinstance(value, list):
            self._diagnosis_result = list()
            for i in value:
                if isinstance(i, DiagnosisInfo):
                    self._diagnosis_result.append(i)
                else:
                    self._diagnosis_result.append(DiagnosisInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBossOrderDiagnosisGetResponse, self).parse_response_content(response_content)
        if 'diagnosis_result' in response:
            self.diagnosis_result = response['diagnosis_result']

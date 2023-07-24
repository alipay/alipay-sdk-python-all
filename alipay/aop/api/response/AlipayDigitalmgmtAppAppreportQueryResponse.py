#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ApmobileAppDetectResultDTO import ApmobileAppDetectResultDTO


class AlipayDigitalmgmtAppAppreportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtAppAppreportQueryResponse, self).__init__()
        self._apmobile_app_detect_result_dto = None

    @property
    def apmobile_app_detect_result_dto(self):
        return self._apmobile_app_detect_result_dto

    @apmobile_app_detect_result_dto.setter
    def apmobile_app_detect_result_dto(self, value):
        if isinstance(value, ApmobileAppDetectResultDTO):
            self._apmobile_app_detect_result_dto = value
        else:
            self._apmobile_app_detect_result_dto = ApmobileAppDetectResultDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtAppAppreportQueryResponse, self).parse_response_content(response_content)
        if 'apmobile_app_detect_result_dto' in response:
            self.apmobile_app_detect_result_dto = response['apmobile_app_detect_result_dto']

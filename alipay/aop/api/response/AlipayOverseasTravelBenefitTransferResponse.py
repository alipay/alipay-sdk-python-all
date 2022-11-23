#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayOverseasTravelBenefitTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelBenefitTransferResponse, self).__init__()
        self._benefit_detail_url = None
        self._result = None
        self._sync_fail_code = None
        self._sync_fail_reason = None
        self._sync_status = None

    @property
    def benefit_detail_url(self):
        return self._benefit_detail_url

    @benefit_detail_url.setter
    def benefit_detail_url(self, value):
        self._benefit_detail_url = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ResultInfoDTO):
            self._result = value
        else:
            self._result = ResultInfoDTO.from_alipay_dict(value)
    @property
    def sync_fail_code(self):
        return self._sync_fail_code

    @sync_fail_code.setter
    def sync_fail_code(self, value):
        self._sync_fail_code = value
    @property
    def sync_fail_reason(self):
        return self._sync_fail_reason

    @sync_fail_reason.setter
    def sync_fail_reason(self, value):
        self._sync_fail_reason = value
    @property
    def sync_status(self):
        return self._sync_status

    @sync_status.setter
    def sync_status(self, value):
        self._sync_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelBenefitTransferResponse, self).parse_response_content(response_content)
        if 'benefit_detail_url' in response:
            self.benefit_detail_url = response['benefit_detail_url']
        if 'result' in response:
            self.result = response['result']
        if 'sync_fail_code' in response:
            self.sync_fail_code = response['sync_fail_code']
        if 'sync_fail_reason' in response:
            self.sync_fail_reason = response['sync_fail_reason']
        if 'sync_status' in response:
            self.sync_status = response['sync_status']

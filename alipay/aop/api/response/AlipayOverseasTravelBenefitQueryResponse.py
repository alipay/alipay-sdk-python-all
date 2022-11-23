#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayOverseasTravelBenefitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelBenefitQueryResponse, self).__init__()
        self._client_benefit_id = None
        self._ext_info = None
        self._result = None
        self._sync_fail_code = None
        self._sync_fail_reason = None
        self._sync_status = None

    @property
    def client_benefit_id(self):
        return self._client_benefit_id

    @client_benefit_id.setter
    def client_benefit_id(self, value):
        self._client_benefit_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
        response = super(AlipayOverseasTravelBenefitQueryResponse, self).parse_response_content(response_content)
        if 'client_benefit_id' in response:
            self.client_benefit_id = response['client_benefit_id']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'result' in response:
            self.result = response['result']
        if 'sync_fail_code' in response:
            self.sync_fail_code = response['sync_fail_code']
        if 'sync_fail_reason' in response:
            self.sync_fail_reason = response['sync_fail_reason']
        if 'sync_status' in response:
            self.sync_status = response['sync_status']

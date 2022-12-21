#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SpeechRecordReportFailDetail import SpeechRecordReportFailDetail


class AlipayMerchantIndirectIotdataBatchcreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectIotdataBatchcreateResponse, self).__init__()
        self._fail_detail = None
        self._success_count = None

    @property
    def fail_detail(self):
        return self._fail_detail

    @fail_detail.setter
    def fail_detail(self, value):
        if isinstance(value, list):
            self._fail_detail = list()
            for i in value:
                if isinstance(i, SpeechRecordReportFailDetail):
                    self._fail_detail.append(i)
                else:
                    self._fail_detail.append(SpeechRecordReportFailDetail.from_alipay_dict(i))
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectIotdataBatchcreateResponse, self).parse_response_content(response_content)
        if 'fail_detail' in response:
            self.fail_detail = response['fail_detail']
        if 'success_count' in response:
            self.success_count = response['success_count']

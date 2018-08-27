#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerContractRecordSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerContractRecordSyncResponse, self).__init__()
        self._record_no = None

    @property
    def record_no(self):
        return self._record_no

    @record_no.setter
    def record_no(self, value):
        self._record_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerContractRecordSyncResponse, self).parse_response_content(response_content)
        if 'record_no' in response:
            self.record_no = response['record_no']

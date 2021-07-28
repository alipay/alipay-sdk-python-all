#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConsumeRecord import ConsumeRecord


class AlipayUserBillDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserBillDetailQueryResponse, self).__init__()
        self._consume_record = None

    @property
    def consume_record(self):
        return self._consume_record

    @consume_record.setter
    def consume_record(self, value):
        if isinstance(value, ConsumeRecord):
            self._consume_record = value
        else:
            self._consume_record = ConsumeRecord.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserBillDetailQueryResponse, self).parse_response_content(response_content)
        if 'consume_record' in response:
            self.consume_record = response['consume_record']

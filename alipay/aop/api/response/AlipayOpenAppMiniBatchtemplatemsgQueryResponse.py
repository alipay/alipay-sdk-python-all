#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BatchTemplateMsgRecordVO import BatchTemplateMsgRecordVO


class AlipayOpenAppMiniBatchtemplatemsgQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppMiniBatchtemplatemsgQueryResponse, self).__init__()
        self._record = None

    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, value):
        if isinstance(value, BatchTemplateMsgRecordVO):
            self._record = value
        else:
            self._record = BatchTemplateMsgRecordVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppMiniBatchtemplatemsgQueryResponse, self).parse_response_content(response_content)
        if 'record' in response:
            self.record = response['record']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenCrowdOperationTag import OpenCrowdOperationTag


class AlipayMarketingQipanTagQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingQipanTagQueryResponse, self).__init__()
        self._operation_tag = None

    @property
    def operation_tag(self):
        return self._operation_tag

    @operation_tag.setter
    def operation_tag(self, value):
        if isinstance(value, OpenCrowdOperationTag):
            self._operation_tag = value
        else:
            self._operation_tag = OpenCrowdOperationTag.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingQipanTagQueryResponse, self).parse_response_content(response_content)
        if 'operation_tag' in response:
            self.operation_tag = response['operation_tag']

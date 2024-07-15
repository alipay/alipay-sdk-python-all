#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenCrowdOperationTag import OpenCrowdOperationTag


class AlipayMarketingQipanTagbaseBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingQipanTagbaseBatchqueryResponse, self).__init__()
        self._operation_tag_list = None

    @property
    def operation_tag_list(self):
        return self._operation_tag_list

    @operation_tag_list.setter
    def operation_tag_list(self, value):
        if isinstance(value, list):
            self._operation_tag_list = list()
            for i in value:
                if isinstance(i, OpenCrowdOperationTag):
                    self._operation_tag_list.append(i)
                else:
                    self._operation_tag_list.append(OpenCrowdOperationTag.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingQipanTagbaseBatchqueryResponse, self).parse_response_content(response_content)
        if 'operation_tag_list' in response:
            self.operation_tag_list = response['operation_tag_list']

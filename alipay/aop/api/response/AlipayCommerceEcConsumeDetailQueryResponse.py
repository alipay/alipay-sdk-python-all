#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcConsumeInfo import EcConsumeInfo
from alipay.aop.api.domain.EcConsumeInfo import EcConsumeInfo


class AlipayCommerceEcConsumeDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcConsumeDetailQueryResponse, self).__init__()
        self._consume_info = None
        self._related_refund_list = None

    @property
    def consume_info(self):
        return self._consume_info

    @consume_info.setter
    def consume_info(self, value):
        if isinstance(value, EcConsumeInfo):
            self._consume_info = value
        else:
            self._consume_info = EcConsumeInfo.from_alipay_dict(value)
    @property
    def related_refund_list(self):
        return self._related_refund_list

    @related_refund_list.setter
    def related_refund_list(self, value):
        if isinstance(value, list):
            self._related_refund_list = list()
            for i in value:
                if isinstance(i, EcConsumeInfo):
                    self._related_refund_list.append(i)
                else:
                    self._related_refund_list.append(EcConsumeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcConsumeDetailQueryResponse, self).parse_response_content(response_content)
        if 'consume_info' in response:
            self.consume_info = response['consume_info']
        if 'related_refund_list' in response:
            self.related_refund_list = response['related_refund_list']

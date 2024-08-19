#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceAssistantDetailVO import ServiceAssistantDetailVO


class AlipayMerchantGroupAssistantServiceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupAssistantServiceQueryResponse, self).__init__()
        self._assistant_detail = None

    @property
    def assistant_detail(self):
        return self._assistant_detail

    @assistant_detail.setter
    def assistant_detail(self, value):
        if isinstance(value, ServiceAssistantDetailVO):
            self._assistant_detail = value
        else:
            self._assistant_detail = ServiceAssistantDetailVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupAssistantServiceQueryResponse, self).parse_response_content(response_content)
        if 'assistant_detail' in response:
            self.assistant_detail = response['assistant_detail']

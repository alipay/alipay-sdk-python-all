#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssistantMsgDetailVO import AssistantMsgDetailVO


class AlipayMerchantGroupAssistantMsgQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupAssistantMsgQueryResponse, self).__init__()
        self._msg_detail = None

    @property
    def msg_detail(self):
        return self._msg_detail

    @msg_detail.setter
    def msg_detail(self, value):
        if isinstance(value, AssistantMsgDetailVO):
            self._msg_detail = value
        else:
            self._msg_detail = AssistantMsgDetailVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupAssistantMsgQueryResponse, self).parse_response_content(response_content)
        if 'msg_detail' in response:
            self.msg_detail = response['msg_detail']

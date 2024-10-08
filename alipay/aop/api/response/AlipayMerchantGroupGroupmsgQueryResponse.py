#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupMsgSendDetailVO import GroupMsgSendDetailVO


class AlipayMerchantGroupGroupmsgQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupGroupmsgQueryResponse, self).__init__()
        self._msg_send_detail = None

    @property
    def msg_send_detail(self):
        return self._msg_send_detail

    @msg_send_detail.setter
    def msg_send_detail(self, value):
        if isinstance(value, GroupMsgSendDetailVO):
            self._msg_send_detail = value
        else:
            self._msg_send_detail = GroupMsgSendDetailVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupGroupmsgQueryResponse, self).parse_response_content(response_content)
        if 'msg_send_detail' in response:
            self.msg_send_detail = response['msg_send_detail']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicLifeMsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLifeMsgSendResponse, self).__init__()
        self._alipay_msg_id = None

    @property
    def alipay_msg_id(self):
        return self._alipay_msg_id

    @alipay_msg_id.setter
    def alipay_msg_id(self, value):
        self._alipay_msg_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLifeMsgSendResponse, self).parse_response_content(response_content)
        if 'alipay_msg_id' in response:
            self.alipay_msg_id = response['alipay_msg_id']

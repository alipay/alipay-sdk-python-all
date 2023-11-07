#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MessageReceiveVO import MessageReceiveVO


class AlipayCommerceEducateYouthEdumessageauthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateYouthEdumessageauthQueryResponse, self).__init__()
        self._inst_auth_state = None
        self._message_receive_state_list = None

    @property
    def inst_auth_state(self):
        return self._inst_auth_state

    @inst_auth_state.setter
    def inst_auth_state(self, value):
        self._inst_auth_state = value
    @property
    def message_receive_state_list(self):
        return self._message_receive_state_list

    @message_receive_state_list.setter
    def message_receive_state_list(self, value):
        if isinstance(value, MessageReceiveVO):
            self._message_receive_state_list = value
        else:
            self._message_receive_state_list = MessageReceiveVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateYouthEdumessageauthQueryResponse, self).parse_response_content(response_content)
        if 'inst_auth_state' in response:
            self.inst_auth_state = response['inst_auth_state']
        if 'message_receive_state_list' in response:
            self.message_receive_state_list = response['message_receive_state_list']

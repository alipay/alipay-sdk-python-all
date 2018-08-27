#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbAdvertChannelResponse import KbAdvertChannelResponse


class KoubeiAdvertCommissionChannelModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertCommissionChannelModifyResponse, self).__init__()
        self._channel_response = None

    @property
    def channel_response(self):
        return self._channel_response

    @channel_response.setter
    def channel_response(self, value):
        if isinstance(value, list):
            self._channel_response = list()
            for i in value:
                if isinstance(i, KbAdvertChannelResponse):
                    self._channel_response.append(i)
                else:
                    self._channel_response.append(KbAdvertChannelResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertCommissionChannelModifyResponse, self).parse_response_content(response_content)
        if 'channel_response' in response:
            self.channel_response = response['channel_response']

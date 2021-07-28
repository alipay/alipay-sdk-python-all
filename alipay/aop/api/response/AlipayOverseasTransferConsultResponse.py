#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTransferConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTransferConsultResponse, self).__init__()
        self._channel_list = None
        self._default_channel = None

    @property
    def channel_list(self):
        return self._channel_list

    @channel_list.setter
    def channel_list(self, value):
        if isinstance(value, list):
            self._channel_list = list()
            for i in value:
                self._channel_list.append(i)
    @property
    def default_channel(self):
        return self._default_channel

    @default_channel.setter
    def default_channel(self, value):
        self._default_channel = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTransferConsultResponse, self).parse_response_content(response_content)
        if 'channel_list' in response:
            self.channel_list = response['channel_list']
        if 'default_channel' in response:
            self.default_channel = response['default_channel']

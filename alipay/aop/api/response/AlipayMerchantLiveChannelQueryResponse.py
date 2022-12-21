#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantLiveChannelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantLiveChannelQueryResponse, self).__init__()
        self._channel_content = None
        self._channel_identity = None
        self._channel_secret = None
        self._channel_type = None

    @property
    def channel_content(self):
        return self._channel_content

    @channel_content.setter
    def channel_content(self, value):
        self._channel_content = value
    @property
    def channel_identity(self):
        return self._channel_identity

    @channel_identity.setter
    def channel_identity(self, value):
        self._channel_identity = value
    @property
    def channel_secret(self):
        return self._channel_secret

    @channel_secret.setter
    def channel_secret(self, value):
        self._channel_secret = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantLiveChannelQueryResponse, self).parse_response_content(response_content)
        if 'channel_content' in response:
            self.channel_content = response['channel_content']
        if 'channel_identity' in response:
            self.channel_identity = response['channel_identity']
        if 'channel_secret' in response:
            self.channel_secret = response['channel_secret']
        if 'channel_type' in response:
            self.channel_type = response['channel_type']

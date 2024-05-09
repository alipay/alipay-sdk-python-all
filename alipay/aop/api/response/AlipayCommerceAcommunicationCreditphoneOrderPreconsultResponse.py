#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConsultChannelResponse import ConsultChannelResponse


class AlipayCommerceAcommunicationCreditphoneOrderPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCreditphoneOrderPreconsultResponse, self).__init__()
        self._channel_list = None
        self._pass = None

    @property
    def channel_list(self):
        return self._channel_list

    @channel_list.setter
    def channel_list(self, value):
        if isinstance(value, list):
            self._channel_list = list()
            for i in value:
                if isinstance(i, ConsultChannelResponse):
                    self._channel_list.append(i)
                else:
                    self._channel_list.append(ConsultChannelResponse.from_alipay_dict(i))
    @property
    def pass(self):
        return self._pass

    @pass.setter
    def pass(self, value):
        self._pass = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCreditphoneOrderPreconsultResponse, self).parse_response_content(response_content)
        if 'channel_list' in response:
            self.channel_list = response['channel_list']
        if 'pass' in response:
            self.pass = response['pass']

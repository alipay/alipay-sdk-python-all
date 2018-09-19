#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperatorChannelInfo import OperatorChannelInfo


class SsdataFindataOperatorChannelQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataFindataOperatorChannelQueryResponse, self).__init__()
        self._channels = None

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, value):
        if isinstance(value, list):
            self._channels = list()
            for i in value:
                if isinstance(i, OperatorChannelInfo):
                    self._channels.append(i)
                else:
                    self._channels.append(OperatorChannelInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(SsdataFindataOperatorChannelQueryResponse, self).parse_response_content(response_content)
        if 'channels' in response:
            self.channels = response['channels']

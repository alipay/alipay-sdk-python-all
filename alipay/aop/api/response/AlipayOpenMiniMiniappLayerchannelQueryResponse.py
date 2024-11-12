#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChannelCodeInfo import ChannelCodeInfo


class AlipayOpenMiniMiniappLayerchannelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMiniappLayerchannelQueryResponse, self).__init__()
        self._channel_code_list = None

    @property
    def channel_code_list(self):
        return self._channel_code_list

    @channel_code_list.setter
    def channel_code_list(self, value):
        if isinstance(value, list):
            self._channel_code_list = list()
            for i in value:
                if isinstance(i, ChannelCodeInfo):
                    self._channel_code_list.append(i)
                else:
                    self._channel_code_list.append(ChannelCodeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMiniappLayerchannelQueryResponse, self).parse_response_content(response_content)
        if 'channel_code_list' in response:
            self.channel_code_list = response['channel_code_list']

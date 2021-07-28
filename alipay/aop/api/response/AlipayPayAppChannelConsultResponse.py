#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChannelInfo import ChannelInfo


class AlipayPayAppChannelConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppChannelConsultResponse, self).__init__()
        self._channel_info_list = None

    @property
    def channel_info_list(self):
        return self._channel_info_list

    @channel_info_list.setter
    def channel_info_list(self, value):
        if isinstance(value, list):
            self._channel_info_list = list()
            for i in value:
                if isinstance(i, ChannelInfo):
                    self._channel_info_list.append(i)
                else:
                    self._channel_info_list.append(ChannelInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppChannelConsultResponse, self).parse_response_content(response_content)
        if 'channel_info_list' in response:
            self.channel_info_list = response['channel_info_list']

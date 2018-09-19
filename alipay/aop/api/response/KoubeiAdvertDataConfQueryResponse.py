#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbadvertChannelTypeResponse import KbadvertChannelTypeResponse
from alipay.aop.api.domain.KbadvertCommissionLimit import KbadvertCommissionLimit


class KoubeiAdvertDataConfQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertDataConfQueryResponse, self).__init__()
        self._channel_types = None
        self._commission_limits = None

    @property
    def channel_types(self):
        return self._channel_types

    @channel_types.setter
    def channel_types(self, value):
        if isinstance(value, list):
            self._channel_types = list()
            for i in value:
                if isinstance(i, KbadvertChannelTypeResponse):
                    self._channel_types.append(i)
                else:
                    self._channel_types.append(KbadvertChannelTypeResponse.from_alipay_dict(i))
    @property
    def commission_limits(self):
        return self._commission_limits

    @commission_limits.setter
    def commission_limits(self, value):
        if isinstance(value, list):
            self._commission_limits = list()
            for i in value:
                if isinstance(i, KbadvertCommissionLimit):
                    self._commission_limits.append(i)
                else:
                    self._commission_limits.append(KbadvertCommissionLimit.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertDataConfQueryResponse, self).parse_response_content(response_content)
        if 'channel_types' in response:
            self.channel_types = response['channel_types']
        if 'commission_limits' in response:
            self.commission_limits = response['commission_limits']

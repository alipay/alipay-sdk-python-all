#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayMiniCardData import AlipayMiniCardData
from alipay.aop.api.domain.AlipayMiniCardData import AlipayMiniCardData


class AlipayUserMemberAlipaycardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMemberAlipaycardQueryResponse, self).__init__()
        self._alipay_card_cache_data = None
        self._alipay_card_real_time_data = None

    @property
    def alipay_card_cache_data(self):
        return self._alipay_card_cache_data

    @alipay_card_cache_data.setter
    def alipay_card_cache_data(self, value):
        if isinstance(value, AlipayMiniCardData):
            self._alipay_card_cache_data = value
        else:
            self._alipay_card_cache_data = AlipayMiniCardData.from_alipay_dict(value)
    @property
    def alipay_card_real_time_data(self):
        return self._alipay_card_real_time_data

    @alipay_card_real_time_data.setter
    def alipay_card_real_time_data(self, value):
        if isinstance(value, AlipayMiniCardData):
            self._alipay_card_real_time_data = value
        else:
            self._alipay_card_real_time_data = AlipayMiniCardData.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserMemberAlipaycardQueryResponse, self).parse_response_content(response_content)
        if 'alipay_card_cache_data' in response:
            self.alipay_card_cache_data = response['alipay_card_cache_data']
        if 'alipay_card_real_time_data' in response:
            self.alipay_card_real_time_data = response['alipay_card_real_time_data']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PortraitDataVO import PortraitDataVO


class AlipayMerchantQipanInsightQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanInsightQueryResponse, self).__init__()
        self._portrait_data_list = None

    @property
    def portrait_data_list(self):
        return self._portrait_data_list

    @portrait_data_list.setter
    def portrait_data_list(self, value):
        if isinstance(value, list):
            self._portrait_data_list = list()
            for i in value:
                if isinstance(i, PortraitDataVO):
                    self._portrait_data_list.append(i)
                else:
                    self._portrait_data_list.append(PortraitDataVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanInsightQueryResponse, self).parse_response_content(response_content)
        if 'portrait_data_list' in response:
            self.portrait_data_list = response['portrait_data_list']

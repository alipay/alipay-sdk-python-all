#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FlowItemInfo import FlowItemInfo


class AlipayCommerceAcommunicationDistributionFlowitemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDistributionFlowitemQueryResponse, self).__init__()
        self._item_info = None

    @property
    def item_info(self):
        return self._item_info

    @item_info.setter
    def item_info(self, value):
        if isinstance(value, FlowItemInfo):
            self._item_info = value
        else:
            self._item_info = FlowItemInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDistributionFlowitemQueryResponse, self).parse_response_content(response_content)
        if 'item_info' in response:
            self.item_info = response['item_info']

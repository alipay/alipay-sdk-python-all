#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FlowItemInfo import FlowItemInfo


class AlipayCommerceAcommunicationDistributionFlowitemBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDistributionFlowitemBatchqueryResponse, self).__init__()
        self._count = None
        self._item_list = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, FlowItemInfo):
                    self._item_list.append(i)
                else:
                    self._item_list.append(FlowItemInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDistributionFlowitemBatchqueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'item_list' in response:
            self.item_list = response['item_list']

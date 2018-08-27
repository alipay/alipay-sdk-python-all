#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InboundOrderVO import InboundOrderVO


class KoubeiRetailWmsInboundorderBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsInboundorderBatchqueryResponse, self).__init__()
        self._inbound_order_vo_list = None

    @property
    def inbound_order_vo_list(self):
        return self._inbound_order_vo_list

    @inbound_order_vo_list.setter
    def inbound_order_vo_list(self, value):
        if isinstance(value, list):
            self._inbound_order_vo_list = list()
            for i in value:
                if isinstance(i, InboundOrderVO):
                    self._inbound_order_vo_list.append(i)
                else:
                    self._inbound_order_vo_list.append(InboundOrderVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsInboundorderBatchqueryResponse, self).parse_response_content(response_content)
        if 'inbound_order_vo_list' in response:
            self.inbound_order_vo_list = response['inbound_order_vo_list']

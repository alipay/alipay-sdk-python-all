#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InboundOrderLine import InboundOrderLine
from alipay.aop.api.domain.InboundOrderVO import InboundOrderVO


class KoubeiRetailWmsInboundorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsInboundorderQueryResponse, self).__init__()
        self._inbound_order_line_list = None
        self._inbound_order_vo = None

    @property
    def inbound_order_line_list(self):
        return self._inbound_order_line_list

    @inbound_order_line_list.setter
    def inbound_order_line_list(self, value):
        if isinstance(value, list):
            self._inbound_order_line_list = list()
            for i in value:
                if isinstance(i, InboundOrderLine):
                    self._inbound_order_line_list.append(i)
                else:
                    self._inbound_order_line_list.append(InboundOrderLine.from_alipay_dict(i))
    @property
    def inbound_order_vo(self):
        return self._inbound_order_vo

    @inbound_order_vo.setter
    def inbound_order_vo(self, value):
        if isinstance(value, InboundOrderVO):
            self._inbound_order_vo = value
        else:
            self._inbound_order_vo = InboundOrderVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsInboundorderQueryResponse, self).parse_response_content(response_content)
        if 'inbound_order_line_list' in response:
            self.inbound_order_line_list = response['inbound_order_line_list']
        if 'inbound_order_vo' in response:
            self.inbound_order_vo = response['inbound_order_vo']

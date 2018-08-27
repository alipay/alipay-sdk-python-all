#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OutboundOrderLine import OutboundOrderLine
from alipay.aop.api.domain.OutboundOrderVO import OutboundOrderVO


class KoubeiRetailWmsOutboundorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsOutboundorderQueryResponse, self).__init__()
        self._outbound_order_line_list = None
        self._outbound_order_vo = None

    @property
    def outbound_order_line_list(self):
        return self._outbound_order_line_list

    @outbound_order_line_list.setter
    def outbound_order_line_list(self, value):
        if isinstance(value, list):
            self._outbound_order_line_list = list()
            for i in value:
                if isinstance(i, OutboundOrderLine):
                    self._outbound_order_line_list.append(i)
                else:
                    self._outbound_order_line_list.append(OutboundOrderLine.from_alipay_dict(i))
    @property
    def outbound_order_vo(self):
        return self._outbound_order_vo

    @outbound_order_vo.setter
    def outbound_order_vo(self, value):
        if isinstance(value, OutboundOrderVO):
            self._outbound_order_vo = value
        else:
            self._outbound_order_vo = OutboundOrderVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsOutboundorderQueryResponse, self).parse_response_content(response_content)
        if 'outbound_order_line_list' in response:
            self.outbound_order_line_list = response['outbound_order_line_list']
        if 'outbound_order_vo' in response:
            self.outbound_order_vo = response['outbound_order_vo']

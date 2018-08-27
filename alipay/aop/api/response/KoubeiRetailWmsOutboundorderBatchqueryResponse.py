#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OutboundOrderVO import OutboundOrderVO


class KoubeiRetailWmsOutboundorderBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsOutboundorderBatchqueryResponse, self).__init__()
        self._outbound_order_vo_list = None

    @property
    def outbound_order_vo_list(self):
        return self._outbound_order_vo_list

    @outbound_order_vo_list.setter
    def outbound_order_vo_list(self, value):
        if isinstance(value, list):
            self._outbound_order_vo_list = list()
            for i in value:
                if isinstance(i, OutboundOrderVO):
                    self._outbound_order_vo_list.append(i)
                else:
                    self._outbound_order_vo_list.append(OutboundOrderVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsOutboundorderBatchqueryResponse, self).parse_response_content(response_content)
        if 'outbound_order_vo_list' in response:
            self.outbound_order_vo_list = response['outbound_order_vo_list']

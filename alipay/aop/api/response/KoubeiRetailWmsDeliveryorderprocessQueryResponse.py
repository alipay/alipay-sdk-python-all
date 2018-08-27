#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryOrderProcessVO import DeliveryOrderProcessVO


class KoubeiRetailWmsDeliveryorderprocessQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsDeliveryorderprocessQueryResponse, self).__init__()
        self._delivery_order_process_vo_list = None

    @property
    def delivery_order_process_vo_list(self):
        return self._delivery_order_process_vo_list

    @delivery_order_process_vo_list.setter
    def delivery_order_process_vo_list(self, value):
        if isinstance(value, list):
            self._delivery_order_process_vo_list = list()
            for i in value:
                if isinstance(i, DeliveryOrderProcessVO):
                    self._delivery_order_process_vo_list.append(i)
                else:
                    self._delivery_order_process_vo_list.append(DeliveryOrderProcessVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsDeliveryorderprocessQueryResponse, self).parse_response_content(response_content)
        if 'delivery_order_process_vo_list' in response:
            self.delivery_order_process_vo_list = response['delivery_order_process_vo_list']

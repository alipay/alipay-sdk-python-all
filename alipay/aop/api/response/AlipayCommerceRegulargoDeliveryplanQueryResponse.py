#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryFulfillmentVO import DeliveryFulfillmentVO
from alipay.aop.api.domain.DeliverySubOrderVO import DeliverySubOrderVO


class AlipayCommerceRegulargoDeliveryplanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRegulargoDeliveryplanQueryResponse, self).__init__()
        self._fulfillment_info = None
        self._sub_order_list = None

    @property
    def fulfillment_info(self):
        return self._fulfillment_info

    @fulfillment_info.setter
    def fulfillment_info(self, value):
        if isinstance(value, DeliveryFulfillmentVO):
            self._fulfillment_info = value
        else:
            self._fulfillment_info = DeliveryFulfillmentVO.from_alipay_dict(value)
    @property
    def sub_order_list(self):
        return self._sub_order_list

    @sub_order_list.setter
    def sub_order_list(self, value):
        if isinstance(value, list):
            self._sub_order_list = list()
            for i in value:
                if isinstance(i, DeliverySubOrderVO):
                    self._sub_order_list.append(i)
                else:
                    self._sub_order_list.append(DeliverySubOrderVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRegulargoDeliveryplanQueryResponse, self).parse_response_content(response_content)
        if 'fulfillment_info' in response:
            self.fulfillment_info = response['fulfillment_info']
        if 'sub_order_list' in response:
            self.sub_order_list = response['sub_order_list']

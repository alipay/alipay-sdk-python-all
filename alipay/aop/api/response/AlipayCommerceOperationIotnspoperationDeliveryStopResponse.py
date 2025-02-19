#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationIotnspoperationDeliveryStopResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationIotnspoperationDeliveryStopResponse, self).__init__()
        self._n_delivery_id = None

    @property
    def n_delivery_id(self):
        return self._n_delivery_id

    @n_delivery_id.setter
    def n_delivery_id(self, value):
        self._n_delivery_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationIotnspoperationDeliveryStopResponse, self).parse_response_content(response_content)
        if 'n_delivery_id' in response:
            self.n_delivery_id = response['n_delivery_id']

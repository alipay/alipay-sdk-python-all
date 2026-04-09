#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryLogistics import DeliveryLogistics


class AlipayOpenSpNcoilopenDeliverylogisticsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNcoilopenDeliverylogisticsQueryResponse, self).__init__()
        self._delivery_infos = None
        self._order_id = None

    @property
    def delivery_infos(self):
        return self._delivery_infos

    @delivery_infos.setter
    def delivery_infos(self, value):
        if isinstance(value, list):
            self._delivery_infos = list()
            for i in value:
                if isinstance(i, DeliveryLogistics):
                    self._delivery_infos.append(i)
                else:
                    self._delivery_infos.append(DeliveryLogistics.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNcoilopenDeliverylogisticsQueryResponse, self).parse_response_content(response_content)
        if 'delivery_infos' in response:
            self.delivery_infos = response['delivery_infos']
        if 'order_id' in response:
            self.order_id = response['order_id']

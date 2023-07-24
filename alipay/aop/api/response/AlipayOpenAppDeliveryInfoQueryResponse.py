#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemDeliveryInfoVO import ItemDeliveryInfoVO


class AlipayOpenAppDeliveryInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppDeliveryInfoQueryResponse, self).__init__()
        self._delivery_infos = None

    @property
    def delivery_infos(self):
        return self._delivery_infos

    @delivery_infos.setter
    def delivery_infos(self, value):
        if isinstance(value, list):
            self._delivery_infos = list()
            for i in value:
                if isinstance(i, ItemDeliveryInfoVO):
                    self._delivery_infos.append(i)
                else:
                    self._delivery_infos.append(ItemDeliveryInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppDeliveryInfoQueryResponse, self).parse_response_content(response_content)
        if 'delivery_infos' in response:
            self.delivery_infos = response['delivery_infos']

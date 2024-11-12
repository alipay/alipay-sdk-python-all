#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupDeliveryDetailVO import GroupDeliveryDetailVO


class AlipayMerchantGroupDeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupDeliveryQueryResponse, self).__init__()
        self._delivery_detail = None

    @property
    def delivery_detail(self):
        return self._delivery_detail

    @delivery_detail.setter
    def delivery_detail(self, value):
        if isinstance(value, GroupDeliveryDetailVO):
            self._delivery_detail = value
        else:
            self._delivery_detail = GroupDeliveryDetailVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupDeliveryQueryResponse, self).parse_response_content(response_content)
        if 'delivery_detail' in response:
            self.delivery_detail = response['delivery_detail']

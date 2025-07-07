#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleStdOrderBaseVO import RecycleStdOrderBaseVO
from alipay.aop.api.domain.RecycleDeliveryVO import RecycleDeliveryVO
from alipay.aop.api.domain.RecycleDeliveryVO import RecycleDeliveryVO


class AlipayCommerceRecycleOrderDelegateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleOrderDelegateQueryResponse, self).__init__()
        self._order_base = None
        self._order_delivery = None
        self._order_sendback = None

    @property
    def order_base(self):
        return self._order_base

    @order_base.setter
    def order_base(self, value):
        if isinstance(value, RecycleStdOrderBaseVO):
            self._order_base = value
        else:
            self._order_base = RecycleStdOrderBaseVO.from_alipay_dict(value)
    @property
    def order_delivery(self):
        return self._order_delivery

    @order_delivery.setter
    def order_delivery(self, value):
        if isinstance(value, RecycleDeliveryVO):
            self._order_delivery = value
        else:
            self._order_delivery = RecycleDeliveryVO.from_alipay_dict(value)
    @property
    def order_sendback(self):
        return self._order_sendback

    @order_sendback.setter
    def order_sendback(self, value):
        if isinstance(value, RecycleDeliveryVO):
            self._order_sendback = value
        else:
            self._order_sendback = RecycleDeliveryVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleOrderDelegateQueryResponse, self).parse_response_content(response_content)
        if 'order_base' in response:
            self.order_base = response['order_base']
        if 'order_delivery' in response:
            self.order_delivery = response['order_delivery']
        if 'order_sendback' in response:
            self.order_sendback = response['order_sendback']

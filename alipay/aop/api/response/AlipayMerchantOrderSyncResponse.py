#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderDataDistributeInfo import OrderDataDistributeInfo


class AlipayMerchantOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantOrderSyncResponse, self).__init__()
        self._distribute_result = None
        self._order_id = None
        self._order_status = None
        self._record_id = None

    @property
    def distribute_result(self):
        return self._distribute_result

    @distribute_result.setter
    def distribute_result(self, value):
        if isinstance(value, list):
            self._distribute_result = list()
            for i in value:
                if isinstance(i, OrderDataDistributeInfo):
                    self._distribute_result.append(i)
                else:
                    self._distribute_result.append(OrderDataDistributeInfo.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantOrderSyncResponse, self).parse_response_content(response_content)
        if 'distribute_result' in response:
            self.distribute_result = response['distribute_result']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'record_id' in response:
            self.record_id = response['record_id']

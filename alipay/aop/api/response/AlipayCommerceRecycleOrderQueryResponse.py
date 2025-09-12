#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleSubOrderInfoVO import RecycleSubOrderInfoVO


class AlipayCommerceRecycleOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleOrderQueryResponse, self).__init__()
        self._open_id = None
        self._order_id = None
        self._order_status = None
        self._out_order_id = None
        self._sub_order_info_list = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def sub_order_info_list(self):
        return self._sub_order_info_list

    @sub_order_info_list.setter
    def sub_order_info_list(self, value):
        if isinstance(value, list):
            self._sub_order_info_list = list()
            for i in value:
                if isinstance(i, RecycleSubOrderInfoVO):
                    self._sub_order_info_list.append(i)
                else:
                    self._sub_order_info_list.append(RecycleSubOrderInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleOrderQueryResponse, self).parse_response_content(response_content)
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'sub_order_info_list' in response:
            self.sub_order_info_list = response['sub_order_info_list']

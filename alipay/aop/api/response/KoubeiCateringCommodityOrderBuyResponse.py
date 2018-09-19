#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringCommodityOrderBuyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringCommodityOrderBuyResponse, self).__init__()
        self._ext_info = None
        self._order_id = None
        self._order_result = None
        self._order_result_msg = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                self._ext_info.append(i)
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_result(self):
        return self._order_result

    @order_result.setter
    def order_result(self, value):
        self._order_result = value
    @property
    def order_result_msg(self):
        return self._order_result_msg

    @order_result_msg.setter
    def order_result_msg(self, value):
        self._order_result_msg = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringCommodityOrderBuyResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_result' in response:
            self.order_result = response['order_result']
        if 'order_result_msg' in response:
            self.order_result_msg = response['order_result_msg']

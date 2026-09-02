#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDapplyApplyorderCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDapplyApplyorderCancelResponse, self).__init__()
        self._order_biz_id = None
        self._order_status = None

    @property
    def order_biz_id(self):
        return self._order_biz_id

    @order_biz_id.setter
    def order_biz_id(self, value):
        self._order_biz_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDapplyApplyorderCancelResponse, self).parse_response_content(response_content)
        if 'order_biz_id' in response:
            self.order_biz_id = response['order_biz_id']
        if 'order_status' in response:
            self.order_status = response['order_status']

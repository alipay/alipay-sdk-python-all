#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationDistributionFloworderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDistributionFloworderCreateResponse, self).__init__()
        self._alipay_order_id = None
        self._alipay_user_id = None
        self._inst_order_id = None
        self._open_id = None
        self._order_status = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def inst_order_id(self):
        return self._inst_order_id

    @inst_order_id.setter
    def inst_order_id(self, value):
        self._inst_order_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDistributionFloworderCreateResponse, self).parse_response_content(response_content)
        if 'alipay_order_id' in response:
            self.alipay_order_id = response['alipay_order_id']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'inst_order_id' in response:
            self.inst_order_id = response['inst_order_id']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_status' in response:
            self.order_status = response['order_status']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizOrderMessage import BizOrderMessage


class AlipayCommerceAcommunicationDistributionOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDistributionOrderQueryResponse, self).__init__()
        self._alipay_order_id = None
        self._biz_order_message_list = None
        self._inst_order_id = None
        self._order_status = None
        self._order_status_code = None
        self._order_status_desc = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def biz_order_message_list(self):
        return self._biz_order_message_list

    @biz_order_message_list.setter
    def biz_order_message_list(self, value):
        if isinstance(value, list):
            self._biz_order_message_list = list()
            for i in value:
                if isinstance(i, BizOrderMessage):
                    self._biz_order_message_list.append(i)
                else:
                    self._biz_order_message_list.append(BizOrderMessage.from_alipay_dict(i))
    @property
    def inst_order_id(self):
        return self._inst_order_id

    @inst_order_id.setter
    def inst_order_id(self, value):
        self._inst_order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_status_code(self):
        return self._order_status_code

    @order_status_code.setter
    def order_status_code(self, value):
        self._order_status_code = value
    @property
    def order_status_desc(self):
        return self._order_status_desc

    @order_status_desc.setter
    def order_status_desc(self, value):
        self._order_status_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDistributionOrderQueryResponse, self).parse_response_content(response_content)
        if 'alipay_order_id' in response:
            self.alipay_order_id = response['alipay_order_id']
        if 'biz_order_message_list' in response:
            self.biz_order_message_list = response['biz_order_message_list']
        if 'inst_order_id' in response:
            self.inst_order_id = response['inst_order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'order_status_code' in response:
            self.order_status_code = response['order_status_code']
        if 'order_status_desc' in response:
            self.order_status_desc = response['order_status_desc']

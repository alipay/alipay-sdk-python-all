#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QWOrderInfo import QWOrderInfo


class AlipayCommerceAcommunicationMcpPhoneCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationMcpPhoneCreateResponse, self).__init__()
        self._bill_no = None
        self._order_jump_url = None
        self._plain_text = None
        self._pre_pay_id = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def order_jump_url(self):
        return self._order_jump_url

    @order_jump_url.setter
    def order_jump_url(self, value):
        self._order_jump_url = value
    @property
    def plain_text(self):
        return self._plain_text

    @plain_text.setter
    def plain_text(self, value):
        if isinstance(value, QWOrderInfo):
            self._plain_text = value
        else:
            self._plain_text = QWOrderInfo.from_alipay_dict(value)
    @property
    def pre_pay_id(self):
        return self._pre_pay_id

    @pre_pay_id.setter
    def pre_pay_id(self, value):
        self._pre_pay_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationMcpPhoneCreateResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'order_jump_url' in response:
            self.order_jump_url = response['order_jump_url']
        if 'plain_text' in response:
            self.plain_text = response['plain_text']
        if 'pre_pay_id' in response:
            self.pre_pay_id = response['pre_pay_id']

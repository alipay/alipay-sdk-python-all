#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationCreditphoneOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCreditphoneOrderQueryResponse, self).__init__()
        self._alipay_order_no = None
        self._alipay_user_id = None
        self._freeze_amount = None
        self._page_order_no = None
        self._sign_time = None
        self._status = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def page_order_no(self):
        return self._page_order_no

    @page_order_no.setter
    def page_order_no(self, value):
        self._page_order_no = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCreditphoneOrderQueryResponse, self).parse_response_content(response_content)
        if 'alipay_order_no' in response:
            self.alipay_order_no = response['alipay_order_no']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'freeze_amount' in response:
            self.freeze_amount = response['freeze_amount']
        if 'page_order_no' in response:
            self.page_order_no = response['page_order_no']
        if 'sign_time' in response:
            self.sign_time = response['sign_time']
        if 'status' in response:
            self.status = response['status']

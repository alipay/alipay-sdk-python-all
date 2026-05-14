#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationCreditphoneOnlineadvanceresultNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCreditphoneOnlineadvanceresultNotifyResponse, self).__init__()
        self._alipay_online_advance_pay_order_no = None

    @property
    def alipay_online_advance_pay_order_no(self):
        return self._alipay_online_advance_pay_order_no

    @alipay_online_advance_pay_order_no.setter
    def alipay_online_advance_pay_order_no(self, value):
        self._alipay_online_advance_pay_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCreditphoneOnlineadvanceresultNotifyResponse, self).parse_response_content(response_content)
        if 'alipay_online_advance_pay_order_no' in response:
            self.alipay_online_advance_pay_order_no = response['alipay_online_advance_pay_order_no']

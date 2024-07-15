#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcenterpriseActivedorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseActivedorderCreateResponse, self).__init__()
        self._biz_agreement_no = None
        self._order_id = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseActivedorderCreateResponse, self).parse_response_content(response_content)
        if 'biz_agreement_no' in response:
            self.biz_agreement_no = response['biz_agreement_no']
        if 'order_id' in response:
            self.order_id = response['order_id']

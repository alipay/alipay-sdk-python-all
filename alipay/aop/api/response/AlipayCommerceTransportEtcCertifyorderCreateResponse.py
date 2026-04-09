#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcCertifyorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcCertifyorderCreateResponse, self).__init__()
        self._alipay_order_id = None
        self._biz_agreement_no = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcCertifyorderCreateResponse, self).parse_response_content(response_content)
        if 'alipay_order_id' in response:
            self.alipay_order_id = response['alipay_order_id']
        if 'biz_agreement_no' in response:
            self.biz_agreement_no = response['biz_agreement_no']

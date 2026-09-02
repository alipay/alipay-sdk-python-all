#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportExpresswayTripUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportExpresswayTripUnsignResponse, self).__init__()
        self._biz_agreement_no = None
        self._biz_status = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportExpresswayTripUnsignResponse, self).parse_response_content(response_content)
        if 'biz_agreement_no' in response:
            self.biz_agreement_no = response['biz_agreement_no']
        if 'biz_status' in response:
            self.biz_status = response['biz_status']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcDevicetripSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcDevicetripSendResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcDevicetripSendResponse, self).parse_response_content(response_content)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPayafteruseFusionquotaSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPayafteruseFusionquotaSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPayafteruseFusionquotaSyncResponse, self).parse_response_content(response_content)

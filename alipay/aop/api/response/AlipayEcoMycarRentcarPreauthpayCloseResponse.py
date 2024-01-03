#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarRentcarPreauthpayCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarRentcarPreauthpayCloseResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarRentcarPreauthpayCloseResponse, self).parse_response_content(response_content)

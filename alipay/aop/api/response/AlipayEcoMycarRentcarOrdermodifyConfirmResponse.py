#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarRentcarOrdermodifyConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarRentcarOrdermodifyConfirmResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarRentcarOrdermodifyConfirmResponse, self).parse_response_content(response_content)

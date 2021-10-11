#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarVehicleServicenotifySendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarVehicleServicenotifySendResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarVehicleServicenotifySendResponse, self).parse_response_content(response_content)

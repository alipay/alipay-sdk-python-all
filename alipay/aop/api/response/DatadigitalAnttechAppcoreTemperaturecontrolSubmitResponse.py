#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAnttechAppcoreTemperaturecontrolSubmitResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechAppcoreTemperaturecontrolSubmitResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechAppcoreTemperaturecontrolSubmitResponse, self).parse_response_content(response_content)

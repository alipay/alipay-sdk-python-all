#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppBoyiBoyiCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppBoyiBoyiCreateResponse, self).__init__()
        self._esd = None
        self._output = None

    @property
    def esd(self):
        return self._esd

    @esd.setter
    def esd(self, value):
        self._esd = value
    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppBoyiBoyiCreateResponse, self).parse_response_content(response_content)
        if 'esd' in response:
            self.esd = response['esd']
        if 'output' in response:
            self.output = response['output']

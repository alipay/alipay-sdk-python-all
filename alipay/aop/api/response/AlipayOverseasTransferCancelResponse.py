#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTransferCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTransferCancelResponse, self).__init__()
        self._pass_through_info = None

    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTransferCancelResponse, self).parse_response_content(response_content)
        if 'pass_through_info' in response:
            self.pass_through_info = response['pass_through_info']

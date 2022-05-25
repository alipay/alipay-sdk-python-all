#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ManjiangTestttttt import ManjiangTestttttt


class AlipayCommerceAcommunicationSsmmmmmCaptureResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationSsmmmmmCaptureResponse, self).__init__()
        self._sds = None

    @property
    def sds(self):
        return self._sds

    @sds.setter
    def sds(self, value):
        if isinstance(value, ManjiangTestttttt):
            self._sds = value
        else:
            self._sds = ManjiangTestttttt.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationSsmmmmmCaptureResponse, self).parse_response_content(response_content)
        if 'sds' in response:
            self.sds = response['sds']

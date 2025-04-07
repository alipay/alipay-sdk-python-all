#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftCtocTransferQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCtocTransferQueryResponse, self).__init__()
        self._transfer_status = None

    @property
    def transfer_status(self):
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, value):
        self._transfer_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftCtocTransferQueryResponse, self).parse_response_content(response_content)
        if 'transfer_status' in response:
            self.transfer_status = response['transfer_status']

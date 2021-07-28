#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTransferPaymentPrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTransferPaymentPrecreateResponse, self).__init__()
        self._pass_through_info = None
        self._transfer_id = None

    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def transfer_id(self):
        return self._transfer_id

    @transfer_id.setter
    def transfer_id(self, value):
        self._transfer_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTransferPaymentPrecreateResponse, self).parse_response_content(response_content)
        if 'pass_through_info' in response:
            self.pass_through_info = response['pass_through_info']
        if 'transfer_id' in response:
            self.transfer_id = response['transfer_id']

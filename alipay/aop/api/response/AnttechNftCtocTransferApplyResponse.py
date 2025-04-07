#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftCtocTransferApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCtocTransferApplyResponse, self).__init__()
        self._biz_id = None
        self._transfer_status = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def transfer_status(self):
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, value):
        self._transfer_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftCtocTransferApplyResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'transfer_status' in response:
            self.transfer_status = response['transfer_status']

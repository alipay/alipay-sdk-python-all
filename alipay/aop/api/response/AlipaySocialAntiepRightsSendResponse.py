#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntiepRightsSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntiepRightsSendResponse, self).__init__()
        self._idempotent = None

    @property
    def idempotent(self):
        return self._idempotent

    @idempotent.setter
    def idempotent(self, value):
        self._idempotent = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntiepRightsSendResponse, self).parse_response_content(response_content)
        if 'idempotent' in response:
            self.idempotent = response['idempotent']

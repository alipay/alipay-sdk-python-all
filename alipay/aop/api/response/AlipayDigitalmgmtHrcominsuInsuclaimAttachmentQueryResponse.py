#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtHrcominsuInsuclaimAttachmentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtHrcominsuInsuclaimAttachmentQueryResponse, self).__init__()
        self._attachment_stream = None

    @property
    def attachment_stream(self):
        return self._attachment_stream

    @attachment_stream.setter
    def attachment_stream(self, value):
        self._attachment_stream = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtHrcominsuInsuclaimAttachmentQueryResponse, self).parse_response_content(response_content)
        if 'attachment_stream' in response:
            self.attachment_stream = response['attachment_stream']

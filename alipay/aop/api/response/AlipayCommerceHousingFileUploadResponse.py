#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingFileUploadResponse, self).__init__()
        self._attachment_id = None

    @property
    def attachment_id(self):
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, value):
        self._attachment_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHousingFileUploadResponse, self).parse_response_content(response_content)
        if 'attachment_id' in response:
            self.attachment_id = response['attachment_id']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandEcoAttachmentUploadResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandEcoAttachmentUploadResponse, self).__init__()
        self._oss_key = None

    @property
    def oss_key(self):
        return self._oss_key

    @oss_key.setter
    def oss_key(self, value):
        self._oss_key = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandEcoAttachmentUploadResponse, self).parse_response_content(response_content)
        if 'oss_key' in response:
            self.oss_key = response['oss_key']

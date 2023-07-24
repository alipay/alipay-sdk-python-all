#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtAppUrlforuploadQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtAppUrlforuploadQueryResponse, self).__init__()
        self._url_for_upload_file = None

    @property
    def url_for_upload_file(self):
        return self._url_for_upload_file

    @url_for_upload_file.setter
    def url_for_upload_file(self, value):
        self._url_for_upload_file = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtAppUrlforuploadQueryResponse, self).parse_response_content(response_content)
        if 'url_for_upload_file' in response:
            self.url_for_upload_file = response['url_for_upload_file']

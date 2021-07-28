#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyIdentifyFileQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyIdentifyFileQueryResponse, self).__init__()
        self._file = None

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyIdentifyFileQueryResponse, self).parse_response_content(response_content)
        if 'file' in response:
            self.file = response['file']

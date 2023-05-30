#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceDspcreativeUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceDspcreativeUploadResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceDspcreativeUploadResponse, self).parse_response_content(response_content)

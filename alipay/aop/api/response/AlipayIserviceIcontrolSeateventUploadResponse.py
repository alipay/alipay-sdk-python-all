#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceIcontrolSeateventUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIcontrolSeateventUploadResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIcontrolSeateventUploadResponse, self).parse_response_content(response_content)

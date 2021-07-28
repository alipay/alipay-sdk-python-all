#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoAutoaftermarketAttachmentUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoAutoaftermarketAttachmentUploadResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoAutoaftermarketAttachmentUploadResponse, self).parse_response_content(response_content)

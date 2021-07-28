#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInsserviceprodSerattachmentUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInsserviceprodSerattachmentUploadResponse, self).__init__()
        self._attachment_no = None

    @property
    def attachment_no(self):
        return self._attachment_no

    @attachment_no.setter
    def attachment_no(self, value):
        self._attachment_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInsserviceprodSerattachmentUploadResponse, self).parse_response_content(response_content)
        if 'attachment_no' in response:
            self.attachment_no = response['attachment_no']

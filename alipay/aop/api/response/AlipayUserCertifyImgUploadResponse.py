#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyImgUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyImgUploadResponse, self).__init__()
        self._certificate_id = None
        self._pic_url = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyImgUploadResponse, self).parse_response_content(response_content)
        if 'certificate_id' in response:
            self.certificate_id = response['certificate_id']
        if 'pic_url' in response:
            self.pic_url = response['pic_url']

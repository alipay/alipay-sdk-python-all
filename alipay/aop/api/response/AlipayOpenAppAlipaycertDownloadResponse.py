#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppAlipaycertDownloadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppAlipaycertDownloadResponse, self).__init__()
        self._alipay_cert_content = None

    @property
    def alipay_cert_content(self):
        return self._alipay_cert_content

    @alipay_cert_content.setter
    def alipay_cert_content(self, value):
        self._alipay_cert_content = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppAlipaycertDownloadResponse, self).parse_response_content(response_content)
        if 'alipay_cert_content' in response:
            self.alipay_cert_content = response['alipay_cert_content']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantSolcreditserviceprodMerchantCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolcreditserviceprodMerchantCreateormodifyResponse, self).__init__()
        self._review_version_no = None
        self._version_no = None

    @property
    def review_version_no(self):
        return self._review_version_no

    @review_version_no.setter
    def review_version_no(self, value):
        self._review_version_no = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolcreditserviceprodMerchantCreateormodifyResponse, self).parse_response_content(response_content)
        if 'review_version_no' in response:
            self.review_version_no = response['review_version_no']
        if 'version_no' in response:
            self.version_no = response['version_no']

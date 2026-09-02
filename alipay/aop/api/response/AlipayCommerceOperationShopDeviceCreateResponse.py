#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationShopDeviceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationShopDeviceCreateResponse, self).__init__()
        self._submission_no = None

    @property
    def submission_no(self):
        return self._submission_no

    @submission_no.setter
    def submission_no(self, value):
        self._submission_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationShopDeviceCreateResponse, self).parse_response_content(response_content)
        if 'submission_no' in response:
            self.submission_no = response['submission_no']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoFaceCheckCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoFaceCheckCreateResponse, self).__init__()
        self._verify_biz_no = None
        self._verify_id = None
        self._verify_url = None

    @property
    def verify_biz_no(self):
        return self._verify_biz_no

    @verify_biz_no.setter
    def verify_biz_no(self, value):
        self._verify_biz_no = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value
    @property
    def verify_url(self):
        return self._verify_url

    @verify_url.setter
    def verify_url(self, value):
        self._verify_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoFaceCheckCreateResponse, self).parse_response_content(response_content)
        if 'verify_biz_no' in response:
            self.verify_biz_no = response['verify_biz_no']
        if 'verify_id' in response:
            self.verify_id = response['verify_id']
        if 'verify_url' in response:
            self.verify_url = response['verify_url']

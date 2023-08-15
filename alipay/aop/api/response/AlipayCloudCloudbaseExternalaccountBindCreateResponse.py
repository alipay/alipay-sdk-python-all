#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseExternalaccountBindCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseExternalaccountBindCreateResponse, self).__init__()
        self._biz_app_id = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseExternalaccountBindCreateResponse, self).parse_response_content(response_content)
        if 'biz_app_id' in response:
            self.biz_app_id = response['biz_app_id']

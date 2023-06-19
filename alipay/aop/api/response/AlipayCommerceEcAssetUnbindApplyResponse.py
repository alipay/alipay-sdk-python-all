#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcAssetUnbindApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcAssetUnbindApplyResponse, self).__init__()
        self._cancel_authorize_link = None

    @property
    def cancel_authorize_link(self):
        return self._cancel_authorize_link

    @cancel_authorize_link.setter
    def cancel_authorize_link(self, value):
        self._cancel_authorize_link = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcAssetUnbindApplyResponse, self).parse_response_content(response_content)
        if 'cancel_authorize_link' in response:
            self.cancel_authorize_link = response['cancel_authorize_link']

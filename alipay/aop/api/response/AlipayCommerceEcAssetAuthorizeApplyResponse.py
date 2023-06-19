#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcAssetAuthorizeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcAssetAuthorizeApplyResponse, self).__init__()
        self._authorize_link = None
        self._status = None

    @property
    def authorize_link(self):
        return self._authorize_link

    @authorize_link.setter
    def authorize_link(self, value):
        self._authorize_link = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcAssetAuthorizeApplyResponse, self).parse_response_content(response_content)
        if 'authorize_link' in response:
            self.authorize_link = response['authorize_link']
        if 'status' in response:
            self.status = response['status']

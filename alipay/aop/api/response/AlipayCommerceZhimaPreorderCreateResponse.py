#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceZhimaPreorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceZhimaPreorderCreateResponse, self).__init__()
        self._biz_type = None
        self._partner_id = None
        self._preorder_no = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def preorder_no(self):
        return self._preorder_no

    @preorder_no.setter
    def preorder_no(self, value):
        self._preorder_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceZhimaPreorderCreateResponse, self).parse_response_content(response_content)
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'preorder_no' in response:
            self.preorder_no = response['preorder_no']

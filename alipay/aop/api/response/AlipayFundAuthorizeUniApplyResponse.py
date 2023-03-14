#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAuthorizeUniApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAuthorizeUniApplyResponse, self).__init__()
        self._authorize_link = None
        self._authorize_link_type = None
        self._biz_scene = None
        self._out_biz_no = None
        self._product_code = None

    @property
    def authorize_link(self):
        return self._authorize_link

    @authorize_link.setter
    def authorize_link(self, value):
        self._authorize_link = value
    @property
    def authorize_link_type(self):
        return self._authorize_link_type

    @authorize_link_type.setter
    def authorize_link_type(self, value):
        self._authorize_link_type = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAuthorizeUniApplyResponse, self).parse_response_content(response_content)
        if 'authorize_link' in response:
            self.authorize_link = response['authorize_link']
        if 'authorize_link_type' in response:
            self.authorize_link_type = response['authorize_link_type']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'product_code' in response:
            self.product_code = response['product_code']

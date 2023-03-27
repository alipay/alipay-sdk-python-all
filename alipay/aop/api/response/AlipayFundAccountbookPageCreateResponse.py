#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAccountbookPageCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountbookPageCreateResponse, self).__init__()
        self._biz_scene = None
        self._out_biz_no = None
        self._process_status = None
        self._product_code = None

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
    def process_status(self):
        return self._process_status

    @process_status.setter
    def process_status(self, value):
        self._process_status = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountbookPageCreateResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'process_status' in response:
            self.process_status = response['process_status']
        if 'product_code' in response:
            self.product_code = response['product_code']

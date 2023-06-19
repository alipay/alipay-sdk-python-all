#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcAssetValidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcAssetValidQueryResponse, self).__init__()
        self._asset_type = None
        self._out_biz_no = None

    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcAssetValidQueryResponse, self).parse_response_content(response_content)
        if 'asset_type' in response:
            self.asset_type = response['asset_type']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']

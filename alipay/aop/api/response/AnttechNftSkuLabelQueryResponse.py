#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftSkuLabelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftSkuLabelQueryResponse, self).__init__()
        self._sku_label_color = None

    @property
    def sku_label_color(self):
        return self._sku_label_color

    @sku_label_color.setter
    def sku_label_color(self, value):
        self._sku_label_color = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftSkuLabelQueryResponse, self).parse_response_content(response_content)
        if 'sku_label_color' in response:
            self.sku_label_color = response['sku_label_color']

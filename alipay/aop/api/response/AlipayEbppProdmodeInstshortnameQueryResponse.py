#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppProdmodeInstshortnameQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppProdmodeInstshortnameQueryResponse, self).__init__()
        self._chargeinst_cn_name = None
        self._chargeinst_en_name = None

    @property
    def chargeinst_cn_name(self):
        return self._chargeinst_cn_name

    @chargeinst_cn_name.setter
    def chargeinst_cn_name(self, value):
        self._chargeinst_cn_name = value
    @property
    def chargeinst_en_name(self):
        return self._chargeinst_en_name

    @chargeinst_en_name.setter
    def chargeinst_en_name(self, value):
        self._chargeinst_en_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppProdmodeInstshortnameQueryResponse, self).parse_response_content(response_content)
        if 'chargeinst_cn_name' in response:
            self.chargeinst_cn_name = response['chargeinst_cn_name']
        if 'chargeinst_en_name' in response:
            self.chargeinst_en_name = response['chargeinst_en_name']

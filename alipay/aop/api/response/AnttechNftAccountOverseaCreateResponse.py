#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftAccountOverseaCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftAccountOverseaCreateResponse, self).__init__()
        self._oversea_id_no = None

    @property
    def oversea_id_no(self):
        return self._oversea_id_no

    @oversea_id_no.setter
    def oversea_id_no(self, value):
        self._oversea_id_no = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftAccountOverseaCreateResponse, self).parse_response_content(response_content)
        if 'oversea_id_no' in response:
            self.oversea_id_no = response['oversea_id_no']

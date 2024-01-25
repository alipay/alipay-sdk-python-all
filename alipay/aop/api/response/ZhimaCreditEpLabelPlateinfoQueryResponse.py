#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpLabelPlateinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpLabelPlateinfoQueryResponse, self).__init__()
        self._hd_pic_src = None

    @property
    def hd_pic_src(self):
        return self._hd_pic_src

    @hd_pic_src.setter
    def hd_pic_src(self, value):
        self._hd_pic_src = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpLabelPlateinfoQueryResponse, self).parse_response_content(response_content)
        if 'hd_pic_src' in response:
            self.hd_pic_src = response['hd_pic_src']

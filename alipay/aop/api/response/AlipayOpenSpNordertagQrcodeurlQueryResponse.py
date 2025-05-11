#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NOrderTagQueryByCoilNoResp import NOrderTagQueryByCoilNoResp


class AlipayOpenSpNordertagQrcodeurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordertagQrcodeurlQueryResponse, self).__init__()
        self._tag_info = None

    @property
    def tag_info(self):
        return self._tag_info

    @tag_info.setter
    def tag_info(self, value):
        if isinstance(value, NOrderTagQueryByCoilNoResp):
            self._tag_info = value
        else:
            self._tag_info = NOrderTagQueryByCoilNoResp.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordertagQrcodeurlQueryResponse, self).parse_response_content(response_content)
        if 'tag_info' in response:
            self.tag_info = response['tag_info']

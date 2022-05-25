#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SignatoryInfoMap import SignatoryInfoMap


class AlipayUserSignatoryInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSignatoryInfoQueryResponse, self).__init__()
        self._out_put_map = None

    @property
    def out_put_map(self):
        return self._out_put_map

    @out_put_map.setter
    def out_put_map(self, value):
        if isinstance(value, SignatoryInfoMap):
            self._out_put_map = value
        else:
            self._out_put_map = SignatoryInfoMap.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserSignatoryInfoQueryResponse, self).parse_response_content(response_content)
        if 'out_put_map' in response:
            self.out_put_map = response['out_put_map']

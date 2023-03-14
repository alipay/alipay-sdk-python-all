#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsOpenYfxInfoDTO import InsOpenYfxInfoDTO


class AlipayInsSceneYfxDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneYfxDetailQueryResponse, self).__init__()
        self._yfx_info = None

    @property
    def yfx_info(self):
        return self._yfx_info

    @yfx_info.setter
    def yfx_info(self, value):
        if isinstance(value, InsOpenYfxInfoDTO):
            self._yfx_info = value
        else:
            self._yfx_info = InsOpenYfxInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneYfxDetailQueryResponse, self).parse_response_content(response_content)
        if 'yfx_info' in response:
            self.yfx_info = response['yfx_info']

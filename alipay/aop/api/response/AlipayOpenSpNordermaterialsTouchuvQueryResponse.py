#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TouchUvInfo import TouchUvInfo


class AlipayOpenSpNordermaterialsTouchuvQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsTouchuvQueryResponse, self).__init__()
        self._touch_uv_infos = None

    @property
    def touch_uv_infos(self):
        return self._touch_uv_infos

    @touch_uv_infos.setter
    def touch_uv_infos(self, value):
        if isinstance(value, list):
            self._touch_uv_infos = list()
            for i in value:
                if isinstance(i, TouchUvInfo):
                    self._touch_uv_infos.append(i)
                else:
                    self._touch_uv_infos.append(TouchUvInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsTouchuvQueryResponse, self).parse_response_content(response_content)
        if 'touch_uv_infos' in response:
            self.touch_uv_infos = response['touch_uv_infos']

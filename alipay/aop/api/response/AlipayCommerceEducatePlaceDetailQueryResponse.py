#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduPlaceInfo import EduPlaceInfo


class AlipayCommerceEducatePlaceDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducatePlaceDetailQueryResponse, self).__init__()
        self._place_info = None

    @property
    def place_info(self):
        return self._place_info

    @place_info.setter
    def place_info(self, value):
        if isinstance(value, EduPlaceInfo):
            self._place_info = value
        else:
            self._place_info = EduPlaceInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducatePlaceDetailQueryResponse, self).parse_response_content(response_content)
        if 'place_info' in response:
            self.place_info = response['place_info']

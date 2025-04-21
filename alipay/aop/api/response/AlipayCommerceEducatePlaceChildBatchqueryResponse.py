#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduPlaceInfo import EduPlaceInfo


class AlipayCommerceEducatePlaceChildBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducatePlaceChildBatchqueryResponse, self).__init__()
        self._place_list = None

    @property
    def place_list(self):
        return self._place_list

    @place_list.setter
    def place_list(self, value):
        if isinstance(value, list):
            self._place_list = list()
            for i in value:
                if isinstance(i, EduPlaceInfo):
                    self._place_list.append(i)
                else:
                    self._place_list.append(EduPlaceInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducatePlaceChildBatchqueryResponse, self).parse_response_content(response_content)
        if 'place_list' in response:
            self.place_list = response['place_list']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduPlaceInfo import EduPlaceInfo


class AlipayCommerceEducatePlaceInfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducatePlaceInfoBatchqueryResponse, self).__init__()
        self._place_info_list = None
        self._total_num = None

    @property
    def place_info_list(self):
        return self._place_info_list

    @place_info_list.setter
    def place_info_list(self, value):
        if isinstance(value, list):
            self._place_info_list = list()
            for i in value:
                if isinstance(i, EduPlaceInfo):
                    self._place_info_list.append(i)
                else:
                    self._place_info_list.append(EduPlaceInfo.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducatePlaceInfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'place_info_list' in response:
            self.place_info_list = response['place_info_list']
        if 'total_num' in response:
            self.total_num = response['total_num']

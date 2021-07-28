#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaginationScenicInfo import PaginationScenicInfo


class AlipayCommerceDataScenicQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDataScenicQueryResponse, self).__init__()
        self._pagination_scenic_info = None

    @property
    def pagination_scenic_info(self):
        return self._pagination_scenic_info

    @pagination_scenic_info.setter
    def pagination_scenic_info(self, value):
        if isinstance(value, PaginationScenicInfo):
            self._pagination_scenic_info = value
        else:
            self._pagination_scenic_info = PaginationScenicInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDataScenicQueryResponse, self).parse_response_content(response_content)
        if 'pagination_scenic_info' in response:
            self.pagination_scenic_info = response['pagination_scenic_info']

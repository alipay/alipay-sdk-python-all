#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceContentDTO import DeviceContentDTO


class AlipayCommercePropertyRiskdetectContentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyRiskdetectContentQueryResponse, self).__init__()
        self._content_results = None
        self._total = None

    @property
    def content_results(self):
        return self._content_results

    @content_results.setter
    def content_results(self, value):
        if isinstance(value, list):
            self._content_results = list()
            for i in value:
                if isinstance(i, DeviceContentDTO):
                    self._content_results.append(i)
                else:
                    self._content_results.append(DeviceContentDTO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyRiskdetectContentQueryResponse, self).parse_response_content(response_content)
        if 'content_results' in response:
            self.content_results = response['content_results']
        if 'total' in response:
            self.total = response['total']

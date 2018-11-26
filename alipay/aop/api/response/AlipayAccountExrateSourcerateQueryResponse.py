#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExSourceRateVO import ExSourceRateVO


class AlipayAccountExrateSourcerateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountExrateSourcerateQueryResponse, self).__init__()
        self._source_rate_list = None

    @property
    def source_rate_list(self):
        return self._source_rate_list

    @source_rate_list.setter
    def source_rate_list(self, value):
        if isinstance(value, list):
            self._source_rate_list = list()
            for i in value:
                if isinstance(i, ExSourceRateVO):
                    self._source_rate_list.append(i)
                else:
                    self._source_rate_list.append(ExSourceRateVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayAccountExrateSourcerateQueryResponse, self).parse_response_content(response_content)
        if 'source_rate_list' in response:
            self.source_rate_list = response['source_rate_list']

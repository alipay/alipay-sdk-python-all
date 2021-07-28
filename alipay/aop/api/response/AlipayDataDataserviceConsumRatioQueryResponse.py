#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RatioDetail import RatioDetail


class AlipayDataDataserviceConsumRatioQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceConsumRatioQueryResponse, self).__init__()
        self._ratio_detail = None

    @property
    def ratio_detail(self):
        return self._ratio_detail

    @ratio_detail.setter
    def ratio_detail(self, value):
        if isinstance(value, RatioDetail):
            self._ratio_detail = value
        else:
            self._ratio_detail = RatioDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceConsumRatioQueryResponse, self).parse_response_content(response_content)
        if 'ratio_detail' in response:
            self.ratio_detail = response['ratio_detail']

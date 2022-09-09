#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsQuoteDTO import InsQuoteDTO


class AlipayInsSceneQuoteDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneQuoteDetailQueryResponse, self).__init__()
        self._quote_detail = None

    @property
    def quote_detail(self):
        return self._quote_detail

    @quote_detail.setter
    def quote_detail(self, value):
        if isinstance(value, InsQuoteDTO):
            self._quote_detail = value
        else:
            self._quote_detail = InsQuoteDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneQuoteDetailQueryResponse, self).parse_response_content(response_content)
        if 'quote_detail' in response:
            self.quote_detail = response['quote_detail']

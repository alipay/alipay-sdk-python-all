#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuoteInfo import QuoteInfo


class AlipayInsAutoAutoinsprodQuoteApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoAutoinsprodQuoteApplyResponse, self).__init__()
        self._enquiry_biz_id = None
        self._quote_infos = None

    @property
    def enquiry_biz_id(self):
        return self._enquiry_biz_id

    @enquiry_biz_id.setter
    def enquiry_biz_id(self, value):
        self._enquiry_biz_id = value
    @property
    def quote_infos(self):
        return self._quote_infos

    @quote_infos.setter
    def quote_infos(self, value):
        if isinstance(value, list):
            self._quote_infos = list()
            for i in value:
                if isinstance(i, QuoteInfo):
                    self._quote_infos.append(i)
                else:
                    self._quote_infos.append(QuoteInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoAutoinsprodQuoteApplyResponse, self).parse_response_content(response_content)
        if 'enquiry_biz_id' in response:
            self.enquiry_biz_id = response['enquiry_biz_id']
        if 'quote_infos' in response:
            self.quote_infos = response['quote_infos']

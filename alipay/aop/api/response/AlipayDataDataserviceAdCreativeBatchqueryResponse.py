#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PageCreative import PageCreative


class AlipayDataDataserviceAdCreativeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdCreativeBatchqueryResponse, self).__init__()
        self._creative_list = None

    @property
    def creative_list(self):
        return self._creative_list

    @creative_list.setter
    def creative_list(self, value):
        if isinstance(value, PageCreative):
            self._creative_list = value
        else:
            self._creative_list = PageCreative.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdCreativeBatchqueryResponse, self).parse_response_content(response_content)
        if 'creative_list' in response:
            self.creative_list = response['creative_list']

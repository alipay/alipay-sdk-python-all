#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AftersalesInfo import AftersalesInfo


class AlipayCommerceMerchantcardAftersalesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardAftersalesQueryResponse, self).__init__()
        self._aftersales_info = None

    @property
    def aftersales_info(self):
        return self._aftersales_info

    @aftersales_info.setter
    def aftersales_info(self, value):
        if isinstance(value, AftersalesInfo):
            self._aftersales_info = value
        else:
            self._aftersales_info = AftersalesInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardAftersalesQueryResponse, self).parse_response_content(response_content)
        if 'aftersales_info' in response:
            self.aftersales_info = response['aftersales_info']

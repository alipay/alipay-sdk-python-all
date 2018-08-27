#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Retailer import Retailer


class KoubeiMemberRetailerQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMemberRetailerQueryResponse, self).__init__()
        self._retailer_list = None

    @property
    def retailer_list(self):
        return self._retailer_list

    @retailer_list.setter
    def retailer_list(self, value):
        if isinstance(value, list):
            self._retailer_list = list()
            for i in value:
                if isinstance(i, Retailer):
                    self._retailer_list.append(i)
                else:
                    self._retailer_list.append(Retailer.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMemberRetailerQueryResponse, self).parse_response_content(response_content)
        if 'retailer_list' in response:
            self.retailer_list = response['retailer_list']

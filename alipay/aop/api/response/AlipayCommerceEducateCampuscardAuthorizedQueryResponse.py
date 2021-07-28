#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SchoolCardSimpleInfo import SchoolCardSimpleInfo


class AlipayCommerceEducateCampuscardAuthorizedQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampuscardAuthorizedQueryResponse, self).__init__()
        self._alipay_card_simple_list = None

    @property
    def alipay_card_simple_list(self):
        return self._alipay_card_simple_list

    @alipay_card_simple_list.setter
    def alipay_card_simple_list(self, value):
        if isinstance(value, list):
            self._alipay_card_simple_list = list()
            for i in value:
                if isinstance(i, SchoolCardSimpleInfo):
                    self._alipay_card_simple_list.append(i)
                else:
                    self._alipay_card_simple_list.append(SchoolCardSimpleInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampuscardAuthorizedQueryResponse, self).parse_response_content(response_content)
        if 'alipay_card_simple_list' in response:
            self.alipay_card_simple_list = response['alipay_card_simple_list']

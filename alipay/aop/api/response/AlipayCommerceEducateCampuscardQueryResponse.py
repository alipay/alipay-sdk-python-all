#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SchoolCardInfo import SchoolCardInfo


class AlipayCommerceEducateCampuscardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampuscardQueryResponse, self).__init__()
        self._alipay_card_list = None

    @property
    def alipay_card_list(self):
        return self._alipay_card_list

    @alipay_card_list.setter
    def alipay_card_list(self, value):
        if isinstance(value, list):
            self._alipay_card_list = list()
            for i in value:
                if isinstance(i, SchoolCardInfo):
                    self._alipay_card_list.append(i)
                else:
                    self._alipay_card_list.append(SchoolCardInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampuscardQueryResponse, self).parse_response_content(response_content)
        if 'alipay_card_list' in response:
            self.alipay_card_list = response['alipay_card_list']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemDiscountDetailInfo import ItemDiscountDetailInfo


class AlipayOpenMiniPromodecisionConsultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPromodecisionConsultQueryResponse, self).__init__()
        self._discount_detail_info = None
        self._result_code = None

    @property
    def discount_detail_info(self):
        return self._discount_detail_info

    @discount_detail_info.setter
    def discount_detail_info(self, value):
        if isinstance(value, ItemDiscountDetailInfo):
            self._discount_detail_info = value
        else:
            self._discount_detail_info = ItemDiscountDetailInfo.from_alipay_dict(value)
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPromodecisionConsultQueryResponse, self).parse_response_content(response_content)
        if 'discount_detail_info' in response:
            self.discount_detail_info = response['discount_detail_info']
        if 'result_code' in response:
            self.result_code = response['result_code']

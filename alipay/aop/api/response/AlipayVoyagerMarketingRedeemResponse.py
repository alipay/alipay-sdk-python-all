#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayVoyagerMarketingRedeemResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerMarketingRedeemResponse, self).__init__()
        self._redeem_order_id = None
        self._result = None

    @property
    def redeem_order_id(self):
        return self._redeem_order_id

    @redeem_order_id.setter
    def redeem_order_id(self, value):
        self._redeem_order_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ResultInfoDTO):
            self._result = value
        else:
            self._result = ResultInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayVoyagerMarketingRedeemResponse, self).parse_response_content(response_content)
        if 'redeem_order_id' in response:
            self.redeem_order_id = response['redeem_order_id']
        if 'result' in response:
            self.result = response['result']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayVoyagerMarketingUnfreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerMarketingUnfreezeResponse, self).__init__()
        self._result = None
        self._unfreeze_order_id = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ResultInfoDTO):
            self._result = value
        else:
            self._result = ResultInfoDTO.from_alipay_dict(value)
    @property
    def unfreeze_order_id(self):
        return self._unfreeze_order_id

    @unfreeze_order_id.setter
    def unfreeze_order_id(self, value):
        self._unfreeze_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayVoyagerMarketingUnfreezeResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'unfreeze_order_id' in response:
            self.unfreeze_order_id = response['unfreeze_order_id']

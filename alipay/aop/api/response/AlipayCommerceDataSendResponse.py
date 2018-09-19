#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DataSendBusinessResult import DataSendBusinessResult


class AlipayCommerceDataSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDataSendResponse, self).__init__()
        self._data_send_business_result = None

    @property
    def data_send_business_result(self):
        return self._data_send_business_result

    @data_send_business_result.setter
    def data_send_business_result(self, value):
        if isinstance(value, DataSendBusinessResult):
            self._data_send_business_result = value
        else:
            self._data_send_business_result = DataSendBusinessResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDataSendResponse, self).parse_response_content(response_content)
        if 'data_send_business_result' in response:
            self.data_send_business_result = response['data_send_business_result']

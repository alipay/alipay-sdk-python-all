#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizActionLogDTO import BizActionLogDTO


class MyxiaojinFinanceAtsbudgetApplyResponse(AlipayResponse):

    def __init__(self):
        super(MyxiaojinFinanceAtsbudgetApplyResponse, self).__init__()
        self._result_data = None
        self._result_msg = None

    @property
    def result_data(self):
        return self._result_data

    @result_data.setter
    def result_data(self, value):
        if isinstance(value, list):
            self._result_data = list()
            for i in value:
                if isinstance(i, BizActionLogDTO):
                    self._result_data.append(i)
                else:
                    self._result_data.append(BizActionLogDTO.from_alipay_dict(i))
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(MyxiaojinFinanceAtsbudgetApplyResponse, self).parse_response_content(response_content)
        if 'result_data' in response:
            self.result_data = response['result_data']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShiftBaseInfo import ShiftBaseInfo


class AlipayIserviceIdeployShiftQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIdeployShiftQueryResponse, self).__init__()
        self._shift_list = None

    @property
    def shift_list(self):
        return self._shift_list

    @shift_list.setter
    def shift_list(self, value):
        if isinstance(value, list):
            self._shift_list = list()
            for i in value:
                if isinstance(i, ShiftBaseInfo):
                    self._shift_list.append(i)
                else:
                    self._shift_list.append(ShiftBaseInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIdeployShiftQueryResponse, self).parse_response_content(response_content)
        if 'shift_list' in response:
            self.shift_list = response['shift_list']

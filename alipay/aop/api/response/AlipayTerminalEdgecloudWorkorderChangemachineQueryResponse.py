#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IotCareWorkOrder import IotCareWorkOrder


class AlipayTerminalEdgecloudWorkorderChangemachineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTerminalEdgecloudWorkorderChangemachineQueryResponse, self).__init__()
        self._work_order_list = None

    @property
    def work_order_list(self):
        return self._work_order_list

    @work_order_list.setter
    def work_order_list(self, value):
        if isinstance(value, list):
            self._work_order_list = list()
            for i in value:
                if isinstance(i, IotCareWorkOrder):
                    self._work_order_list.append(i)
                else:
                    self._work_order_list.append(IotCareWorkOrder.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTerminalEdgecloudWorkorderChangemachineQueryResponse, self).parse_response_content(response_content)
        if 'work_order_list' in response:
            self.work_order_list = response['work_order_list']

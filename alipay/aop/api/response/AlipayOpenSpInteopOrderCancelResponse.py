#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InteopSubTaskOpInfoVO import InteopSubTaskOpInfoVO


class AlipayOpenSpInteopOrderCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpInteopOrderCancelResponse, self).__init__()
        self._inteop_order_no = None
        self._sub_task_op_infos = None

    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def sub_task_op_infos(self):
        return self._sub_task_op_infos

    @sub_task_op_infos.setter
    def sub_task_op_infos(self, value):
        if isinstance(value, list):
            self._sub_task_op_infos = list()
            for i in value:
                if isinstance(i, InteopSubTaskOpInfoVO):
                    self._sub_task_op_infos.append(i)
                else:
                    self._sub_task_op_infos.append(InteopSubTaskOpInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpInteopOrderCancelResponse, self).parse_response_content(response_content)
        if 'inteop_order_no' in response:
            self.inteop_order_no = response['inteop_order_no']
        if 'sub_task_op_infos' in response:
            self.sub_task_op_infos = response['sub_task_op_infos']

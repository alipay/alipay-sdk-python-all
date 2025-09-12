#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InteOpSubOrderInfo import InteOpSubOrderInfo


class AlipayOpenSpInteopOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpInteopOrderQueryResponse, self).__init__()
        self._inteop_order_no = None
        self._inteop_order_status = None
        self._inteop_sub_order_infos = None

    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def inteop_order_status(self):
        return self._inteop_order_status

    @inteop_order_status.setter
    def inteop_order_status(self, value):
        self._inteop_order_status = value
    @property
    def inteop_sub_order_infos(self):
        return self._inteop_sub_order_infos

    @inteop_sub_order_infos.setter
    def inteop_sub_order_infos(self, value):
        if isinstance(value, list):
            self._inteop_sub_order_infos = list()
            for i in value:
                if isinstance(i, InteOpSubOrderInfo):
                    self._inteop_sub_order_infos.append(i)
                else:
                    self._inteop_sub_order_infos.append(InteOpSubOrderInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpInteopOrderQueryResponse, self).parse_response_content(response_content)
        if 'inteop_order_no' in response:
            self.inteop_order_no = response['inteop_order_no']
        if 'inteop_order_status' in response:
            self.inteop_order_status = response['inteop_order_status']
        if 'inteop_sub_order_infos' in response:
            self.inteop_sub_order_infos = response['inteop_sub_order_infos']

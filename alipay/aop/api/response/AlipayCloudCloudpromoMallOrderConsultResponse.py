#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoMallOrderConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallOrderConsultResponse, self).__init__()
        self._order_id_list = None
        self._status = None

    @property
    def order_id_list(self):
        return self._order_id_list

    @order_id_list.setter
    def order_id_list(self, value):
        if isinstance(value, list):
            self._order_id_list = list()
            for i in value:
                self._order_id_list.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallOrderConsultResponse, self).parse_response_content(response_content)
        if 'order_id_list' in response:
            self.order_id_list = response['order_id_list']
        if 'status' in response:
            self.status = response['status']

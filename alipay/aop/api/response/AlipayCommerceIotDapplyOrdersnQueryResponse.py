#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDapplyOrdersnQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDapplyOrdersnQueryResponse, self).__init__()
        self._order_biz_id = None
        self._sn_list = None

    @property
    def order_biz_id(self):
        return self._order_biz_id

    @order_biz_id.setter
    def order_biz_id(self, value):
        self._order_biz_id = value
    @property
    def sn_list(self):
        return self._sn_list

    @sn_list.setter
    def sn_list(self, value):
        if isinstance(value, list):
            self._sn_list = list()
            for i in value:
                self._sn_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDapplyOrdersnQueryResponse, self).parse_response_content(response_content)
        if 'order_biz_id' in response:
            self.order_biz_id = response['order_biz_id']
        if 'sn_list' in response:
            self.sn_list = response['sn_list']

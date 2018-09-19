#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringOrderPushSignResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringOrderPushSignResponse, self).__init__()
        self._ext_infos = None
        self._order_id = None

    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringOrderPushSignResponse, self).parse_response_content(response_content)
        if 'ext_infos' in response:
            self.ext_infos = response['ext_infos']
        if 'order_id' in response:
            self.order_id = response['order_id']

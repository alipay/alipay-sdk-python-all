#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeGiftStatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeGiftStatusSyncResponse, self).__init__()
        self._recipient_open_id = None
        self._recipient_user_id = None
        self._tb_og_id = None
        self._tb_order_id = None

    @property
    def recipient_open_id(self):
        return self._recipient_open_id

    @recipient_open_id.setter
    def recipient_open_id(self, value):
        self._recipient_open_id = value
    @property
    def recipient_user_id(self):
        return self._recipient_user_id

    @recipient_user_id.setter
    def recipient_user_id(self, value):
        self._recipient_user_id = value
    @property
    def tb_og_id(self):
        return self._tb_og_id

    @tb_og_id.setter
    def tb_og_id(self, value):
        self._tb_og_id = value
    @property
    def tb_order_id(self):
        return self._tb_order_id

    @tb_order_id.setter
    def tb_order_id(self, value):
        self._tb_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeGiftStatusSyncResponse, self).parse_response_content(response_content)
        if 'recipient_open_id' in response:
            self.recipient_open_id = response['recipient_open_id']
        if 'recipient_user_id' in response:
            self.recipient_user_id = response['recipient_user_id']
        if 'tb_og_id' in response:
            self.tb_og_id = response['tb_og_id']
        if 'tb_order_id' in response:
            self.tb_order_id = response['tb_order_id']

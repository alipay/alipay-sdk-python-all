#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGamepaycoinTradeorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGamepaycoinTradeorderQueryResponse, self).__init__()
        self._bill_amount = None
        self._cp_extra = None
        self._goods_name = None
        self._refund_amount = None
        self._status = None
        self._zone_id = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def cp_extra(self):
        return self._cp_extra

    @cp_extra.setter
    def cp_extra(self, value):
        self._cp_extra = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def zone_id(self):
        return self._zone_id

    @zone_id.setter
    def zone_id(self, value):
        self._zone_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserGamepaycoinTradeorderQueryResponse, self).parse_response_content(response_content)
        if 'bill_amount' in response:
            self.bill_amount = response['bill_amount']
        if 'cp_extra' in response:
            self.cp_extra = response['cp_extra']
        if 'goods_name' in response:
            self.goods_name = response['goods_name']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'status' in response:
            self.status = response['status']
        if 'zone_id' in response:
            self.zone_id = response['zone_id']

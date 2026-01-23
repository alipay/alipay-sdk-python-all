#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradePeriodAccountGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePeriodAccountGetResponse, self).__init__()
        self._alipay_card_id = None
        self._bank_card_no = None
        self._inst_name = None
        self._overdraft_out_card_no = None
        self._postponed_time = None
        self._settle_way = None

    @property
    def alipay_card_id(self):
        return self._alipay_card_id

    @alipay_card_id.setter
    def alipay_card_id(self, value):
        self._alipay_card_id = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def overdraft_out_card_no(self):
        return self._overdraft_out_card_no

    @overdraft_out_card_no.setter
    def overdraft_out_card_no(self, value):
        self._overdraft_out_card_no = value
    @property
    def postponed_time(self):
        return self._postponed_time

    @postponed_time.setter
    def postponed_time(self, value):
        self._postponed_time = value
    @property
    def settle_way(self):
        return self._settle_way

    @settle_way.setter
    def settle_way(self, value):
        self._settle_way = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradePeriodAccountGetResponse, self).parse_response_content(response_content)
        if 'alipay_card_id' in response:
            self.alipay_card_id = response['alipay_card_id']
        if 'bank_card_no' in response:
            self.bank_card_no = response['bank_card_no']
        if 'inst_name' in response:
            self.inst_name = response['inst_name']
        if 'overdraft_out_card_no' in response:
            self.overdraft_out_card_no = response['overdraft_out_card_no']
        if 'postponed_time' in response:
            self.postponed_time = response['postponed_time']
        if 'settle_way' in response:
            self.settle_way = response['settle_way']

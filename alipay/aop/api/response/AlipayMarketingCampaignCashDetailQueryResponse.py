#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignCashDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignCashDetailQueryResponse, self).__init__()
        self._camp_status = None
        self._coupon_name = None
        self._crowd_no = None
        self._end_time = None
        self._origin_crowd_no = None
        self._prize_msg = None
        self._prize_type = None
        self._send_amount = None
        self._start_time = None
        self._total_amount = None
        self._total_count = None
        self._total_num = None

    @property
    def camp_status(self):
        return self._camp_status

    @camp_status.setter
    def camp_status(self, value):
        self._camp_status = value
    @property
    def coupon_name(self):
        return self._coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self._coupon_name = value
    @property
    def crowd_no(self):
        return self._crowd_no

    @crowd_no.setter
    def crowd_no(self, value):
        self._crowd_no = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def origin_crowd_no(self):
        return self._origin_crowd_no

    @origin_crowd_no.setter
    def origin_crowd_no(self, value):
        self._origin_crowd_no = value
    @property
    def prize_msg(self):
        return self._prize_msg

    @prize_msg.setter
    def prize_msg(self, value):
        self._prize_msg = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def send_amount(self):
        return self._send_amount

    @send_amount.setter
    def send_amount(self, value):
        self._send_amount = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignCashDetailQueryResponse, self).parse_response_content(response_content)
        if 'camp_status' in response:
            self.camp_status = response['camp_status']
        if 'coupon_name' in response:
            self.coupon_name = response['coupon_name']
        if 'crowd_no' in response:
            self.crowd_no = response['crowd_no']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'origin_crowd_no' in response:
            self.origin_crowd_no = response['origin_crowd_no']
        if 'prize_msg' in response:
            self.prize_msg = response['prize_msg']
        if 'prize_type' in response:
            self.prize_type = response['prize_type']
        if 'send_amount' in response:
            self.send_amount = response['send_amount']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_num' in response:
            self.total_num = response['total_num']

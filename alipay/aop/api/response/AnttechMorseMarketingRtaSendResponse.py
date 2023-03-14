#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SendEquityOrderResult import SendEquityOrderResult


class AnttechMorseMarketingRtaSendResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingRtaSendResponse, self).__init__()
        self._biz_no = None
        self._campaign_id = None
        self._send_equity_order_result_list = None
        self._send_order_id = None
        self._send_order_time = None
        self._send_status = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def send_equity_order_result_list(self):
        return self._send_equity_order_result_list

    @send_equity_order_result_list.setter
    def send_equity_order_result_list(self, value):
        if isinstance(value, SendEquityOrderResult):
            self._send_equity_order_result_list = value
        else:
            self._send_equity_order_result_list = SendEquityOrderResult.from_alipay_dict(value)
    @property
    def send_order_id(self):
        return self._send_order_id

    @send_order_id.setter
    def send_order_id(self, value):
        self._send_order_id = value
    @property
    def send_order_time(self):
        return self._send_order_time

    @send_order_time.setter
    def send_order_time(self, value):
        self._send_order_time = value
    @property
    def send_status(self):
        return self._send_status

    @send_status.setter
    def send_status(self, value):
        self._send_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingRtaSendResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'campaign_id' in response:
            self.campaign_id = response['campaign_id']
        if 'send_equity_order_result_list' in response:
            self.send_equity_order_result_list = response['send_equity_order_result_list']
        if 'send_order_id' in response:
            self.send_order_id = response['send_order_id']
        if 'send_order_time' in response:
            self.send_order_time = response['send_order_time']
        if 'send_status' in response:
            self.send_status = response['send_status']

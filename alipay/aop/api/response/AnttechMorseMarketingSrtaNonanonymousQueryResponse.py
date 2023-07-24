#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseMarketingSrtaNonanonymousQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingSrtaNonanonymousQueryResponse, self).__init__()
        self._biz_no = None
        self._campaign_id = None
        self._campaign_text = None
        self._campaign_text_type = None
        self._channel = None
        self._link = None
        self._max_amount = None
        self._min_amount = None
        self._need_deduct = None
        self._prize_type = None
        self._threshold = None

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
    def campaign_text(self):
        return self._campaign_text

    @campaign_text.setter
    def campaign_text(self, value):
        self._campaign_text = value
    @property
    def campaign_text_type(self):
        return self._campaign_text_type

    @campaign_text_type.setter
    def campaign_text_type(self, value):
        self._campaign_text_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def max_amount(self):
        return self._max_amount

    @max_amount.setter
    def max_amount(self, value):
        self._max_amount = value
    @property
    def min_amount(self):
        return self._min_amount

    @min_amount.setter
    def min_amount(self, value):
        self._min_amount = value
    @property
    def need_deduct(self):
        return self._need_deduct

    @need_deduct.setter
    def need_deduct(self, value):
        self._need_deduct = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingSrtaNonanonymousQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'campaign_id' in response:
            self.campaign_id = response['campaign_id']
        if 'campaign_text' in response:
            self.campaign_text = response['campaign_text']
        if 'campaign_text_type' in response:
            self.campaign_text_type = response['campaign_text_type']
        if 'channel' in response:
            self.channel = response['channel']
        if 'link' in response:
            self.link = response['link']
        if 'max_amount' in response:
            self.max_amount = response['max_amount']
        if 'min_amount' in response:
            self.min_amount = response['min_amount']
        if 'need_deduct' in response:
            self.need_deduct = response['need_deduct']
        if 'prize_type' in response:
            self.prize_type = response['prize_type']
        if 'threshold' in response:
            self.threshold = response['threshold']

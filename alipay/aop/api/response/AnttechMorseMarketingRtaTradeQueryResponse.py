#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseMarketingRtaTradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingRtaTradeQueryResponse, self).__init__()
        self._biz_no = None
        self._campaign_id = None
        self._discount_amt = None
        self._mobile_sha_256 = None
        self._out_biz_no = None
        self._payment_amt = None
        self._resource_id = None
        self._trade_date = None
        self._trade_no = None
        self._trade_status = None
        self._trade_total_amt = None
        self._trade_type = None

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
    def discount_amt(self):
        return self._discount_amt

    @discount_amt.setter
    def discount_amt(self, value):
        self._discount_amt = value
    @property
    def mobile_sha_256(self):
        return self._mobile_sha_256

    @mobile_sha_256.setter
    def mobile_sha_256(self, value):
        self._mobile_sha_256 = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payment_amt(self):
        return self._payment_amt

    @payment_amt.setter
    def payment_amt(self, value):
        self._payment_amt = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def trade_date(self):
        return self._trade_date

    @trade_date.setter
    def trade_date(self, value):
        self._trade_date = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value
    @property
    def trade_total_amt(self):
        return self._trade_total_amt

    @trade_total_amt.setter
    def trade_total_amt(self, value):
        self._trade_total_amt = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingRtaTradeQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'campaign_id' in response:
            self.campaign_id = response['campaign_id']
        if 'discount_amt' in response:
            self.discount_amt = response['discount_amt']
        if 'mobile_sha_256' in response:
            self.mobile_sha_256 = response['mobile_sha_256']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'payment_amt' in response:
            self.payment_amt = response['payment_amt']
        if 'resource_id' in response:
            self.resource_id = response['resource_id']
        if 'trade_date' in response:
            self.trade_date = response['trade_date']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
        if 'trade_total_amt' in response:
            self.trade_total_amt = response['trade_total_amt']
        if 'trade_type' in response:
            self.trade_type = response['trade_type']

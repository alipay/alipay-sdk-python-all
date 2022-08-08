#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignUnicardExcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignUnicardExcodeQueryResponse, self).__init__()
        self._can_exchange = None
        self._card_template_id = None
        self._city_code = None
        self._exchange_code = None
        self._expire_date = None
        self._gmt_create = None
        self._out_biz_no = None
        self._status = None
        self._un_exchange_cause = None

    @property
    def can_exchange(self):
        return self._can_exchange

    @can_exchange.setter
    def can_exchange(self, value):
        self._can_exchange = value
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def exchange_code(self):
        return self._exchange_code

    @exchange_code.setter
    def exchange_code(self, value):
        self._exchange_code = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def un_exchange_cause(self):
        return self._un_exchange_cause

    @un_exchange_cause.setter
    def un_exchange_cause(self, value):
        self._un_exchange_cause = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignUnicardExcodeQueryResponse, self).parse_response_content(response_content)
        if 'can_exchange' in response:
            self.can_exchange = response['can_exchange']
        if 'card_template_id' in response:
            self.card_template_id = response['card_template_id']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'exchange_code' in response:
            self.exchange_code = response['exchange_code']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
        if 'un_exchange_cause' in response:
            self.un_exchange_cause = response['un_exchange_cause']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiDonationServiceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiDonationServiceCreateResponse, self).__init__()
        self._biz_receipt = None
        self._donation_complete_link = None
        self._donation_id = None
        self._request_id = None

    @property
    def biz_receipt(self):
        return self._biz_receipt

    @biz_receipt.setter
    def biz_receipt(self, value):
        self._biz_receipt = value
    @property
    def donation_complete_link(self):
        return self._donation_complete_link

    @donation_complete_link.setter
    def donation_complete_link(self, value):
        self._donation_complete_link = value
    @property
    def donation_id(self):
        return self._donation_id

    @donation_id.setter
    def donation_id(self, value):
        self._donation_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiDonationServiceCreateResponse, self).parse_response_content(response_content)
        if 'biz_receipt' in response:
            self.biz_receipt = response['biz_receipt']
        if 'donation_complete_link' in response:
            self.donation_complete_link = response['donation_complete_link']
        if 'donation_id' in response:
            self.donation_id = response['donation_id']
        if 'request_id' in response:
            self.request_id = response['request_id']

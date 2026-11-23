#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCareerJobinterviewInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCareerJobinterviewInitializeResponse, self).__init__()
        self._interview_url = None
        self._order_no = None
        self._out_biz_no = None
        self._shorten_url = None
        self._status = None

    @property
    def interview_url(self):
        return self._interview_url

    @interview_url.setter
    def interview_url(self, value):
        self._interview_url = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def shorten_url(self):
        return self._shorten_url

    @shorten_url.setter
    def shorten_url(self, value):
        self._shorten_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCareerJobinterviewInitializeResponse, self).parse_response_content(response_content)
        if 'interview_url' in response:
            self.interview_url = response['interview_url']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'shorten_url' in response:
            self.shorten_url = response['shorten_url']
        if 'status' in response:
            self.status = response['status']

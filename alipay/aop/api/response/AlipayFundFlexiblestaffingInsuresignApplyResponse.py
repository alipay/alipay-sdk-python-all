#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundFlexiblestaffingInsuresignApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundFlexiblestaffingInsuresignApplyResponse, self).__init__()
        self._alipay_id = None
        self._alipay_open_id = None
        self._apply_link = None
        self._status = None

    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def apply_link(self):
        return self._apply_link

    @apply_link.setter
    def apply_link(self, value):
        self._apply_link = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundFlexiblestaffingInsuresignApplyResponse, self).parse_response_content(response_content)
        if 'alipay_id' in response:
            self.alipay_id = response['alipay_id']
        if 'alipay_open_id' in response:
            self.alipay_open_id = response['alipay_open_id']
        if 'apply_link' in response:
            self.apply_link = response['apply_link']
        if 'status' in response:
            self.status = response['status']

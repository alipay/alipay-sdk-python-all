#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundFlexiblestaffingInsuresignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundFlexiblestaffingInsuresignQueryResponse, self).__init__()
        self._alipay_id = None
        self._alipay_open_id = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._out_biz_no = None

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
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundFlexiblestaffingInsuresignQueryResponse, self).parse_response_content(response_content)
        if 'alipay_id' in response:
            self.alipay_id = response['alipay_id']
        if 'alipay_open_id' in response:
            self.alipay_open_id = response['alipay_open_id']
        if 'effect_end_time' in response:
            self.effect_end_time = response['effect_end_time']
        if 'effect_start_time' in response:
            self.effect_start_time = response['effect_start_time']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']

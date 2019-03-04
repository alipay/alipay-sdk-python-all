#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeUserSceneConsultResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeUserSceneConsultResponse, self).__init__()
        self._display_msg = None
        self._open = None
        self._permit = None
        self._refuse_code = None
        self._refuse_msg = None
        self._risk_order_no = None
        self._top_amount = None
        self._top_goods_count = None
        self._zm_score_level = None

    @property
    def display_msg(self):
        return self._display_msg

    @display_msg.setter
    def display_msg(self, value):
        self._display_msg = value
    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value
    @property
    def permit(self):
        return self._permit

    @permit.setter
    def permit(self, value):
        self._permit = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def risk_order_no(self):
        return self._risk_order_no

    @risk_order_no.setter
    def risk_order_no(self, value):
        self._risk_order_no = value
    @property
    def top_amount(self):
        return self._top_amount

    @top_amount.setter
    def top_amount(self, value):
        self._top_amount = value
    @property
    def top_goods_count(self):
        return self._top_goods_count

    @top_goods_count.setter
    def top_goods_count(self, value):
        self._top_goods_count = value
    @property
    def zm_score_level(self):
        return self._zm_score_level

    @zm_score_level.setter
    def zm_score_level(self, value):
        self._zm_score_level = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeUserSceneConsultResponse, self).parse_response_content(response_content)
        if 'display_msg' in response:
            self.display_msg = response['display_msg']
        if 'open' in response:
            self.open = response['open']
        if 'permit' in response:
            self.permit = response['permit']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'risk_order_no' in response:
            self.risk_order_no = response['risk_order_no']
        if 'top_amount' in response:
            self.top_amount = response['top_amount']
        if 'top_goods_count' in response:
            self.top_goods_count = response['top_goods_count']
        if 'zm_score_level' in response:
            self.zm_score_level = response['zm_score_level']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HbmtActivityInfoVO import HbmtActivityInfoVO


class AlipayPcreditHuabeiPcreditbenefitHuabeijinPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiPcreditbenefitHuabeijinPreconsultResponse, self).__init__()
        self._activity_info = None
        self._already_triggered = None
        self._calculated_amount = None
        self._can_participate = None
        self._cap_applied = None
        self._hb_biz_code = None
        self._max_calculated_amount = None
        self._min_calculated_amount = None

    @property
    def activity_info(self):
        return self._activity_info

    @activity_info.setter
    def activity_info(self, value):
        if isinstance(value, HbmtActivityInfoVO):
            self._activity_info = value
        else:
            self._activity_info = HbmtActivityInfoVO.from_alipay_dict(value)
    @property
    def already_triggered(self):
        return self._already_triggered

    @already_triggered.setter
    def already_triggered(self, value):
        self._already_triggered = value
    @property
    def calculated_amount(self):
        return self._calculated_amount

    @calculated_amount.setter
    def calculated_amount(self, value):
        self._calculated_amount = value
    @property
    def can_participate(self):
        return self._can_participate

    @can_participate.setter
    def can_participate(self, value):
        self._can_participate = value
    @property
    def cap_applied(self):
        return self._cap_applied

    @cap_applied.setter
    def cap_applied(self, value):
        self._cap_applied = value
    @property
    def hb_biz_code(self):
        return self._hb_biz_code

    @hb_biz_code.setter
    def hb_biz_code(self, value):
        self._hb_biz_code = value
    @property
    def max_calculated_amount(self):
        return self._max_calculated_amount

    @max_calculated_amount.setter
    def max_calculated_amount(self, value):
        self._max_calculated_amount = value
    @property
    def min_calculated_amount(self):
        return self._min_calculated_amount

    @min_calculated_amount.setter
    def min_calculated_amount(self, value):
        self._min_calculated_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiPcreditbenefitHuabeijinPreconsultResponse, self).parse_response_content(response_content)
        if 'activity_info' in response:
            self.activity_info = response['activity_info']
        if 'already_triggered' in response:
            self.already_triggered = response['already_triggered']
        if 'calculated_amount' in response:
            self.calculated_amount = response['calculated_amount']
        if 'can_participate' in response:
            self.can_participate = response['can_participate']
        if 'cap_applied' in response:
            self.cap_applied = response['cap_applied']
        if 'hb_biz_code' in response:
            self.hb_biz_code = response['hb_biz_code']
        if 'max_calculated_amount' in response:
            self.max_calculated_amount = response['max_calculated_amount']
        if 'min_calculated_amount' in response:
            self.min_calculated_amount = response['min_calculated_amount']

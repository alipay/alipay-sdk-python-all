#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeUserRiskConsultResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeUserRiskConsultResponse, self).__init__()
        self._permit = None
        self._refuse_code = None
        self._risk_order_no = None
        self._scene_level = None
        self._zm_score_level = None

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
    def risk_order_no(self):
        return self._risk_order_no

    @risk_order_no.setter
    def risk_order_no(self, value):
        self._risk_order_no = value
    @property
    def scene_level(self):
        return self._scene_level

    @scene_level.setter
    def scene_level(self, value):
        self._scene_level = value
    @property
    def zm_score_level(self):
        return self._zm_score_level

    @zm_score_level.setter
    def zm_score_level(self, value):
        self._zm_score_level = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeUserRiskConsultResponse, self).parse_response_content(response_content)
        if 'permit' in response:
            self.permit = response['permit']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'risk_order_no' in response:
            self.risk_order_no = response['risk_order_no']
        if 'scene_level' in response:
            self.scene_level = response['scene_level']
        if 'zm_score_level' in response:
            self.zm_score_level = response['zm_score_level']

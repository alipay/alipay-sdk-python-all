#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoPreConsultResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoPreConsultResponse, self).__init__()
        self._admittance = None
        self._alipay_user_id = None

    @property
    def admittance(self):
        return self._admittance

    @admittance.setter
    def admittance(self, value):
        self._admittance = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoPreConsultResponse, self).parse_response_content(response_content)
        if 'admittance' in response:
            self.admittance = response['admittance']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']

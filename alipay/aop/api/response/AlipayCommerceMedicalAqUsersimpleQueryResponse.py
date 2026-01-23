#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAqUsersimpleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAqUsersimpleQueryResponse, self).__init__()
        self._alipay_user_id = None
        self._aq_user_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def aq_user_id(self):
        return self._aq_user_id

    @aq_user_id.setter
    def aq_user_id(self, value):
        self._aq_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAqUsersimpleQueryResponse, self).parse_response_content(response_content)
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'aq_user_id' in response:
            self.aq_user_id = response['aq_user_id']

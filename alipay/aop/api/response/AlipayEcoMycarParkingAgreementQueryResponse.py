#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserAdvanceInfo import UserAdvanceInfo


class AlipayEcoMycarParkingAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingAgreementQueryResponse, self).__init__()
        self._agreement_status = None
        self._user_advance_info = None

    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
    @property
    def user_advance_info(self):
        return self._user_advance_info

    @user_advance_info.setter
    def user_advance_info(self, value):
        if isinstance(value, UserAdvanceInfo):
            self._user_advance_info = value
        else:
            self._user_advance_info = UserAdvanceInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingAgreementQueryResponse, self).parse_response_content(response_content)
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
        if 'user_advance_info' in response:
            self.user_advance_info = response['user_advance_info']

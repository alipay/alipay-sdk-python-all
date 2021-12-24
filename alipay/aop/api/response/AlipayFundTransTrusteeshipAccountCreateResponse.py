#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtCardInfo import ExtCardInfo


class AlipayFundTransTrusteeshipAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransTrusteeshipAccountCreateResponse, self).__init__()
        self._alipay_account_no = None
        self._alipay_user_id = None
        self._ext_card_info = None

    @property
    def alipay_account_no(self):
        return self._alipay_account_no

    @alipay_account_no.setter
    def alipay_account_no(self, value):
        self._alipay_account_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def ext_card_info(self):
        return self._ext_card_info

    @ext_card_info.setter
    def ext_card_info(self, value):
        if isinstance(value, ExtCardInfo):
            self._ext_card_info = value
        else:
            self._ext_card_info = ExtCardInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransTrusteeshipAccountCreateResponse, self).parse_response_content(response_content)
        if 'alipay_account_no' in response:
            self.alipay_account_no = response['alipay_account_no']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'ext_card_info' in response:
            self.ext_card_info = response['ext_card_info']

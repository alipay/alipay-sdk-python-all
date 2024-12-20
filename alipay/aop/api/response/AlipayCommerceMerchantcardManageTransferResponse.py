#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FailCardReason import FailCardReason


class AlipayCommerceMerchantcardManageTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardManageTransferResponse, self).__init__()
        self._card_template_ids = None
        self._confirm_link = None
        self._fail_card_reasons = None

    @property
    def card_template_ids(self):
        return self._card_template_ids

    @card_template_ids.setter
    def card_template_ids(self, value):
        if isinstance(value, list):
            self._card_template_ids = list()
            for i in value:
                self._card_template_ids.append(i)
    @property
    def confirm_link(self):
        return self._confirm_link

    @confirm_link.setter
    def confirm_link(self, value):
        self._confirm_link = value
    @property
    def fail_card_reasons(self):
        return self._fail_card_reasons

    @fail_card_reasons.setter
    def fail_card_reasons(self, value):
        if isinstance(value, list):
            self._fail_card_reasons = list()
            for i in value:
                if isinstance(i, FailCardReason):
                    self._fail_card_reasons.append(i)
                else:
                    self._fail_card_reasons.append(FailCardReason.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardManageTransferResponse, self).parse_response_content(response_content)
        if 'card_template_ids' in response:
            self.card_template_ids = response['card_template_ids']
        if 'confirm_link' in response:
            self.confirm_link = response['confirm_link']
        if 'fail_card_reasons' in response:
            self.fail_card_reasons = response['fail_card_reasons']

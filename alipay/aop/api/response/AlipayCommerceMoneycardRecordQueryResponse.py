#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MoneyCardUseRecordDetail import MoneyCardUseRecordDetail


class AlipayCommerceMoneycardRecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMoneycardRecordQueryResponse, self).__init__()
        self._money_card_use_record_detail = None

    @property
    def money_card_use_record_detail(self):
        return self._money_card_use_record_detail

    @money_card_use_record_detail.setter
    def money_card_use_record_detail(self, value):
        if isinstance(value, MoneyCardUseRecordDetail):
            self._money_card_use_record_detail = value
        else:
            self._money_card_use_record_detail = MoneyCardUseRecordDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMoneycardRecordQueryResponse, self).parse_response_content(response_content)
        if 'money_card_use_record_detail' in response:
            self.money_card_use_record_detail = response['money_card_use_record_detail']

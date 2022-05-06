#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TimeCardConsumeCardInfo import TimeCardConsumeCardInfo
from alipay.aop.api.domain.TimeCardConsumerRecordInfo import TimeCardConsumerRecordInfo


class AlipayCommerceOperationTimescardConsumelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTimescardConsumelistQueryResponse, self).__init__()
        self._card_info = None
        self._consume_record = None

    @property
    def card_info(self):
        return self._card_info

    @card_info.setter
    def card_info(self, value):
        if isinstance(value, TimeCardConsumeCardInfo):
            self._card_info = value
        else:
            self._card_info = TimeCardConsumeCardInfo.from_alipay_dict(value)
    @property
    def consume_record(self):
        return self._consume_record

    @consume_record.setter
    def consume_record(self, value):
        if isinstance(value, list):
            self._consume_record = list()
            for i in value:
                if isinstance(i, TimeCardConsumerRecordInfo):
                    self._consume_record.append(i)
                else:
                    self._consume_record.append(TimeCardConsumerRecordInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationTimescardConsumelistQueryResponse, self).parse_response_content(response_content)
        if 'card_info' in response:
            self.card_info = response['card_info']
        if 'consume_record' in response:
            self.consume_record = response['consume_record']

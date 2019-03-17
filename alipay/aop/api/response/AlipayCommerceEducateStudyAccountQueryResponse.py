#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StudyAccountInfo import StudyAccountInfo


class AlipayCommerceEducateStudyAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateStudyAccountQueryResponse, self).__init__()
        self._alipay_card_list = None

    @property
    def alipay_card_list(self):
        return self._alipay_card_list

    @alipay_card_list.setter
    def alipay_card_list(self, value):
        if isinstance(value, StudyAccountInfo):
            self._alipay_card_list = value
        else:
            self._alipay_card_list = StudyAccountInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateStudyAccountQueryResponse, self).parse_response_content(response_content)
        if 'alipay_card_list' in response:
            self.alipay_card_list = response['alipay_card_list']

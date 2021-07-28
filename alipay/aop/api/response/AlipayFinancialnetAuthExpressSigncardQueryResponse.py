#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SignCardInfo import SignCardInfo


class AlipayFinancialnetAuthExpressSigncardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthExpressSigncardQueryResponse, self).__init__()
        self._sign_card_infos = None

    @property
    def sign_card_infos(self):
        return self._sign_card_infos

    @sign_card_infos.setter
    def sign_card_infos(self, value):
        if isinstance(value, list):
            self._sign_card_infos = list()
            for i in value:
                if isinstance(i, SignCardInfo):
                    self._sign_card_infos.append(i)
                else:
                    self._sign_card_infos.append(SignCardInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthExpressSigncardQueryResponse, self).parse_response_content(response_content)
        if 'sign_card_infos' in response:
            self.sign_card_infos = response['sign_card_infos']

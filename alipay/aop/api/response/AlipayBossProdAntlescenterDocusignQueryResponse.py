#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecipientSignStatusResult import RecipientSignStatusResult


class AlipayBossProdAntlescenterDocusignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlescenterDocusignQueryResponse, self).__init__()
        self._recipient_sign_status_result_list = None

    @property
    def recipient_sign_status_result_list(self):
        return self._recipient_sign_status_result_list

    @recipient_sign_status_result_list.setter
    def recipient_sign_status_result_list(self, value):
        if isinstance(value, list):
            self._recipient_sign_status_result_list = list()
            for i in value:
                if isinstance(i, RecipientSignStatusResult):
                    self._recipient_sign_status_result_list.append(i)
                else:
                    self._recipient_sign_status_result_list.append(RecipientSignStatusResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlescenterDocusignQueryResponse, self).parse_response_content(response_content)
        if 'recipient_sign_status_result_list' in response:
            self.recipient_sign_status_result_list = response['recipient_sign_status_result_list']

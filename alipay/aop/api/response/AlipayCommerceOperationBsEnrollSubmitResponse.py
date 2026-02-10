#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BsEnrollParticipant import BsEnrollParticipant
from alipay.aop.api.domain.BsEnrollParticipantResult import BsEnrollParticipantResult


class AlipayCommerceOperationBsEnrollSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationBsEnrollSubmitResponse, self).__init__()
        self._failed_participants = None
        self._participants_result = None

    @property
    def failed_participants(self):
        return self._failed_participants

    @failed_participants.setter
    def failed_participants(self, value):
        if isinstance(value, list):
            self._failed_participants = list()
            for i in value:
                if isinstance(i, BsEnrollParticipant):
                    self._failed_participants.append(i)
                else:
                    self._failed_participants.append(BsEnrollParticipant.from_alipay_dict(i))
    @property
    def participants_result(self):
        return self._participants_result

    @participants_result.setter
    def participants_result(self, value):
        if isinstance(value, list):
            self._participants_result = list()
            for i in value:
                if isinstance(i, BsEnrollParticipantResult):
                    self._participants_result.append(i)
                else:
                    self._participants_result.append(BsEnrollParticipantResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationBsEnrollSubmitResponse, self).parse_response_content(response_content)
        if 'failed_participants' in response:
            self.failed_participants = response['failed_participants']
        if 'participants_result' in response:
            self.participants_result = response['participants_result']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BsParticipantResponseDTO import BsParticipantResponseDTO


class AlipayCommerceOperationBsEnrollsRecoverResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationBsEnrollsRecoverResponse, self).__init__()
        self._failed_participants = None

    @property
    def failed_participants(self):
        return self._failed_participants

    @failed_participants.setter
    def failed_participants(self, value):
        if isinstance(value, list):
            self._failed_participants = list()
            for i in value:
                if isinstance(i, BsParticipantResponseDTO):
                    self._failed_participants.append(i)
                else:
                    self._failed_participants.append(BsParticipantResponseDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationBsEnrollsRecoverResponse, self).parse_response_content(response_content)
        if 'failed_participants' in response:
            self.failed_participants = response['failed_participants']

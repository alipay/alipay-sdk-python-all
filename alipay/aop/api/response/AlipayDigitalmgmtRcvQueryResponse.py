#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RcvDto import RcvDto


class AlipayDigitalmgmtRcvQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtRcvQueryResponse, self).__init__()
        self._rcv_dto = None

    @property
    def rcv_dto(self):
        return self._rcv_dto

    @rcv_dto.setter
    def rcv_dto(self, value):
        if isinstance(value, RcvDto):
            self._rcv_dto = value
        else:
            self._rcv_dto = RcvDto.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtRcvQueryResponse, self).parse_response_content(response_content)
        if 'rcv_dto' in response:
            self.rcv_dto = response['rcv_dto']

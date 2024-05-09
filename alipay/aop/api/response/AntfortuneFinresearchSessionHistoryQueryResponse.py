#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FinSessionDetail import FinSessionDetail


class AntfortuneFinresearchSessionHistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneFinresearchSessionHistoryQueryResponse, self).__init__()
        self._session_list = None

    @property
    def session_list(self):
        return self._session_list

    @session_list.setter
    def session_list(self, value):
        if isinstance(value, FinSessionDetail):
            self._session_list = value
        else:
            self._session_list = FinSessionDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntfortuneFinresearchSessionHistoryQueryResponse, self).parse_response_content(response_content)
        if 'session_list' in response:
            self.session_list = response['session_list']

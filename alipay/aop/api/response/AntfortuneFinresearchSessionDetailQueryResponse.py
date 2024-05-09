#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FinMessageDetail import FinMessageDetail
from alipay.aop.api.domain.FinSessionDetail import FinSessionDetail


class AntfortuneFinresearchSessionDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneFinresearchSessionDetailQueryResponse, self).__init__()
        self._message_list = None
        self._session_detail = None

    @property
    def message_list(self):
        return self._message_list

    @message_list.setter
    def message_list(self, value):
        if isinstance(value, FinMessageDetail):
            self._message_list = value
        else:
            self._message_list = FinMessageDetail.from_alipay_dict(value)
    @property
    def session_detail(self):
        return self._session_detail

    @session_detail.setter
    def session_detail(self, value):
        if isinstance(value, FinSessionDetail):
            self._session_detail = value
        else:
            self._session_detail = FinSessionDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntfortuneFinresearchSessionDetailQueryResponse, self).parse_response_content(response_content)
        if 'message_list' in response:
            self.message_list = response['message_list']
        if 'session_detail' in response:
            self.session_detail = response['session_detail']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZXZSessionDetail import ZXZSessionDetail


class AntfortuneFinresearchSessionListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneFinresearchSessionListQueryResponse, self).__init__()
        self._session_list = None

    @property
    def session_list(self):
        return self._session_list

    @session_list.setter
    def session_list(self, value):
        if isinstance(value, list):
            self._session_list = list()
            for i in value:
                if isinstance(i, ZXZSessionDetail):
                    self._session_list.append(i)
                else:
                    self._session_list.append(ZXZSessionDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntfortuneFinresearchSessionListQueryResponse, self).parse_response_content(response_content)
        if 'session_list' in response:
            self.session_list = response['session_list']

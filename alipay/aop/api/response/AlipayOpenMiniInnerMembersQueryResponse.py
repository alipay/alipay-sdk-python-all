#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenAppOperatorVo import OpenAppOperatorVo


class AlipayOpenMiniInnerMembersQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerMembersQueryResponse, self).__init__()
        self._open_app_operator_vo = None

    @property
    def open_app_operator_vo(self):
        return self._open_app_operator_vo

    @open_app_operator_vo.setter
    def open_app_operator_vo(self, value):
        if isinstance(value, list):
            self._open_app_operator_vo = list()
            for i in value:
                if isinstance(i, OpenAppOperatorVo):
                    self._open_app_operator_vo.append(i)
                else:
                    self._open_app_operator_vo.append(OpenAppOperatorVo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerMembersQueryResponse, self).parse_response_content(response_content)
        if 'open_app_operator_vo' in response:
            self.open_app_operator_vo = response['open_app_operator_vo']

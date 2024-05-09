#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DelOauthDetail import DelOauthDetail
from alipay.aop.api.domain.DelOauthDetailResult import DelOauthDetailResult


class AlipayUserDeloauthDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDeloauthDetailQueryResponse, self).__init__()
        self._details = None
        self._response = None

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                if isinstance(i, DelOauthDetail):
                    self._details.append(i)
                else:
                    self._details.append(DelOauthDetail.from_alipay_dict(i))
    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        if isinstance(value, DelOauthDetailResult):
            self._response = value
        else:
            self._response = DelOauthDetailResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserDeloauthDetailQueryResponse, self).parse_response_content(response_content)
        if 'details' in response:
            self.details = response['details']
        if 'response' in response:
            self.response = response['response']

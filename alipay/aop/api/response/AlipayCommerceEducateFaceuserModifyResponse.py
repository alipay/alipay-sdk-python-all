#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FailFaceUserInfo import FailFaceUserInfo


class AlipayCommerceEducateFaceuserModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateFaceuserModifyResponse, self).__init__()
        self._fail_user_list = None

    @property
    def fail_user_list(self):
        return self._fail_user_list

    @fail_user_list.setter
    def fail_user_list(self, value):
        if isinstance(value, list):
            self._fail_user_list = list()
            for i in value:
                if isinstance(i, FailFaceUserInfo):
                    self._fail_user_list.append(i)
                else:
                    self._fail_user_list.append(FailFaceUserInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateFaceuserModifyResponse, self).parse_response_content(response_content)
        if 'fail_user_list' in response:
            self.fail_user_list = response['fail_user_list']

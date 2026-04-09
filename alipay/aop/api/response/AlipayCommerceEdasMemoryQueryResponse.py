#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserLabels import UserLabels


class AlipayCommerceEdasMemoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEdasMemoryQueryResponse, self).__init__()
        self._user_labels = None

    @property
    def user_labels(self):
        return self._user_labels

    @user_labels.setter
    def user_labels(self, value):
        if isinstance(value, list):
            self._user_labels = list()
            for i in value:
                if isinstance(i, UserLabels):
                    self._user_labels.append(i)
                else:
                    self._user_labels.append(UserLabels.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEdasMemoryQueryResponse, self).parse_response_content(response_content)
        if 'user_labels' in response:
            self.user_labels = response['user_labels']

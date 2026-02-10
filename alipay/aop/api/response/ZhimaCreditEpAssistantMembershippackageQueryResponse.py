#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpAssistantMembershippackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAssistantMembershippackageQueryResponse, self).__init__()
        self._licenses = None
        self._unlock_right_num = None

    @property
    def licenses(self):
        return self._licenses

    @licenses.setter
    def licenses(self, value):
        if isinstance(value, list):
            self._licenses = list()
            for i in value:
                self._licenses.append(i)
    @property
    def unlock_right_num(self):
        return self._unlock_right_num

    @unlock_right_num.setter
    def unlock_right_num(self, value):
        self._unlock_right_num = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAssistantMembershippackageQueryResponse, self).parse_response_content(response_content)
        if 'licenses' in response:
            self.licenses = response['licenses']
        if 'unlock_right_num' in response:
            self.unlock_right_num = response['unlock_right_num']

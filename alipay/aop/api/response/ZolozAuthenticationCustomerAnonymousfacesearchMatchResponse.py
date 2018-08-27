#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FaceSearchAnonymousUserInfo import FaceSearchAnonymousUserInfo


class ZolozAuthenticationCustomerAnonymousfacesearchMatchResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationCustomerAnonymousfacesearchMatchResponse, self).__init__()
        self._userinfolist = None

    @property
    def userinfolist(self):
        return self._userinfolist

    @userinfolist.setter
    def userinfolist(self, value):
        if isinstance(value, list):
            self._userinfolist = list()
            for i in value:
                if isinstance(i, FaceSearchAnonymousUserInfo):
                    self._userinfolist.append(i)
                else:
                    self._userinfolist.append(FaceSearchAnonymousUserInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZolozAuthenticationCustomerAnonymousfacesearchMatchResponse, self).parse_response_content(response_content)
        if 'userinfolist' in response:
            self.userinfolist = response['userinfolist']

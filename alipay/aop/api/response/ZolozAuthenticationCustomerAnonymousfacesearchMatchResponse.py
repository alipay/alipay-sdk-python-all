#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FaceSearchUserInfo import FaceSearchUserInfo
from alipay.aop.api.domain.FaceSearchUserInfo import FaceSearchUserInfo
from alipay.aop.api.domain.FaceSearchAnonymousUserInfo import FaceSearchAnonymousUserInfo


class ZolozAuthenticationCustomerAnonymousfacesearchMatchResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationCustomerAnonymousfacesearchMatchResponse, self).__init__()
        self._candidatelist = None
        self._foundface = None
        self._retcodesub = None
        self._retmessagesub = None
        self._userinfolist = None

    @property
    def candidatelist(self):
        return self._candidatelist

    @candidatelist.setter
    def candidatelist(self, value):
        if isinstance(value, list):
            self._candidatelist = list()
            for i in value:
                if isinstance(i, FaceSearchUserInfo):
                    self._candidatelist.append(i)
                else:
                    self._candidatelist.append(FaceSearchUserInfo.from_alipay_dict(i))
    @property
    def foundface(self):
        return self._foundface

    @foundface.setter
    def foundface(self, value):
        if isinstance(value, FaceSearchUserInfo):
            self._foundface = value
        else:
            self._foundface = FaceSearchUserInfo.from_alipay_dict(value)
    @property
    def retcodesub(self):
        return self._retcodesub

    @retcodesub.setter
    def retcodesub(self, value):
        self._retcodesub = value
    @property
    def retmessagesub(self):
        return self._retmessagesub

    @retmessagesub.setter
    def retmessagesub(self, value):
        self._retmessagesub = value
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
        if 'candidatelist' in response:
            self.candidatelist = response['candidatelist']
        if 'foundface' in response:
            self.foundface = response['foundface']
        if 'retcodesub' in response:
            self.retcodesub = response['retcodesub']
        if 'retmessagesub' in response:
            self.retmessagesub = response['retmessagesub']
        if 'userinfolist' in response:
            self.userinfolist = response['userinfolist']

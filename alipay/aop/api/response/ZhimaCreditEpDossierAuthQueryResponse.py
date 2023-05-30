#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpAuthContent import EpAuthContent


class ZhimaCreditEpDossierAuthQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDossierAuthQueryResponse, self).__init__()
        self._ep_auth_content = None

    @property
    def ep_auth_content(self):
        return self._ep_auth_content

    @ep_auth_content.setter
    def ep_auth_content(self, value):
        if isinstance(value, list):
            self._ep_auth_content = list()
            for i in value:
                if isinstance(i, EpAuthContent):
                    self._ep_auth_content.append(i)
                else:
                    self._ep_auth_content.append(EpAuthContent.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDossierAuthQueryResponse, self).parse_response_content(response_content)
        if 'ep_auth_content' in response:
            self.ep_auth_content = response['ep_auth_content']

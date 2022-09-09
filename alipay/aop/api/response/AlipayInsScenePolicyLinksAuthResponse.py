#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsPolicyLinkDTO import InsPolicyLinkDTO


class AlipayInsScenePolicyLinksAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePolicyLinksAuthResponse, self).__init__()
        self._policy_links = None

    @property
    def policy_links(self):
        return self._policy_links

    @policy_links.setter
    def policy_links(self, value):
        if isinstance(value, list):
            self._policy_links = list()
            for i in value:
                if isinstance(i, InsPolicyLinkDTO):
                    self._policy_links.append(i)
                else:
                    self._policy_links.append(InsPolicyLinkDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePolicyLinksAuthResponse, self).parse_response_content(response_content)
        if 'policy_links' in response:
            self.policy_links = response['policy_links']

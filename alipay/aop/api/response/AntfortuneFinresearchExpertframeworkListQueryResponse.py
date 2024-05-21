#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZXZExpertFrameworkList import ZXZExpertFrameworkList


class AntfortuneFinresearchExpertframeworkListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneFinresearchExpertframeworkListQueryResponse, self).__init__()
        self._expert_frameworks = None

    @property
    def expert_frameworks(self):
        return self._expert_frameworks

    @expert_frameworks.setter
    def expert_frameworks(self, value):
        if isinstance(value, ZXZExpertFrameworkList):
            self._expert_frameworks = value
        else:
            self._expert_frameworks = ZXZExpertFrameworkList.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntfortuneFinresearchExpertframeworkListQueryResponse, self).parse_response_content(response_content)
        if 'expert_frameworks' in response:
            self.expert_frameworks = response['expert_frameworks']

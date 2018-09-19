#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoxCrowdMatchModel import PromoxCrowdMatchModel


class AlipayDataDataserviceAntlbsCrowdMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAntlbsCrowdMatchResponse, self).__init__()
        self._match_result = None

    @property
    def match_result(self):
        return self._match_result

    @match_result.setter
    def match_result(self, value):
        if isinstance(value, list):
            self._match_result = list()
            for i in value:
                if isinstance(i, PromoxCrowdMatchModel):
                    self._match_result.append(i)
                else:
                    self._match_result.append(PromoxCrowdMatchModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAntlbsCrowdMatchResponse, self).parse_response_content(response_content)
        if 'match_result' in response:
            self.match_result = response['match_result']

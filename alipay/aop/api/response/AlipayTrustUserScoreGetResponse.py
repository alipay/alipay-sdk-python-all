#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AliTrustScore import AliTrustScore


class AlipayTrustUserScoreGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTrustUserScoreGetResponse, self).__init__()
        self._ali_trust_score = None

    @property
    def ali_trust_score(self):
        return self._ali_trust_score

    @ali_trust_score.setter
    def ali_trust_score(self, value):
        if isinstance(value, AliTrustScore):
            self._ali_trust_score = value
        else:
            self._ali_trust_score = AliTrustScore.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayTrustUserScoreGetResponse, self).parse_response_content(response_content)
        if 'ali_trust_score' in response:
            self.ali_trust_score = response['ali_trust_score']

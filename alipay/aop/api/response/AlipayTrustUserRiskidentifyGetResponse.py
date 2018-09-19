#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AliTrustRiskIdentify import AliTrustRiskIdentify


class AlipayTrustUserRiskidentifyGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTrustUserRiskidentifyGetResponse, self).__init__()
        self._ali_trust_risk_identify = None

    @property
    def ali_trust_risk_identify(self):
        return self._ali_trust_risk_identify

    @ali_trust_risk_identify.setter
    def ali_trust_risk_identify(self, value):
        if isinstance(value, AliTrustRiskIdentify):
            self._ali_trust_risk_identify = value
        else:
            self._ali_trust_risk_identify = AliTrustRiskIdentify.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayTrustUserRiskidentifyGetResponse, self).parse_response_content(response_content)
        if 'ali_trust_risk_identify' in response:
            self.ali_trust_risk_identify = response['ali_trust_risk_identify']

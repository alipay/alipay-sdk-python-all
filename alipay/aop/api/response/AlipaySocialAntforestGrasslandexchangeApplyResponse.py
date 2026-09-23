#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GrasslandCert import GrasslandCert


class AlipaySocialAntforestGrasslandexchangeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestGrasslandexchangeApplyResponse, self).__init__()
        self._idempotent = None
        self._user_grassland_certificate = None

    @property
    def idempotent(self):
        return self._idempotent

    @idempotent.setter
    def idempotent(self, value):
        self._idempotent = value
    @property
    def user_grassland_certificate(self):
        return self._user_grassland_certificate

    @user_grassland_certificate.setter
    def user_grassland_certificate(self, value):
        if isinstance(value, GrasslandCert):
            self._user_grassland_certificate = value
        else:
            self._user_grassland_certificate = GrasslandCert.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestGrasslandexchangeApplyResponse, self).parse_response_content(response_content)
        if 'idempotent' in response:
            self.idempotent = response['idempotent']
        if 'user_grassland_certificate' in response:
            self.user_grassland_certificate = response['user_grassland_certificate']

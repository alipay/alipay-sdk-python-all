#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserPeerpayprodAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserPeerpayprodAgreementSignResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserPeerpayprodAgreementSignResponse, self).parse_response_content(response_content)

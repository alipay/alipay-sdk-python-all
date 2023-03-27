#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceTruspleLoanscenedatapushSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTruspleLoanscenedatapushSubmitResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTruspleLoanscenedatapushSubmitResponse, self).parse_response_content(response_content)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEduJzApplyresultSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEduJzApplyresultSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoEduJzApplyresultSyncResponse, self).parse_response_content(response_content)

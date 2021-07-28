#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiEnterpriseReimburseSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiEnterpriseReimburseSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiEnterpriseReimburseSyncResponse, self).parse_response_content(response_content)

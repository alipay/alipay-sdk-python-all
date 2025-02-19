#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantQipanGreyblackcrowduserAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanGreyblackcrowduserAddResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanGreyblackcrowduserAddResponse, self).parse_response_content(response_content)

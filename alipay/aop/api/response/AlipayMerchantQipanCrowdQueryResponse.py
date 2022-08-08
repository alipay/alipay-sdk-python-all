#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QipanMerchantCrowd import QipanMerchantCrowd


class AlipayMerchantQipanCrowdQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanCrowdQueryResponse, self).__init__()
        self._crowd_info = None

    @property
    def crowd_info(self):
        return self._crowd_info

    @crowd_info.setter
    def crowd_info(self, value):
        if isinstance(value, QipanMerchantCrowd):
            self._crowd_info = value
        else:
            self._crowd_info = QipanMerchantCrowd.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanCrowdQueryResponse, self).parse_response_content(response_content)
        if 'crowd_info' in response:
            self.crowd_info = response['crowd_info']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsSellerActivity import InsSellerActivity


class AlipayInsSceneSellerActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneSellerActivityQueryResponse, self).__init__()
        self._ins_seller_activity = None

    @property
    def ins_seller_activity(self):
        return self._ins_seller_activity

    @ins_seller_activity.setter
    def ins_seller_activity(self, value):
        if isinstance(value, InsSellerActivity):
            self._ins_seller_activity = value
        else:
            self._ins_seller_activity = InsSellerActivity.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneSellerActivityQueryResponse, self).parse_response_content(response_content)
        if 'ins_seller_activity' in response:
            self.ins_seller_activity = response['ins_seller_activity']

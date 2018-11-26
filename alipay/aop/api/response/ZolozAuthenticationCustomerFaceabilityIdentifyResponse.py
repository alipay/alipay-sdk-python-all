#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FaceAbilityExtInfo import FaceAbilityExtInfo


class ZolozAuthenticationCustomerFaceabilityIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationCustomerFaceabilityIdentifyResponse, self).__init__()
        self._biz_info = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        if isinstance(value, FaceAbilityExtInfo):
            self._biz_info = value
        else:
            self._biz_info = FaceAbilityExtInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZolozAuthenticationCustomerFaceabilityIdentifyResponse, self).parse_response_content(response_content)
        if 'biz_info' in response:
            self.biz_info = response['biz_info']

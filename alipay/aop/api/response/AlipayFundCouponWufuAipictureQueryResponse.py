#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AiPictureVO import AiPictureVO


class AlipayFundCouponWufuAipictureQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponWufuAipictureQueryResponse, self).__init__()
        self._ai_picture_list = None

    @property
    def ai_picture_list(self):
        return self._ai_picture_list

    @ai_picture_list.setter
    def ai_picture_list(self, value):
        if isinstance(value, list):
            self._ai_picture_list = list()
            for i in value:
                if isinstance(i, AiPictureVO):
                    self._ai_picture_list.append(i)
                else:
                    self._ai_picture_list.append(AiPictureVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponWufuAipictureQueryResponse, self).parse_response_content(response_content)
        if 'ai_picture_list' in response:
            self.ai_picture_list = response['ai_picture_list']

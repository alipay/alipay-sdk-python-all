#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RetailPointPrizeInfoDTO import RetailPointPrizeInfoDTO


class AlipayCommerceRetailActivityConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailActivityConsultResponse, self).__init__()
        self._point_prize_info = None

    @property
    def point_prize_info(self):
        return self._point_prize_info

    @point_prize_info.setter
    def point_prize_info(self, value):
        if isinstance(value, list):
            self._point_prize_info = list()
            for i in value:
                if isinstance(i, RetailPointPrizeInfoDTO):
                    self._point_prize_info.append(i)
                else:
                    self._point_prize_info.append(RetailPointPrizeInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailActivityConsultResponse, self).parse_response_content(response_content)
        if 'point_prize_info' in response:
            self.point_prize_info = response['point_prize_info']

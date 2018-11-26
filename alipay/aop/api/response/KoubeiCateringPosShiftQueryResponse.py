#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopPosSchedule import ShopPosSchedule


class KoubeiCateringPosShiftQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosShiftQueryResponse, self).__init__()
        self._shop_pos_schedules = None

    @property
    def shop_pos_schedules(self):
        return self._shop_pos_schedules

    @shop_pos_schedules.setter
    def shop_pos_schedules(self, value):
        if isinstance(value, list):
            self._shop_pos_schedules = list()
            for i in value:
                if isinstance(i, ShopPosSchedule):
                    self._shop_pos_schedules.append(i)
                else:
                    self._shop_pos_schedules.append(ShopPosSchedule.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosShiftQueryResponse, self).parse_response_content(response_content)
        if 'shop_pos_schedules' in response:
            self.shop_pos_schedules = response['shop_pos_schedules']

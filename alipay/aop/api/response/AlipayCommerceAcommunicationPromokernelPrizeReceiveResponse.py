#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CampOrderInfo import CampOrderInfo
from alipay.aop.api.domain.PrizeSendOrderDetailRes import PrizeSendOrderDetailRes


class AlipayCommerceAcommunicationPromokernelPrizeReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationPromokernelPrizeReceiveResponse, self).__init__()
        self._camp_order_info = None
        self._prize_send_order_detail_list = None

    @property
    def camp_order_info(self):
        return self._camp_order_info

    @camp_order_info.setter
    def camp_order_info(self, value):
        if isinstance(value, CampOrderInfo):
            self._camp_order_info = value
        else:
            self._camp_order_info = CampOrderInfo.from_alipay_dict(value)
    @property
    def prize_send_order_detail_list(self):
        return self._prize_send_order_detail_list

    @prize_send_order_detail_list.setter
    def prize_send_order_detail_list(self, value):
        if isinstance(value, list):
            self._prize_send_order_detail_list = list()
            for i in value:
                if isinstance(i, PrizeSendOrderDetailRes):
                    self._prize_send_order_detail_list.append(i)
                else:
                    self._prize_send_order_detail_list.append(PrizeSendOrderDetailRes.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationPromokernelPrizeReceiveResponse, self).parse_response_content(response_content)
        if 'camp_order_info' in response:
            self.camp_order_info = response['camp_order_info']
        if 'prize_send_order_detail_list' in response:
            self.prize_send_order_detail_list = response['prize_send_order_detail_list']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KnPrizeInfo import KnPrizeInfo


class AlipayMarketingCampaignDrawcampConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignDrawcampConsultResponse, self).__init__()
        self._camp_id = None
        self._error_code = None
        self._error_msg = None
        self._valid_prize_infos = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def valid_prize_infos(self):
        return self._valid_prize_infos

    @valid_prize_infos.setter
    def valid_prize_infos(self, value):
        if isinstance(value, list):
            self._valid_prize_infos = list()
            for i in value:
                if isinstance(i, KnPrizeInfo):
                    self._valid_prize_infos.append(i)
                else:
                    self._valid_prize_infos.append(KnPrizeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignDrawcampConsultResponse, self).parse_response_content(response_content)
        if 'camp_id' in response:
            self.camp_id = response['camp_id']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'valid_prize_infos' in response:
            self.valid_prize_infos = response['valid_prize_infos']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoyagerCampaignInfo import VoyagerCampaignInfo
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayVoyagerMarketingCampaignqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerMarketingCampaignqueryResponse, self).__init__()
        self._campaign_infos = None
        self._feedback_city_code = None
        self._feedback_ext_info_list = None
        self._result = None

    @property
    def campaign_infos(self):
        return self._campaign_infos

    @campaign_infos.setter
    def campaign_infos(self, value):
        if isinstance(value, list):
            self._campaign_infos = list()
            for i in value:
                if isinstance(i, VoyagerCampaignInfo):
                    self._campaign_infos.append(i)
                else:
                    self._campaign_infos.append(VoyagerCampaignInfo.from_alipay_dict(i))
    @property
    def feedback_city_code(self):
        return self._feedback_city_code

    @feedback_city_code.setter
    def feedback_city_code(self, value):
        self._feedback_city_code = value
    @property
    def feedback_ext_info_list(self):
        return self._feedback_ext_info_list

    @feedback_ext_info_list.setter
    def feedback_ext_info_list(self, value):
        if isinstance(value, list):
            self._feedback_ext_info_list = list()
            for i in value:
                self._feedback_ext_info_list.append(i)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ResultInfoDTO):
            self._result = value
        else:
            self._result = ResultInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayVoyagerMarketingCampaignqueryResponse, self).parse_response_content(response_content)
        if 'campaign_infos' in response:
            self.campaign_infos = response['campaign_infos']
        if 'feedback_city_code' in response:
            self.feedback_city_code = response['feedback_city_code']
        if 'feedback_ext_info_list' in response:
            self.feedback_ext_info_list = response['feedback_ext_info_list']
        if 'result' in response:
            self.result = response['result']

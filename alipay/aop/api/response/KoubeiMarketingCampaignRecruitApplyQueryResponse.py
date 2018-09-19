#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecruitItemApplyData import RecruitItemApplyData


class KoubeiMarketingCampaignRecruitApplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignRecruitApplyQueryResponse, self).__init__()
        self._bought_time = None
        self._end_time = None
        self._item_count = None
        self._item_info = None
        self._name = None
        self._prehot_time = None

    @property
    def bought_time(self):
        return self._bought_time

    @bought_time.setter
    def bought_time(self, value):
        self._bought_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def item_count(self):
        return self._item_count

    @item_count.setter
    def item_count(self, value):
        self._item_count = value
    @property
    def item_info(self):
        return self._item_info

    @item_info.setter
    def item_info(self, value):
        if isinstance(value, list):
            self._item_info = list()
            for i in value:
                if isinstance(i, RecruitItemApplyData):
                    self._item_info.append(i)
                else:
                    self._item_info.append(RecruitItemApplyData.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def prehot_time(self):
        return self._prehot_time

    @prehot_time.setter
    def prehot_time(self, value):
        self._prehot_time = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignRecruitApplyQueryResponse, self).parse_response_content(response_content)
        if 'bought_time' in response:
            self.bought_time = response['bought_time']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'item_count' in response:
            self.item_count = response['item_count']
        if 'item_info' in response:
            self.item_info = response['item_info']
        if 'name' in response:
            self.name = response['name']
        if 'prehot_time' in response:
            self.prehot_time = response['prehot_time']

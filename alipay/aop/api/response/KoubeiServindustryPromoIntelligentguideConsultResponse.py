#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecommendCard import RecommendCard
from alipay.aop.api.domain.RecommendServiceInfo import RecommendServiceInfo


class KoubeiServindustryPromoIntelligentguideConsultResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryPromoIntelligentguideConsultResponse, self).__init__()
        self._consume_max = None
        self._consume_min = None
        self._recommend_card = None
        self._recommend_service_info = None
        self._user_tags = None

    @property
    def consume_max(self):
        return self._consume_max

    @consume_max.setter
    def consume_max(self, value):
        self._consume_max = value
    @property
    def consume_min(self):
        return self._consume_min

    @consume_min.setter
    def consume_min(self, value):
        self._consume_min = value
    @property
    def recommend_card(self):
        return self._recommend_card

    @recommend_card.setter
    def recommend_card(self, value):
        if isinstance(value, RecommendCard):
            self._recommend_card = value
        else:
            self._recommend_card = RecommendCard.from_alipay_dict(value)
    @property
    def recommend_service_info(self):
        return self._recommend_service_info

    @recommend_service_info.setter
    def recommend_service_info(self, value):
        if isinstance(value, list):
            self._recommend_service_info = list()
            for i in value:
                if isinstance(i, RecommendServiceInfo):
                    self._recommend_service_info.append(i)
                else:
                    self._recommend_service_info.append(RecommendServiceInfo.from_alipay_dict(i))
    @property
    def user_tags(self):
        return self._user_tags

    @user_tags.setter
    def user_tags(self, value):
        self._user_tags = value

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryPromoIntelligentguideConsultResponse, self).parse_response_content(response_content)
        if 'consume_max' in response:
            self.consume_max = response['consume_max']
        if 'consume_min' in response:
            self.consume_min = response['consume_min']
        if 'recommend_card' in response:
            self.recommend_card = response['recommend_card']
        if 'recommend_service_info' in response:
            self.recommend_service_info = response['recommend_service_info']
        if 'user_tags' in response:
            self.user_tags = response['user_tags']

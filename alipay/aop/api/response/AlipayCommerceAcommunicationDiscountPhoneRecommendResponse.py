#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecommendItemInfo import RecommendItemInfo
from alipay.aop.api.domain.RecommendLayeredItemResponse import RecommendLayeredItemResponse


class AlipayCommerceAcommunicationDiscountPhoneRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDiscountPhoneRecommendResponse, self).__init__()
        self._mobile = None
        self._recommend_item_info = None
        self._recommend_layered_item_info = None

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def recommend_item_info(self):
        return self._recommend_item_info

    @recommend_item_info.setter
    def recommend_item_info(self, value):
        if isinstance(value, list):
            self._recommend_item_info = list()
            for i in value:
                if isinstance(i, RecommendItemInfo):
                    self._recommend_item_info.append(i)
                else:
                    self._recommend_item_info.append(RecommendItemInfo.from_alipay_dict(i))
    @property
    def recommend_layered_item_info(self):
        return self._recommend_layered_item_info

    @recommend_layered_item_info.setter
    def recommend_layered_item_info(self, value):
        if isinstance(value, RecommendLayeredItemResponse):
            self._recommend_layered_item_info = value
        else:
            self._recommend_layered_item_info = RecommendLayeredItemResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDiscountPhoneRecommendResponse, self).parse_response_content(response_content)
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'recommend_item_info' in response:
            self.recommend_item_info = response['recommend_item_info']
        if 'recommend_layered_item_info' in response:
            self.recommend_layered_item_info = response['recommend_layered_item_info']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentRoomApartmentInfo import RentRoomApartmentInfo
from alipay.aop.api.domain.RentRoomCommunityInfo import RentRoomCommunityInfo


class AlipayOpenAppRentroomAreaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppRentroomAreaQueryResponse, self).__init__()
        self._apartment_info = None
        self._area_type = None
        self._community_info = None

    @property
    def apartment_info(self):
        return self._apartment_info

    @apartment_info.setter
    def apartment_info(self, value):
        if isinstance(value, RentRoomApartmentInfo):
            self._apartment_info = value
        else:
            self._apartment_info = RentRoomApartmentInfo.from_alipay_dict(value)
    @property
    def area_type(self):
        return self._area_type

    @area_type.setter
    def area_type(self, value):
        self._area_type = value
    @property
    def community_info(self):
        return self._community_info

    @community_info.setter
    def community_info(self, value):
        if isinstance(value, RentRoomCommunityInfo):
            self._community_info = value
        else:
            self._community_info = RentRoomCommunityInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppRentroomAreaQueryResponse, self).parse_response_content(response_content)
        if 'apartment_info' in response:
            self.apartment_info = response['apartment_info']
        if 'area_type' in response:
            self.area_type = response['area_type']
        if 'community_info' in response:
            self.community_info = response['community_info']

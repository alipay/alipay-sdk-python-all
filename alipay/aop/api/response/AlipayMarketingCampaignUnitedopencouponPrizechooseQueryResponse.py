#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenPrizeCategoryDetail import OpenPrizeCategoryDetail


class AlipayMarketingCampaignUnitedopencouponPrizechooseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignUnitedopencouponPrizechooseQueryResponse, self).__init__()
        self._bind_phone = None
        self._camp_end_time = None
        self._camp_start_time = None
        self._camp_status = None
        self._login_id = None
        self._prize_category_details = None
        self._real_name_auth = None
        self._risk_user = None

    @property
    def bind_phone(self):
        return self._bind_phone

    @bind_phone.setter
    def bind_phone(self, value):
        self._bind_phone = value
    @property
    def camp_end_time(self):
        return self._camp_end_time

    @camp_end_time.setter
    def camp_end_time(self, value):
        self._camp_end_time = value
    @property
    def camp_start_time(self):
        return self._camp_start_time

    @camp_start_time.setter
    def camp_start_time(self, value):
        self._camp_start_time = value
    @property
    def camp_status(self):
        return self._camp_status

    @camp_status.setter
    def camp_status(self, value):
        self._camp_status = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def prize_category_details(self):
        return self._prize_category_details

    @prize_category_details.setter
    def prize_category_details(self, value):
        if isinstance(value, list):
            self._prize_category_details = list()
            for i in value:
                if isinstance(i, OpenPrizeCategoryDetail):
                    self._prize_category_details.append(i)
                else:
                    self._prize_category_details.append(OpenPrizeCategoryDetail.from_alipay_dict(i))
    @property
    def real_name_auth(self):
        return self._real_name_auth

    @real_name_auth.setter
    def real_name_auth(self, value):
        self._real_name_auth = value
    @property
    def risk_user(self):
        return self._risk_user

    @risk_user.setter
    def risk_user(self, value):
        self._risk_user = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignUnitedopencouponPrizechooseQueryResponse, self).parse_response_content(response_content)
        if 'bind_phone' in response:
            self.bind_phone = response['bind_phone']
        if 'camp_end_time' in response:
            self.camp_end_time = response['camp_end_time']
        if 'camp_start_time' in response:
            self.camp_start_time = response['camp_start_time']
        if 'camp_status' in response:
            self.camp_status = response['camp_status']
        if 'login_id' in response:
            self.login_id = response['login_id']
        if 'prize_category_details' in response:
            self.prize_category_details = response['prize_category_details']
        if 'real_name_auth' in response:
            self.real_name_auth = response['real_name_auth']
        if 'risk_user' in response:
            self.risk_user = response['risk_user']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UnitedVoucherDigest import UnitedVoucherDigest
from alipay.aop.api.domain.UnitedCountInfo import UnitedCountInfo


class AlipayMarketingCampaignUnitedopencouponConfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignUnitedopencouponConfigQueryResponse, self).__init__()
        self._bind_phone = None
        self._camp_end_time = None
        self._camp_start_time = None
        self._camp_status = None
        self._has_receive = None
        self._login_id = None
        self._lottery_mode = None
        self._real_name_auth = None
        self._remain_budget = None
        self._risk_user = None
        self._today_has_receive = None
        self._voucher_digests = None
        self._win_count_info = None
        self._win_enable = None

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
    def has_receive(self):
        return self._has_receive

    @has_receive.setter
    def has_receive(self, value):
        self._has_receive = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def lottery_mode(self):
        return self._lottery_mode

    @lottery_mode.setter
    def lottery_mode(self, value):
        self._lottery_mode = value
    @property
    def real_name_auth(self):
        return self._real_name_auth

    @real_name_auth.setter
    def real_name_auth(self, value):
        self._real_name_auth = value
    @property
    def remain_budget(self):
        return self._remain_budget

    @remain_budget.setter
    def remain_budget(self, value):
        self._remain_budget = value
    @property
    def risk_user(self):
        return self._risk_user

    @risk_user.setter
    def risk_user(self, value):
        self._risk_user = value
    @property
    def today_has_receive(self):
        return self._today_has_receive

    @today_has_receive.setter
    def today_has_receive(self, value):
        self._today_has_receive = value
    @property
    def voucher_digests(self):
        return self._voucher_digests

    @voucher_digests.setter
    def voucher_digests(self, value):
        if isinstance(value, UnitedVoucherDigest):
            self._voucher_digests = value
        else:
            self._voucher_digests = UnitedVoucherDigest.from_alipay_dict(value)
    @property
    def win_count_info(self):
        return self._win_count_info

    @win_count_info.setter
    def win_count_info(self, value):
        if isinstance(value, UnitedCountInfo):
            self._win_count_info = value
        else:
            self._win_count_info = UnitedCountInfo.from_alipay_dict(value)
    @property
    def win_enable(self):
        return self._win_enable

    @win_enable.setter
    def win_enable(self, value):
        self._win_enable = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignUnitedopencouponConfigQueryResponse, self).parse_response_content(response_content)
        if 'bind_phone' in response:
            self.bind_phone = response['bind_phone']
        if 'camp_end_time' in response:
            self.camp_end_time = response['camp_end_time']
        if 'camp_start_time' in response:
            self.camp_start_time = response['camp_start_time']
        if 'camp_status' in response:
            self.camp_status = response['camp_status']
        if 'has_receive' in response:
            self.has_receive = response['has_receive']
        if 'login_id' in response:
            self.login_id = response['login_id']
        if 'lottery_mode' in response:
            self.lottery_mode = response['lottery_mode']
        if 'real_name_auth' in response:
            self.real_name_auth = response['real_name_auth']
        if 'remain_budget' in response:
            self.remain_budget = response['remain_budget']
        if 'risk_user' in response:
            self.risk_user = response['risk_user']
        if 'today_has_receive' in response:
            self.today_has_receive = response['today_has_receive']
        if 'voucher_digests' in response:
            self.voucher_digests = response['voucher_digests']
        if 'win_count_info' in response:
            self.win_count_info = response['win_count_info']
        if 'win_enable' in response:
            self.win_enable = response['win_enable']

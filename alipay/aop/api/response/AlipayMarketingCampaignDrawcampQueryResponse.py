#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpPrizeInfoModel import MpPrizeInfoModel


class AlipayMarketingCampaignDrawcampQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignDrawcampQueryResponse, self).__init__()
        self._account_count = None
        self._appid_count = None
        self._award_count = None
        self._award_rate = None
        self._camp_code = None
        self._camp_end_time = None
        self._camp_id = None
        self._camp_name = None
        self._camp_start_time = None
        self._camp_status = None
        self._cert_rule_id = None
        self._certification_count = None
        self._creator = None
        self._crowd_rule_id = None
        self._mobile_count = None
        self._prize_list = None
        self._promo_rule_id = None
        self._trigger_type = None
        self._trigger_user_rule_id = None
        self._user_rule_id = None

    @property
    def account_count(self):
        return self._account_count

    @account_count.setter
    def account_count(self, value):
        self._account_count = value
    @property
    def appid_count(self):
        return self._appid_count

    @appid_count.setter
    def appid_count(self, value):
        self._appid_count = value
    @property
    def award_count(self):
        return self._award_count

    @award_count.setter
    def award_count(self, value):
        self._award_count = value
    @property
    def award_rate(self):
        return self._award_rate

    @award_rate.setter
    def award_rate(self, value):
        self._award_rate = value
    @property
    def camp_code(self):
        return self._camp_code

    @camp_code.setter
    def camp_code(self, value):
        self._camp_code = value
    @property
    def camp_end_time(self):
        return self._camp_end_time

    @camp_end_time.setter
    def camp_end_time(self, value):
        self._camp_end_time = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def camp_name(self):
        return self._camp_name

    @camp_name.setter
    def camp_name(self, value):
        self._camp_name = value
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
    def cert_rule_id(self):
        return self._cert_rule_id

    @cert_rule_id.setter
    def cert_rule_id(self, value):
        self._cert_rule_id = value
    @property
    def certification_count(self):
        return self._certification_count

    @certification_count.setter
    def certification_count(self, value):
        self._certification_count = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def crowd_rule_id(self):
        return self._crowd_rule_id

    @crowd_rule_id.setter
    def crowd_rule_id(self, value):
        self._crowd_rule_id = value
    @property
    def mobile_count(self):
        return self._mobile_count

    @mobile_count.setter
    def mobile_count(self, value):
        self._mobile_count = value
    @property
    def prize_list(self):
        return self._prize_list

    @prize_list.setter
    def prize_list(self, value):
        if isinstance(value, list):
            self._prize_list = list()
            for i in value:
                if isinstance(i, MpPrizeInfoModel):
                    self._prize_list.append(i)
                else:
                    self._prize_list.append(MpPrizeInfoModel.from_alipay_dict(i))
    @property
    def promo_rule_id(self):
        return self._promo_rule_id

    @promo_rule_id.setter
    def promo_rule_id(self, value):
        self._promo_rule_id = value
    @property
    def trigger_type(self):
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, value):
        self._trigger_type = value
    @property
    def trigger_user_rule_id(self):
        return self._trigger_user_rule_id

    @trigger_user_rule_id.setter
    def trigger_user_rule_id(self, value):
        self._trigger_user_rule_id = value
    @property
    def user_rule_id(self):
        return self._user_rule_id

    @user_rule_id.setter
    def user_rule_id(self, value):
        self._user_rule_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignDrawcampQueryResponse, self).parse_response_content(response_content)
        if 'account_count' in response:
            self.account_count = response['account_count']
        if 'appid_count' in response:
            self.appid_count = response['appid_count']
        if 'award_count' in response:
            self.award_count = response['award_count']
        if 'award_rate' in response:
            self.award_rate = response['award_rate']
        if 'camp_code' in response:
            self.camp_code = response['camp_code']
        if 'camp_end_time' in response:
            self.camp_end_time = response['camp_end_time']
        if 'camp_id' in response:
            self.camp_id = response['camp_id']
        if 'camp_name' in response:
            self.camp_name = response['camp_name']
        if 'camp_start_time' in response:
            self.camp_start_time = response['camp_start_time']
        if 'camp_status' in response:
            self.camp_status = response['camp_status']
        if 'cert_rule_id' in response:
            self.cert_rule_id = response['cert_rule_id']
        if 'certification_count' in response:
            self.certification_count = response['certification_count']
        if 'creator' in response:
            self.creator = response['creator']
        if 'crowd_rule_id' in response:
            self.crowd_rule_id = response['crowd_rule_id']
        if 'mobile_count' in response:
            self.mobile_count = response['mobile_count']
        if 'prize_list' in response:
            self.prize_list = response['prize_list']
        if 'promo_rule_id' in response:
            self.promo_rule_id = response['promo_rule_id']
        if 'trigger_type' in response:
            self.trigger_type = response['trigger_type']
        if 'trigger_user_rule_id' in response:
            self.trigger_user_rule_id = response['trigger_user_rule_id']
        if 'user_rule_id' in response:
            self.user_rule_id = response['user_rule_id']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MpPrizeInfoModel import MpPrizeInfoModel


class AlipayMarketingCampaignDrawcampCreateModel(object):

    def __init__(self):
        self._account_count = None
        self._appid_count = None
        self._award_count = None
        self._award_rate = None
        self._camp_code = None
        self._camp_end_time = None
        self._camp_name = None
        self._camp_start_time = None
        self._cert_rule_id = None
        self._certification_count = None
        self._crowd_rule_id = None
        self._mobile_count = None
        self._mpid = None
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
    def mpid(self):
        return self._mpid

    @mpid.setter
    def mpid(self, value):
        self._mpid = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.account_count:
            if hasattr(self.account_count, 'to_alipay_dict'):
                params['account_count'] = self.account_count.to_alipay_dict()
            else:
                params['account_count'] = self.account_count
        if self.appid_count:
            if hasattr(self.appid_count, 'to_alipay_dict'):
                params['appid_count'] = self.appid_count.to_alipay_dict()
            else:
                params['appid_count'] = self.appid_count
        if self.award_count:
            if hasattr(self.award_count, 'to_alipay_dict'):
                params['award_count'] = self.award_count.to_alipay_dict()
            else:
                params['award_count'] = self.award_count
        if self.award_rate:
            if hasattr(self.award_rate, 'to_alipay_dict'):
                params['award_rate'] = self.award_rate.to_alipay_dict()
            else:
                params['award_rate'] = self.award_rate
        if self.camp_code:
            if hasattr(self.camp_code, 'to_alipay_dict'):
                params['camp_code'] = self.camp_code.to_alipay_dict()
            else:
                params['camp_code'] = self.camp_code
        if self.camp_end_time:
            if hasattr(self.camp_end_time, 'to_alipay_dict'):
                params['camp_end_time'] = self.camp_end_time.to_alipay_dict()
            else:
                params['camp_end_time'] = self.camp_end_time
        if self.camp_name:
            if hasattr(self.camp_name, 'to_alipay_dict'):
                params['camp_name'] = self.camp_name.to_alipay_dict()
            else:
                params['camp_name'] = self.camp_name
        if self.camp_start_time:
            if hasattr(self.camp_start_time, 'to_alipay_dict'):
                params['camp_start_time'] = self.camp_start_time.to_alipay_dict()
            else:
                params['camp_start_time'] = self.camp_start_time
        if self.cert_rule_id:
            if hasattr(self.cert_rule_id, 'to_alipay_dict'):
                params['cert_rule_id'] = self.cert_rule_id.to_alipay_dict()
            else:
                params['cert_rule_id'] = self.cert_rule_id
        if self.certification_count:
            if hasattr(self.certification_count, 'to_alipay_dict'):
                params['certification_count'] = self.certification_count.to_alipay_dict()
            else:
                params['certification_count'] = self.certification_count
        if self.crowd_rule_id:
            if hasattr(self.crowd_rule_id, 'to_alipay_dict'):
                params['crowd_rule_id'] = self.crowd_rule_id.to_alipay_dict()
            else:
                params['crowd_rule_id'] = self.crowd_rule_id
        if self.mobile_count:
            if hasattr(self.mobile_count, 'to_alipay_dict'):
                params['mobile_count'] = self.mobile_count.to_alipay_dict()
            else:
                params['mobile_count'] = self.mobile_count
        if self.mpid:
            if hasattr(self.mpid, 'to_alipay_dict'):
                params['mpid'] = self.mpid.to_alipay_dict()
            else:
                params['mpid'] = self.mpid
        if self.prize_list:
            if isinstance(self.prize_list, list):
                for i in range(0, len(self.prize_list)):
                    element = self.prize_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_list[i] = element.to_alipay_dict()
            if hasattr(self.prize_list, 'to_alipay_dict'):
                params['prize_list'] = self.prize_list.to_alipay_dict()
            else:
                params['prize_list'] = self.prize_list
        if self.promo_rule_id:
            if hasattr(self.promo_rule_id, 'to_alipay_dict'):
                params['promo_rule_id'] = self.promo_rule_id.to_alipay_dict()
            else:
                params['promo_rule_id'] = self.promo_rule_id
        if self.trigger_type:
            if hasattr(self.trigger_type, 'to_alipay_dict'):
                params['trigger_type'] = self.trigger_type.to_alipay_dict()
            else:
                params['trigger_type'] = self.trigger_type
        if self.trigger_user_rule_id:
            if hasattr(self.trigger_user_rule_id, 'to_alipay_dict'):
                params['trigger_user_rule_id'] = self.trigger_user_rule_id.to_alipay_dict()
            else:
                params['trigger_user_rule_id'] = self.trigger_user_rule_id
        if self.user_rule_id:
            if hasattr(self.user_rule_id, 'to_alipay_dict'):
                params['user_rule_id'] = self.user_rule_id.to_alipay_dict()
            else:
                params['user_rule_id'] = self.user_rule_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignDrawcampCreateModel()
        if 'account_count' in d:
            o.account_count = d['account_count']
        if 'appid_count' in d:
            o.appid_count = d['appid_count']
        if 'award_count' in d:
            o.award_count = d['award_count']
        if 'award_rate' in d:
            o.award_rate = d['award_rate']
        if 'camp_code' in d:
            o.camp_code = d['camp_code']
        if 'camp_end_time' in d:
            o.camp_end_time = d['camp_end_time']
        if 'camp_name' in d:
            o.camp_name = d['camp_name']
        if 'camp_start_time' in d:
            o.camp_start_time = d['camp_start_time']
        if 'cert_rule_id' in d:
            o.cert_rule_id = d['cert_rule_id']
        if 'certification_count' in d:
            o.certification_count = d['certification_count']
        if 'crowd_rule_id' in d:
            o.crowd_rule_id = d['crowd_rule_id']
        if 'mobile_count' in d:
            o.mobile_count = d['mobile_count']
        if 'mpid' in d:
            o.mpid = d['mpid']
        if 'prize_list' in d:
            o.prize_list = d['prize_list']
        if 'promo_rule_id' in d:
            o.promo_rule_id = d['promo_rule_id']
        if 'trigger_type' in d:
            o.trigger_type = d['trigger_type']
        if 'trigger_user_rule_id' in d:
            o.trigger_user_rule_id = d['trigger_user_rule_id']
        if 'user_rule_id' in d:
            o.user_rule_id = d['user_rule_id']
        return o



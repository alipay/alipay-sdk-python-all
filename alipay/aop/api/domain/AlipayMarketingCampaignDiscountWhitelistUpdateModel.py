#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignDiscountWhitelistUpdateModel(object):

    def __init__(self):
        self._camp_id = None
        self._user_white_list = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def user_white_list(self):
        return self._user_white_list

    @user_white_list.setter
    def user_white_list(self, value):
        self._user_white_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.user_white_list:
            if hasattr(self.user_white_list, 'to_alipay_dict'):
                params['user_white_list'] = self.user_white_list.to_alipay_dict()
            else:
                params['user_white_list'] = self.user_white_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignDiscountWhitelistUpdateModel()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'user_white_list' in d:
            o.user_white_list = d['user_white_list']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignUnicardCardRefundModel(object):

    def __init__(self):
        self._uni_card_no = None
        self._user_id = None

    @property
    def uni_card_no(self):
        return self._uni_card_no

    @uni_card_no.setter
    def uni_card_no(self, value):
        self._uni_card_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.uni_card_no:
            if hasattr(self.uni_card_no, 'to_alipay_dict'):
                params['uni_card_no'] = self.uni_card_no.to_alipay_dict()
            else:
                params['uni_card_no'] = self.uni_card_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignUnicardCardRefundModel()
        if 'uni_card_no' in d:
            o.uni_card_no = d['uni_card_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



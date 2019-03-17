#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignMemberAuthApplyModel(object):

    def __init__(self):
        self._auth_token = None

    @property
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, value):
        self._auth_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_token:
            if hasattr(self.auth_token, 'to_alipay_dict'):
                params['auth_token'] = self.auth_token.to_alipay_dict()
            else:
                params['auth_token'] = self.auth_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignMemberAuthApplyModel()
        if 'auth_token' in d:
            o.auth_token = d['auth_token']
        return o



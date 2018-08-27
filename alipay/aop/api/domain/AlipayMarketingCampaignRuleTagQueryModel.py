#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignRuleTagQueryModel(object):

    def __init__(self):
        self._mpid = None

    @property
    def mpid(self):
        return self._mpid

    @mpid.setter
    def mpid(self, value):
        self._mpid = value


    def to_alipay_dict(self):
        params = dict()
        if self.mpid:
            if hasattr(self.mpid, 'to_alipay_dict'):
                params['mpid'] = self.mpid.to_alipay_dict()
            else:
                params['mpid'] = self.mpid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignRuleTagQueryModel()
        if 'mpid' in d:
            o.mpid = d['mpid']
        return o



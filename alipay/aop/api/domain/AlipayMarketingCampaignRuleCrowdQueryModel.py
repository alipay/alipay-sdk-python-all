#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignRuleCrowdQueryModel(object):

    def __init__(self):
        self._mpid = None
        self._ruleid = None

    @property
    def mpid(self):
        return self._mpid

    @mpid.setter
    def mpid(self, value):
        self._mpid = value
    @property
    def ruleid(self):
        return self._ruleid

    @ruleid.setter
    def ruleid(self, value):
        self._ruleid = value


    def to_alipay_dict(self):
        params = dict()
        if self.mpid:
            if hasattr(self.mpid, 'to_alipay_dict'):
                params['mpid'] = self.mpid.to_alipay_dict()
            else:
                params['mpid'] = self.mpid
        if self.ruleid:
            if hasattr(self.ruleid, 'to_alipay_dict'):
                params['ruleid'] = self.ruleid.to_alipay_dict()
            else:
                params['ruleid'] = self.ruleid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignRuleCrowdQueryModel()
        if 'mpid' in d:
            o.mpid = d['mpid']
        if 'ruleid' in d:
            o.ruleid = d['ruleid']
        return o



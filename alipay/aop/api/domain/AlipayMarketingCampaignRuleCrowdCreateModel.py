#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignRuleCrowdCreateModel(object):

    def __init__(self):
        self._mdatacrowdsource = None
        self._mpid = None
        self._ruledesc = None

    @property
    def mdatacrowdsource(self):
        return self._mdatacrowdsource

    @mdatacrowdsource.setter
    def mdatacrowdsource(self, value):
        self._mdatacrowdsource = value
    @property
    def mpid(self):
        return self._mpid

    @mpid.setter
    def mpid(self, value):
        self._mpid = value
    @property
    def ruledesc(self):
        return self._ruledesc

    @ruledesc.setter
    def ruledesc(self, value):
        self._ruledesc = value


    def to_alipay_dict(self):
        params = dict()
        if self.mdatacrowdsource:
            if hasattr(self.mdatacrowdsource, 'to_alipay_dict'):
                params['mdatacrowdsource'] = self.mdatacrowdsource.to_alipay_dict()
            else:
                params['mdatacrowdsource'] = self.mdatacrowdsource
        if self.mpid:
            if hasattr(self.mpid, 'to_alipay_dict'):
                params['mpid'] = self.mpid.to_alipay_dict()
            else:
                params['mpid'] = self.mpid
        if self.ruledesc:
            if hasattr(self.ruledesc, 'to_alipay_dict'):
                params['ruledesc'] = self.ruledesc.to_alipay_dict()
            else:
                params['ruledesc'] = self.ruledesc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignRuleCrowdCreateModel()
        if 'mdatacrowdsource' in d:
            o.mdatacrowdsource = d['mdatacrowdsource']
        if 'mpid' in d:
            o.mpid = d['mpid']
        if 'ruledesc' in d:
            o.ruledesc = d['ruledesc']
        return o



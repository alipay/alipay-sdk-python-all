#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignCashStatusModifyModel(object):

    def __init__(self):
        self._camp_status = None
        self._crowd_no = None

    @property
    def camp_status(self):
        return self._camp_status

    @camp_status.setter
    def camp_status(self, value):
        self._camp_status = value
    @property
    def crowd_no(self):
        return self._crowd_no

    @crowd_no.setter
    def crowd_no(self, value):
        self._crowd_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_status:
            if hasattr(self.camp_status, 'to_alipay_dict'):
                params['camp_status'] = self.camp_status.to_alipay_dict()
            else:
                params['camp_status'] = self.camp_status
        if self.crowd_no:
            if hasattr(self.crowd_no, 'to_alipay_dict'):
                params['crowd_no'] = self.crowd_no.to_alipay_dict()
            else:
                params['crowd_no'] = self.crowd_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignCashStatusModifyModel()
        if 'camp_status' in d:
            o.camp_status = d['camp_status']
        if 'crowd_no' in d:
            o.crowd_no = d['crowd_no']
        return o



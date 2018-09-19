#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignDrawcampStatusUpdateModel(object):

    def __init__(self):
        self._camp_id = None
        self._camp_status = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def camp_status(self):
        return self._camp_status

    @camp_status.setter
    def camp_status(self, value):
        self._camp_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.camp_status:
            if hasattr(self.camp_status, 'to_alipay_dict'):
                params['camp_status'] = self.camp_status.to_alipay_dict()
            else:
                params['camp_status'] = self.camp_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignDrawcampStatusUpdateModel()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'camp_status' in d:
            o.camp_status = d['camp_status']
        return o



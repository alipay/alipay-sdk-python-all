#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignCrowdDetailQueryModel(object):

    def __init__(self):
        self._crowd_group_id = None

    @property
    def crowd_group_id(self):
        return self._crowd_group_id

    @crowd_group_id.setter
    def crowd_group_id(self, value):
        self._crowd_group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_group_id:
            if hasattr(self.crowd_group_id, 'to_alipay_dict'):
                params['crowd_group_id'] = self.crowd_group_id.to_alipay_dict()
            else:
                params['crowd_group_id'] = self.crowd_group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignCrowdDetailQueryModel()
        if 'crowd_group_id' in d:
            o.crowd_group_id = d['crowd_group_id']
        return o



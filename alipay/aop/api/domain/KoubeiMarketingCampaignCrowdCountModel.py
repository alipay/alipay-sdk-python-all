#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignCrowdCountModel(object):

    def __init__(self):
        self._conditions = None
        self._crowd_group_id = None
        self._dimensions = None

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        self._conditions = value
    @property
    def crowd_group_id(self):
        return self._crowd_group_id

    @crowd_group_id.setter
    def crowd_group_id(self, value):
        self._crowd_group_id = value
    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):
        self._dimensions = value


    def to_alipay_dict(self):
        params = dict()
        if self.conditions:
            if hasattr(self.conditions, 'to_alipay_dict'):
                params['conditions'] = self.conditions.to_alipay_dict()
            else:
                params['conditions'] = self.conditions
        if self.crowd_group_id:
            if hasattr(self.crowd_group_id, 'to_alipay_dict'):
                params['crowd_group_id'] = self.crowd_group_id.to_alipay_dict()
            else:
                params['crowd_group_id'] = self.crowd_group_id
        if self.dimensions:
            if hasattr(self.dimensions, 'to_alipay_dict'):
                params['dimensions'] = self.dimensions.to_alipay_dict()
            else:
                params['dimensions'] = self.dimensions
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignCrowdCountModel()
        if 'conditions' in d:
            o.conditions = d['conditions']
        if 'crowd_group_id' in d:
            o.crowd_group_id = d['crowd_group_id']
        if 'dimensions' in d:
            o.dimensions = d['dimensions']
        return o



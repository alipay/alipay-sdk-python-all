#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneMarketingCrowdWshopMatchModel(object):

    def __init__(self):
        self._crowd_id = None
        self._user_id = None

    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
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
        o = AntfortuneMarketingCrowdWshopMatchModel()
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



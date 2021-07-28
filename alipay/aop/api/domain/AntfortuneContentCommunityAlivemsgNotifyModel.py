#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneContentCommunityAlivemsgNotifyModel(object):

    def __init__(self):
        self._live_id = None
        self._live_status = None
        self._tb_user_id = None

    @property
    def live_id(self):
        return self._live_id

    @live_id.setter
    def live_id(self, value):
        self._live_id = value
    @property
    def live_status(self):
        return self._live_status

    @live_status.setter
    def live_status(self, value):
        self._live_status = value
    @property
    def tb_user_id(self):
        return self._tb_user_id

    @tb_user_id.setter
    def tb_user_id(self, value):
        self._tb_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.live_id:
            if hasattr(self.live_id, 'to_alipay_dict'):
                params['live_id'] = self.live_id.to_alipay_dict()
            else:
                params['live_id'] = self.live_id
        if self.live_status:
            if hasattr(self.live_status, 'to_alipay_dict'):
                params['live_status'] = self.live_status.to_alipay_dict()
            else:
                params['live_status'] = self.live_status
        if self.tb_user_id:
            if hasattr(self.tb_user_id, 'to_alipay_dict'):
                params['tb_user_id'] = self.tb_user_id.to_alipay_dict()
            else:
                params['tb_user_id'] = self.tb_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneContentCommunityAlivemsgNotifyModel()
        if 'live_id' in d:
            o.live_id = d['live_id']
        if 'live_status' in d:
            o.live_status = d['live_status']
        if 'tb_user_id' in d:
            o.tb_user_id = d['tb_user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WatchPromoPrizeDetail(object):

    def __init__(self):
        self._biz_no = None
        self._jump_alipay_url = None
        self._prize_state = None
        self._prize_type = None
        self._skin_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def jump_alipay_url(self):
        return self._jump_alipay_url

    @jump_alipay_url.setter
    def jump_alipay_url(self, value):
        self._jump_alipay_url = value
    @property
    def prize_state(self):
        return self._prize_state

    @prize_state.setter
    def prize_state(self, value):
        self._prize_state = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def skin_id(self):
        return self._skin_id

    @skin_id.setter
    def skin_id(self, value):
        self._skin_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.jump_alipay_url:
            if hasattr(self.jump_alipay_url, 'to_alipay_dict'):
                params['jump_alipay_url'] = self.jump_alipay_url.to_alipay_dict()
            else:
                params['jump_alipay_url'] = self.jump_alipay_url
        if self.prize_state:
            if hasattr(self.prize_state, 'to_alipay_dict'):
                params['prize_state'] = self.prize_state.to_alipay_dict()
            else:
                params['prize_state'] = self.prize_state
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.skin_id:
            if hasattr(self.skin_id, 'to_alipay_dict'):
                params['skin_id'] = self.skin_id.to_alipay_dict()
            else:
                params['skin_id'] = self.skin_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WatchPromoPrizeDetail()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'jump_alipay_url' in d:
            o.jump_alipay_url = d['jump_alipay_url']
        if 'prize_state' in d:
            o.prize_state = d['prize_state']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'skin_id' in d:
            o.skin_id = d['skin_id']
        return o



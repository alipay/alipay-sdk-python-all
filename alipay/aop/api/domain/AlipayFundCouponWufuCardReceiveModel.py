#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundCouponWufuCardReceiveModel(object):

    def __init__(self):
        self._front_biz_no = None
        self._scene = None
        self._user_id = None

    @property
    def front_biz_no(self):
        return self._front_biz_no

    @front_biz_no.setter
    def front_biz_no(self, value):
        self._front_biz_no = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.front_biz_no:
            if hasattr(self.front_biz_no, 'to_alipay_dict'):
                params['front_biz_no'] = self.front_biz_no.to_alipay_dict()
            else:
                params['front_biz_no'] = self.front_biz_no
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        o = AlipayFundCouponWufuCardReceiveModel()
        if 'front_biz_no' in d:
            o.front_biz_no = d['front_biz_no']
        if 'scene' in d:
            o.scene = d['scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



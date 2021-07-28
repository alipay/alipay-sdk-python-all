#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundCouponWufuLiveAcceptModel(object):

    def __init__(self):
        self._card_type = None
        self._front_biz_no = None
        self._scene = None
        self._taobao_id = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
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
    def taobao_id(self):
        return self._taobao_id

    @taobao_id.setter
    def taobao_id(self, value):
        self._taobao_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
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
        if self.taobao_id:
            if hasattr(self.taobao_id, 'to_alipay_dict'):
                params['taobao_id'] = self.taobao_id.to_alipay_dict()
            else:
                params['taobao_id'] = self.taobao_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundCouponWufuLiveAcceptModel()
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'front_biz_no' in d:
            o.front_biz_no = d['front_biz_no']
        if 'scene' in d:
            o.scene = d['scene']
        if 'taobao_id' in d:
            o.taobao_id = d['taobao_id']
        return o



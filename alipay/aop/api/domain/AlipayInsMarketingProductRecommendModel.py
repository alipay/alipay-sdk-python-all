#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsObject import InsObject
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsPerson import InsPerson


class AlipayInsMarketingProductRecommendModel(object):

    def __init__(self):
        self._biz_data = None
        self._ins_object = None
        self._scene_code = None
        self._source = None
        self._stake_holders = None
        self._user = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def ins_object(self):
        return self._ins_object

    @ins_object.setter
    def ins_object(self, value):
        if isinstance(value, InsObject):
            self._ins_object = value
        else:
            self._ins_object = InsObject.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def stake_holders(self):
        return self._stake_holders

    @stake_holders.setter
    def stake_holders(self, value):
        if isinstance(value, InsPerson):
            self._stake_holders = value
        else:
            self._stake_holders = InsPerson.from_alipay_dict(value)
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, InsPerson):
            self._user = value
        else:
            self._user = InsPerson.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.ins_object:
            if hasattr(self.ins_object, 'to_alipay_dict'):
                params['ins_object'] = self.ins_object.to_alipay_dict()
            else:
                params['ins_object'] = self.ins_object
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.stake_holders:
            if hasattr(self.stake_holders, 'to_alipay_dict'):
                params['stake_holders'] = self.stake_holders.to_alipay_dict()
            else:
                params['stake_holders'] = self.stake_holders
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsMarketingProductRecommendModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'ins_object' in d:
            o.ins_object = d['ins_object']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'source' in d:
            o.source = d['source']
        if 'stake_holders' in d:
            o.stake_holders = d['stake_holders']
        if 'user' in d:
            o.user = d['user']
        return o



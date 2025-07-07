#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleAddressInfo import RecycleAddressInfo
from alipay.aop.api.domain.RecycleOutAssessInfo import RecycleOutAssessInfo


class AlipayCommerceRecycleOutOrderCreateModel(object):

    def __init__(self):
        self._address_info = None
        self._assess_info = None
        self._biz_scene = None
        self._from_source = None
        self._memo = None
        self._open_id = None
        self._order_channel = None
        self._user_id = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, RecycleAddressInfo):
            self._address_info = value
        else:
            self._address_info = RecycleAddressInfo.from_alipay_dict(value)
    @property
    def assess_info(self):
        return self._assess_info

    @assess_info.setter
    def assess_info(self, value):
        if isinstance(value, RecycleOutAssessInfo):
            self._assess_info = value
        else:
            self._assess_info = RecycleOutAssessInfo.from_alipay_dict(value)
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def from_source(self):
        return self._from_source

    @from_source.setter
    def from_source(self, value):
        self._from_source = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_channel(self):
        return self._order_channel

    @order_channel.setter
    def order_channel(self, value):
        self._order_channel = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.assess_info:
            if hasattr(self.assess_info, 'to_alipay_dict'):
                params['assess_info'] = self.assess_info.to_alipay_dict()
            else:
                params['assess_info'] = self.assess_info
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.from_source:
            if hasattr(self.from_source, 'to_alipay_dict'):
                params['from_source'] = self.from_source.to_alipay_dict()
            else:
                params['from_source'] = self.from_source
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_channel:
            if hasattr(self.order_channel, 'to_alipay_dict'):
                params['order_channel'] = self.order_channel.to_alipay_dict()
            else:
                params['order_channel'] = self.order_channel
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
        o = AlipayCommerceRecycleOutOrderCreateModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'assess_info' in d:
            o.assess_info = d['assess_info']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'from_source' in d:
            o.from_source = d['from_source']
        if 'memo' in d:
            o.memo = d['memo']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_channel' in d:
            o.order_channel = d['order_channel']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



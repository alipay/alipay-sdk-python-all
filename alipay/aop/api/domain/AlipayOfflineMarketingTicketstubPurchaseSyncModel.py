#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineMarketingTicketstubPurchaseSyncModel(object):

    def __init__(self):
        self._action_type = None
        self._biz_no = None
        self._buyer_info = None
        self._order_no = None
        self._order_time = None
        self._scene_code = None
        self._stub_info = None
        self._venue_code = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        self._buyer_info = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def stub_info(self):
        return self._stub_info

    @stub_info.setter
    def stub_info(self, value):
        self._stub_info = value
    @property
    def venue_code(self):
        return self._venue_code

    @venue_code.setter
    def venue_code(self, value):
        self._venue_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.stub_info:
            if hasattr(self.stub_info, 'to_alipay_dict'):
                params['stub_info'] = self.stub_info.to_alipay_dict()
            else:
                params['stub_info'] = self.stub_info
        if self.venue_code:
            if hasattr(self.venue_code, 'to_alipay_dict'):
                params['venue_code'] = self.venue_code.to_alipay_dict()
            else:
                params['venue_code'] = self.venue_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketingTicketstubPurchaseSyncModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'stub_info' in d:
            o.stub_info = d['stub_info']
        if 'venue_code' in d:
            o.venue_code = d['venue_code']
        return o



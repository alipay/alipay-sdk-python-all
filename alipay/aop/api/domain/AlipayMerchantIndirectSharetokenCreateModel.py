#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantIndirectSharetokenCreateModel(object):

    def __init__(self):
        self._biz_link = None
        self._biz_scene = None
        self._biz_tracker = None
        self._channel_info = None
        self._expire_time = None
        self._merchant_name = None
        self._out_biz_no = None
        self._out_open_id = None
        self._partner_id = None
        self._pay_amount = None
        self._sub_merchant_id = None

    @property
    def biz_link(self):
        return self._biz_link

    @biz_link.setter
    def biz_link(self, value):
        self._biz_link = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def biz_tracker(self):
        return self._biz_tracker

    @biz_tracker.setter
    def biz_tracker(self, value):
        self._biz_tracker = value
    @property
    def channel_info(self):
        return self._channel_info

    @channel_info.setter
    def channel_info(self, value):
        self._channel_info = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_open_id(self):
        return self._out_open_id

    @out_open_id.setter
    def out_open_id(self, value):
        self._out_open_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_link:
            if hasattr(self.biz_link, 'to_alipay_dict'):
                params['biz_link'] = self.biz_link.to_alipay_dict()
            else:
                params['biz_link'] = self.biz_link
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.biz_tracker:
            if hasattr(self.biz_tracker, 'to_alipay_dict'):
                params['biz_tracker'] = self.biz_tracker.to_alipay_dict()
            else:
                params['biz_tracker'] = self.biz_tracker
        if self.channel_info:
            if hasattr(self.channel_info, 'to_alipay_dict'):
                params['channel_info'] = self.channel_info.to_alipay_dict()
            else:
                params['channel_info'] = self.channel_info
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_open_id:
            if hasattr(self.out_open_id, 'to_alipay_dict'):
                params['out_open_id'] = self.out_open_id.to_alipay_dict()
            else:
                params['out_open_id'] = self.out_open_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectSharetokenCreateModel()
        if 'biz_link' in d:
            o.biz_link = d['biz_link']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'biz_tracker' in d:
            o.biz_tracker = d['biz_tracker']
        if 'channel_info' in d:
            o.channel_info = d['channel_info']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_open_id' in d:
            o.out_open_id = d['out_open_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        return o



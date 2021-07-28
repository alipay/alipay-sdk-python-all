#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiSceneprodBenefitCreateModel(object):

    def __init__(self):
        self._benefit_channel = None
        self._benefit_name = None
        self._benefit_type = None
        self._biz_scene = None
        self._budget = None
        self._end_time = None
        self._out_biz_no = None
        self._partner_id = None
        self._seller_id = None
        self._send_count = None
        self._start_time = None

    @property
    def benefit_channel(self):
        return self._benefit_channel

    @benefit_channel.setter
    def benefit_channel(self, value):
        self._benefit_channel = value
    @property
    def benefit_name(self):
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, value):
        self._benefit_name = value
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        self._budget = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def send_count(self):
        return self._send_count

    @send_count.setter
    def send_count(self, value):
        self._send_count = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_channel:
            if hasattr(self.benefit_channel, 'to_alipay_dict'):
                params['benefit_channel'] = self.benefit_channel.to_alipay_dict()
            else:
                params['benefit_channel'] = self.benefit_channel
        if self.benefit_name:
            if hasattr(self.benefit_name, 'to_alipay_dict'):
                params['benefit_name'] = self.benefit_name.to_alipay_dict()
            else:
                params['benefit_name'] = self.benefit_name
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.budget:
            if hasattr(self.budget, 'to_alipay_dict'):
                params['budget'] = self.budget.to_alipay_dict()
            else:
                params['budget'] = self.budget
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.send_count:
            if hasattr(self.send_count, 'to_alipay_dict'):
                params['send_count'] = self.send_count.to_alipay_dict()
            else:
                params['send_count'] = self.send_count
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiSceneprodBenefitCreateModel()
        if 'benefit_channel' in d:
            o.benefit_channel = d['benefit_channel']
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'budget' in d:
            o.budget = d['budget']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'send_count' in d:
            o.send_count = d['send_count']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o



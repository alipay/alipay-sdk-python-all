#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySupervisionFundstransferQuerystatusModel(object):

    def __init__(self):
        self._biz_scene = None
        self._operate_no = None
        self._out_trade_no = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def operate_no(self):
        return self._operate_no

    @operate_no.setter
    def operate_no(self, value):
        self._operate_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.operate_no:
            if hasattr(self.operate_no, 'to_alipay_dict'):
                params['operate_no'] = self.operate_no.to_alipay_dict()
            else:
                params['operate_no'] = self.operate_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySupervisionFundstransferQuerystatusModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'operate_no' in d:
            o.operate_no = d['operate_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        return o



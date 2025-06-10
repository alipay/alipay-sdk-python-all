#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingAssetTransferdetailQueryModel(object):

    def __init__(self):
        self._scene_code = None
        self._scene_param_map = None
        self._trade_no = None
        self._trans_types = None

    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_param_map(self):
        return self._scene_param_map

    @scene_param_map.setter
    def scene_param_map(self, value):
        self._scene_param_map = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trans_types(self):
        return self._trans_types

    @trans_types.setter
    def trans_types(self, value):
        if isinstance(value, list):
            self._trans_types = list()
            for i in value:
                self._trans_types.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_param_map:
            if hasattr(self.scene_param_map, 'to_alipay_dict'):
                params['scene_param_map'] = self.scene_param_map.to_alipay_dict()
            else:
                params['scene_param_map'] = self.scene_param_map
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trans_types:
            if isinstance(self.trans_types, list):
                for i in range(0, len(self.trans_types)):
                    element = self.trans_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trans_types[i] = element.to_alipay_dict()
            if hasattr(self.trans_types, 'to_alipay_dict'):
                params['trans_types'] = self.trans_types.to_alipay_dict()
            else:
                params['trans_types'] = self.trans_types
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingAssetTransferdetailQueryModel()
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_param_map' in d:
            o.scene_param_map = d['scene_param_map']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trans_types' in d:
            o.trans_types = d['trans_types']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantIndirectIotQueryModel(object):

    def __init__(self):
        self._device_id = None
        self._device_id_type = None
        self._occasion = None
        self._play_mode = None
        self._smid = None
        self._suppler_id = None
        self._trade_id = None
        self._trade_type = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_id_type(self):
        return self._device_id_type

    @device_id_type.setter
    def device_id_type(self, value):
        self._device_id_type = value
    @property
    def occasion(self):
        return self._occasion

    @occasion.setter
    def occasion(self, value):
        self._occasion = value
    @property
    def play_mode(self):
        return self._play_mode

    @play_mode.setter
    def play_mode(self, value):
        self._play_mode = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def suppler_id(self):
        return self._suppler_id

    @suppler_id.setter
    def suppler_id(self, value):
        self._suppler_id = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_id_type:
            if hasattr(self.device_id_type, 'to_alipay_dict'):
                params['device_id_type'] = self.device_id_type.to_alipay_dict()
            else:
                params['device_id_type'] = self.device_id_type
        if self.occasion:
            if hasattr(self.occasion, 'to_alipay_dict'):
                params['occasion'] = self.occasion.to_alipay_dict()
            else:
                params['occasion'] = self.occasion
        if self.play_mode:
            if hasattr(self.play_mode, 'to_alipay_dict'):
                params['play_mode'] = self.play_mode.to_alipay_dict()
            else:
                params['play_mode'] = self.play_mode
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.suppler_id:
            if hasattr(self.suppler_id, 'to_alipay_dict'):
                params['suppler_id'] = self.suppler_id.to_alipay_dict()
            else:
                params['suppler_id'] = self.suppler_id
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectIotQueryModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_id_type' in d:
            o.device_id_type = d['device_id_type']
        if 'occasion' in d:
            o.occasion = d['occasion']
        if 'play_mode' in d:
            o.play_mode = d['play_mode']
        if 'smid' in d:
            o.smid = d['smid']
        if 'suppler_id' in d:
            o.suppler_id = d['suppler_id']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o



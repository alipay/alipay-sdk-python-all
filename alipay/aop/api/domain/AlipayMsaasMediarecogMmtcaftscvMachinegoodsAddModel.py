#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsState import GoodsState


class AlipayMsaasMediarecogMmtcaftscvMachinegoodsAddModel(object):

    def __init__(self):
        self._algorithm_goods_id = None
        self._display_mode = None
        self._exist_goods_state = None
        self._floor_num = None
        self._machine_type_id = None

    @property
    def algorithm_goods_id(self):
        return self._algorithm_goods_id

    @algorithm_goods_id.setter
    def algorithm_goods_id(self, value):
        self._algorithm_goods_id = value
    @property
    def display_mode(self):
        return self._display_mode

    @display_mode.setter
    def display_mode(self, value):
        self._display_mode = value
    @property
    def exist_goods_state(self):
        return self._exist_goods_state

    @exist_goods_state.setter
    def exist_goods_state(self, value):
        if isinstance(value, list):
            self._exist_goods_state = list()
            for i in value:
                if isinstance(i, GoodsState):
                    self._exist_goods_state.append(i)
                else:
                    self._exist_goods_state.append(GoodsState.from_alipay_dict(i))
    @property
    def floor_num(self):
        return self._floor_num

    @floor_num.setter
    def floor_num(self, value):
        self._floor_num = value
    @property
    def machine_type_id(self):
        return self._machine_type_id

    @machine_type_id.setter
    def machine_type_id(self, value):
        self._machine_type_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_goods_id:
            if hasattr(self.algorithm_goods_id, 'to_alipay_dict'):
                params['algorithm_goods_id'] = self.algorithm_goods_id.to_alipay_dict()
            else:
                params['algorithm_goods_id'] = self.algorithm_goods_id
        if self.display_mode:
            if hasattr(self.display_mode, 'to_alipay_dict'):
                params['display_mode'] = self.display_mode.to_alipay_dict()
            else:
                params['display_mode'] = self.display_mode
        if self.exist_goods_state:
            if isinstance(self.exist_goods_state, list):
                for i in range(0, len(self.exist_goods_state)):
                    element = self.exist_goods_state[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exist_goods_state[i] = element.to_alipay_dict()
            if hasattr(self.exist_goods_state, 'to_alipay_dict'):
                params['exist_goods_state'] = self.exist_goods_state.to_alipay_dict()
            else:
                params['exist_goods_state'] = self.exist_goods_state
        if self.floor_num:
            if hasattr(self.floor_num, 'to_alipay_dict'):
                params['floor_num'] = self.floor_num.to_alipay_dict()
            else:
                params['floor_num'] = self.floor_num
        if self.machine_type_id:
            if hasattr(self.machine_type_id, 'to_alipay_dict'):
                params['machine_type_id'] = self.machine_type_id.to_alipay_dict()
            else:
                params['machine_type_id'] = self.machine_type_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcaftscvMachinegoodsAddModel()
        if 'algorithm_goods_id' in d:
            o.algorithm_goods_id = d['algorithm_goods_id']
        if 'display_mode' in d:
            o.display_mode = d['display_mode']
        if 'exist_goods_state' in d:
            o.exist_goods_state = d['exist_goods_state']
        if 'floor_num' in d:
            o.floor_num = d['floor_num']
        if 'machine_type_id' in d:
            o.machine_type_id = d['machine_type_id']
        return o



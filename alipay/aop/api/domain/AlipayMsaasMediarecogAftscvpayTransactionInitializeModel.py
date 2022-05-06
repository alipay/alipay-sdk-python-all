#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodInfo import GoodInfo
from alipay.aop.api.domain.WeightFloor import WeightFloor


class AlipayMsaasMediarecogAftscvpayTransactionInitializeModel(object):

    def __init__(self):
        self._goods_infos = None
        self._machine_type = None
        self._scene = None
        self._terminal_id = None
        self._total_floors = None
        self._transaction_id = None
        self._type = None
        self._uid = None
        self._weight_template = None

    @property
    def goods_infos(self):
        return self._goods_infos

    @goods_infos.setter
    def goods_infos(self, value):
        if isinstance(value, list):
            self._goods_infos = list()
            for i in value:
                if isinstance(i, GoodInfo):
                    self._goods_infos.append(i)
                else:
                    self._goods_infos.append(GoodInfo.from_alipay_dict(i))
    @property
    def machine_type(self):
        return self._machine_type

    @machine_type.setter
    def machine_type(self, value):
        self._machine_type = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value
    @property
    def total_floors(self):
        return self._total_floors

    @total_floors.setter
    def total_floors(self, value):
        self._total_floors = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def weight_template(self):
        return self._weight_template

    @weight_template.setter
    def weight_template(self, value):
        if isinstance(value, list):
            self._weight_template = list()
            for i in value:
                if isinstance(i, WeightFloor):
                    self._weight_template.append(i)
                else:
                    self._weight_template.append(WeightFloor.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.goods_infos:
            if isinstance(self.goods_infos, list):
                for i in range(0, len(self.goods_infos)):
                    element = self.goods_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_infos[i] = element.to_alipay_dict()
            if hasattr(self.goods_infos, 'to_alipay_dict'):
                params['goods_infos'] = self.goods_infos.to_alipay_dict()
            else:
                params['goods_infos'] = self.goods_infos
        if self.machine_type:
            if hasattr(self.machine_type, 'to_alipay_dict'):
                params['machine_type'] = self.machine_type.to_alipay_dict()
            else:
                params['machine_type'] = self.machine_type
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        if self.total_floors:
            if hasattr(self.total_floors, 'to_alipay_dict'):
                params['total_floors'] = self.total_floors.to_alipay_dict()
            else:
                params['total_floors'] = self.total_floors
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.weight_template:
            if isinstance(self.weight_template, list):
                for i in range(0, len(self.weight_template)):
                    element = self.weight_template[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.weight_template[i] = element.to_alipay_dict()
            if hasattr(self.weight_template, 'to_alipay_dict'):
                params['weight_template'] = self.weight_template.to_alipay_dict()
            else:
                params['weight_template'] = self.weight_template
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogAftscvpayTransactionInitializeModel()
        if 'goods_infos' in d:
            o.goods_infos = d['goods_infos']
        if 'machine_type' in d:
            o.machine_type = d['machine_type']
        if 'scene' in d:
            o.scene = d['scene']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        if 'total_floors' in d:
            o.total_floors = d['total_floors']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        if 'type' in d:
            o.type = d['type']
        if 'uid' in d:
            o.uid = d['uid']
        if 'weight_template' in d:
            o.weight_template = d['weight_template']
        return o



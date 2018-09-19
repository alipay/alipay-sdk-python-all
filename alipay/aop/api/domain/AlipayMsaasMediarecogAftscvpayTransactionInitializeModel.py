#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodInfo import GoodInfo


class AlipayMsaasMediarecogAftscvpayTransactionInitializeModel(object):

    def __init__(self):
        self._goods_infos = None
        self._scene = None
        self._terminal_id = None
        self._transaction_id = None

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
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


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
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogAftscvpayTransactionInitializeModel()
        if 'goods_infos' in d:
            o.goods_infos = d['goods_infos']
        if 'scene' in d:
            o.scene = d['scene']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o



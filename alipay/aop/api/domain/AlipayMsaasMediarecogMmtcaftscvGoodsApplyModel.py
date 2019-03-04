#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApplyGoodsInfo import ApplyGoodsInfo


class AlipayMsaasMediarecogMmtcaftscvGoodsApplyModel(object):

    def __init__(self):
        self._batch_num = None
        self._goods_infos = None
        self._machine_type_id = None

    @property
    def batch_num(self):
        return self._batch_num

    @batch_num.setter
    def batch_num(self, value):
        self._batch_num = value
    @property
    def goods_infos(self):
        return self._goods_infos

    @goods_infos.setter
    def goods_infos(self, value):
        if isinstance(value, list):
            self._goods_infos = list()
            for i in value:
                if isinstance(i, ApplyGoodsInfo):
                    self._goods_infos.append(i)
                else:
                    self._goods_infos.append(ApplyGoodsInfo.from_alipay_dict(i))
    @property
    def machine_type_id(self):
        return self._machine_type_id

    @machine_type_id.setter
    def machine_type_id(self, value):
        self._machine_type_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_num:
            if hasattr(self.batch_num, 'to_alipay_dict'):
                params['batch_num'] = self.batch_num.to_alipay_dict()
            else:
                params['batch_num'] = self.batch_num
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
        o = AlipayMsaasMediarecogMmtcaftscvGoodsApplyModel()
        if 'batch_num' in d:
            o.batch_num = d['batch_num']
        if 'goods_infos' in d:
            o.goods_infos = d['goods_infos']
        if 'machine_type_id' in d:
            o.machine_type_id = d['machine_type_id']
        return o



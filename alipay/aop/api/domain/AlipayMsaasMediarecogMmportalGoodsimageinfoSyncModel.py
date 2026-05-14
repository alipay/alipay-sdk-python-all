#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsImageInfo import GoodsImageInfo


class AlipayMsaasMediarecogMmportalGoodsimageinfoSyncModel(object):

    def __init__(self):
        self._algorithm_id = None
        self._img_infos = None

    @property
    def algorithm_id(self):
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, value):
        self._algorithm_id = value
    @property
    def img_infos(self):
        return self._img_infos

    @img_infos.setter
    def img_infos(self, value):
        if isinstance(value, list):
            self._img_infos = list()
            for i in value:
                if isinstance(i, GoodsImageInfo):
                    self._img_infos.append(i)
                else:
                    self._img_infos.append(GoodsImageInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_id:
            if hasattr(self.algorithm_id, 'to_alipay_dict'):
                params['algorithm_id'] = self.algorithm_id.to_alipay_dict()
            else:
                params['algorithm_id'] = self.algorithm_id
        if self.img_infos:
            if isinstance(self.img_infos, list):
                for i in range(0, len(self.img_infos)):
                    element = self.img_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.img_infos[i] = element.to_alipay_dict()
            if hasattr(self.img_infos, 'to_alipay_dict'):
                params['img_infos'] = self.img_infos.to_alipay_dict()
            else:
                params['img_infos'] = self.img_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmportalGoodsimageinfoSyncModel()
        if 'algorithm_id' in d:
            o.algorithm_id = d['algorithm_id']
        if 'img_infos' in d:
            o.img_infos = d['img_infos']
        return o



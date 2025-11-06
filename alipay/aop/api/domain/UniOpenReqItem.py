#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UniOpenReqItemDetailInfos import UniOpenReqItemDetailInfos


class UniOpenReqItem(object):

    def __init__(self):
        self._detail_infos = None
        self._open_type = None

    @property
    def detail_infos(self):
        return self._detail_infos

    @detail_infos.setter
    def detail_infos(self, value):
        if isinstance(value, UniOpenReqItemDetailInfos):
            self._detail_infos = value
        else:
            self._detail_infos = UniOpenReqItemDetailInfos.from_alipay_dict(value)
    @property
    def open_type(self):
        return self._open_type

    @open_type.setter
    def open_type(self, value):
        self._open_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_infos:
            if hasattr(self.detail_infos, 'to_alipay_dict'):
                params['detail_infos'] = self.detail_infos.to_alipay_dict()
            else:
                params['detail_infos'] = self.detail_infos
        if self.open_type:
            if hasattr(self.open_type, 'to_alipay_dict'):
                params['open_type'] = self.open_type.to_alipay_dict()
            else:
                params['open_type'] = self.open_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UniOpenReqItem()
        if 'detail_infos' in d:
            o.detail_infos = d['detail_infos']
        if 'open_type' in d:
            o.open_type = d['open_type']
        return o



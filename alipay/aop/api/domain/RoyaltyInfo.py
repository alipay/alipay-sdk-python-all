#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoyaltyDetailInfos import RoyaltyDetailInfos


class RoyaltyInfo(object):

    def __init__(self):
        self._royalty_detail_infos = None
        self._royalty_type = None

    @property
    def royalty_detail_infos(self):
        return self._royalty_detail_infos

    @royalty_detail_infos.setter
    def royalty_detail_infos(self, value):
        if isinstance(value, list):
            self._royalty_detail_infos = list()
            for i in value:
                if isinstance(i, RoyaltyDetailInfos):
                    self._royalty_detail_infos.append(i)
                else:
                    self._royalty_detail_infos.append(RoyaltyDetailInfos.from_alipay_dict(i))
    @property
    def royalty_type(self):
        return self._royalty_type

    @royalty_type.setter
    def royalty_type(self, value):
        self._royalty_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.royalty_detail_infos:
            if isinstance(self.royalty_detail_infos, list):
                for i in range(0, len(self.royalty_detail_infos)):
                    element = self.royalty_detail_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_detail_infos[i] = element.to_alipay_dict()
            if hasattr(self.royalty_detail_infos, 'to_alipay_dict'):
                params['royalty_detail_infos'] = self.royalty_detail_infos.to_alipay_dict()
            else:
                params['royalty_detail_infos'] = self.royalty_detail_infos
        if self.royalty_type:
            if hasattr(self.royalty_type, 'to_alipay_dict'):
                params['royalty_type'] = self.royalty_type.to_alipay_dict()
            else:
                params['royalty_type'] = self.royalty_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoyaltyInfo()
        if 'royalty_detail_infos' in d:
            o.royalty_detail_infos = d['royalty_detail_infos']
        if 'royalty_type' in d:
            o.royalty_type = d['royalty_type']
        return o



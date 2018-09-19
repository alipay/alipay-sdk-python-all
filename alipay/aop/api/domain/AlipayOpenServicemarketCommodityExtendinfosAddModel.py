#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommodityPublicExtInfos import CommodityPublicExtInfos


class AlipayOpenServicemarketCommodityExtendinfosAddModel(object):

    def __init__(self):
        self._commodity_ext_infos = None
        self._commodity_id = None
        self._user_id = None

    @property
    def commodity_ext_infos(self):
        return self._commodity_ext_infos

    @commodity_ext_infos.setter
    def commodity_ext_infos(self, value):
        if isinstance(value, list):
            self._commodity_ext_infos = list()
            for i in value:
                if isinstance(i, CommodityPublicExtInfos):
                    self._commodity_ext_infos.append(i)
                else:
                    self._commodity_ext_infos.append(CommodityPublicExtInfos.from_alipay_dict(i))
    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_ext_infos:
            if isinstance(self.commodity_ext_infos, list):
                for i in range(0, len(self.commodity_ext_infos)):
                    element = self.commodity_ext_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commodity_ext_infos[i] = element.to_alipay_dict()
            if hasattr(self.commodity_ext_infos, 'to_alipay_dict'):
                params['commodity_ext_infos'] = self.commodity_ext_infos.to_alipay_dict()
            else:
                params['commodity_ext_infos'] = self.commodity_ext_infos
        if self.commodity_id:
            if hasattr(self.commodity_id, 'to_alipay_dict'):
                params['commodity_id'] = self.commodity_id.to_alipay_dict()
            else:
                params['commodity_id'] = self.commodity_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketCommodityExtendinfosAddModel()
        if 'commodity_ext_infos' in d:
            o.commodity_ext_infos = d['commodity_ext_infos']
        if 'commodity_id' in d:
            o.commodity_id = d['commodity_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



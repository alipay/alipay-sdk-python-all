#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.EnvInfo import EnvInfo
from alipay.aop.api.domain.ItemDetail import ItemDetail


class AlipayBusinessOrderConsultModel(object):

    def __init__(self):
        self._buyer_identity = None
        self._env_info = None
        self._item_list = None

    @property
    def buyer_identity(self):
        return self._buyer_identity

    @buyer_identity.setter
    def buyer_identity(self, value):
        if isinstance(value, UserIdentity):
            self._buyer_identity = value
        else:
            self._buyer_identity = UserIdentity.from_alipay_dict(value)
    @property
    def env_info(self):
        return self._env_info

    @env_info.setter
    def env_info(self, value):
        if isinstance(value, EnvInfo):
            self._env_info = value
        else:
            self._env_info = EnvInfo.from_alipay_dict(value)
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ItemDetail):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ItemDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_identity:
            if hasattr(self.buyer_identity, 'to_alipay_dict'):
                params['buyer_identity'] = self.buyer_identity.to_alipay_dict()
            else:
                params['buyer_identity'] = self.buyer_identity
        if self.env_info:
            if hasattr(self.env_info, 'to_alipay_dict'):
                params['env_info'] = self.env_info.to_alipay_dict()
            else:
                params['env_info'] = self.env_info
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessOrderConsultModel()
        if 'buyer_identity' in d:
            o.buyer_identity = d['buyer_identity']
        if 'env_info' in d:
            o.env_info = d['env_info']
        if 'item_list' in d:
            o.item_list = d['item_list']
        return o



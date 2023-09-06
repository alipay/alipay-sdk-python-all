#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MpcItemVO import MpcItemVO


class TechriskInnovateMpcpromoItemSyncModel(object):

    def __init__(self):
        self._auth_app_id = None
        self._item_list = None

    @property
    def auth_app_id(self):
        return self._auth_app_id

    @auth_app_id.setter
    def auth_app_id(self, value):
        self._auth_app_id = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, MpcItemVO):
                    self._item_list.append(i)
                else:
                    self._item_list.append(MpcItemVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.auth_app_id:
            if hasattr(self.auth_app_id, 'to_alipay_dict'):
                params['auth_app_id'] = self.auth_app_id.to_alipay_dict()
            else:
                params['auth_app_id'] = self.auth_app_id
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
        o = TechriskInnovateMpcpromoItemSyncModel()
        if 'auth_app_id' in d:
            o.auth_app_id = d['auth_app_id']
        if 'item_list' in d:
            o.item_list = d['item_list']
        return o



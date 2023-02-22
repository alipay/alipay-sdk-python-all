#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LmDeleteItemList import LmDeleteItemList


class MybankMarketingCampaignBkpromoguardbaseLmitemdeleteSyncModel(object):

    def __init__(self):
        self._biz_id = None
        self._item_id_list = None
        self._request_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def item_id_list(self):
        return self._item_id_list

    @item_id_list.setter
    def item_id_list(self, value):
        if isinstance(value, LmDeleteItemList):
            self._item_id_list = value
        else:
            self._item_id_list = LmDeleteItemList.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.item_id_list:
            if hasattr(self.item_id_list, 'to_alipay_dict'):
                params['item_id_list'] = self.item_id_list.to_alipay_dict()
            else:
                params['item_id_list'] = self.item_id_list
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankMarketingCampaignBkpromoguardbaseLmitemdeleteSyncModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o



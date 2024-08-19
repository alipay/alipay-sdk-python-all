#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemModifyOutItemInfo import AppItemModifyOutItemInfo


class VoucherAvailableModifyAppItemInfo(object):

    def __init__(self):
        self._app_item_out_item_info = None
        self._item_id = None

    @property
    def app_item_out_item_info(self):
        return self._app_item_out_item_info

    @app_item_out_item_info.setter
    def app_item_out_item_info(self, value):
        if isinstance(value, AppItemModifyOutItemInfo):
            self._app_item_out_item_info = value
        else:
            self._app_item_out_item_info = AppItemModifyOutItemInfo.from_alipay_dict(value)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_out_item_info:
            if hasattr(self.app_item_out_item_info, 'to_alipay_dict'):
                params['app_item_out_item_info'] = self.app_item_out_item_info.to_alipay_dict()
            else:
                params['app_item_out_item_info'] = self.app_item_out_item_info
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableModifyAppItemInfo()
        if 'app_item_out_item_info' in d:
            o.app_item_out_item_info = d['app_item_out_item_info']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o



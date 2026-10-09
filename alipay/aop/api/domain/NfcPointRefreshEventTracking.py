#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NfcPointRefreshEventTracking(object):

    def __init__(self):
        self._atmosphere = None
        self._biz_tid = None
        self._camp_id = None
        self._camp_ids = None
        self._camp_type = None
        self._item_type = None
        self._scheme_id = None
        self._ui_type = None

    @property
    def atmosphere(self):
        return self._atmosphere

    @atmosphere.setter
    def atmosphere(self, value):
        self._atmosphere = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def camp_ids(self):
        return self._camp_ids

    @camp_ids.setter
    def camp_ids(self, value):
        if isinstance(value, list):
            self._camp_ids = list()
            for i in value:
                self._camp_ids.append(i)
    @property
    def camp_type(self):
        return self._camp_type

    @camp_type.setter
    def camp_type(self, value):
        self._camp_type = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def scheme_id(self):
        return self._scheme_id

    @scheme_id.setter
    def scheme_id(self, value):
        self._scheme_id = value
    @property
    def ui_type(self):
        return self._ui_type

    @ui_type.setter
    def ui_type(self, value):
        self._ui_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.atmosphere:
            if hasattr(self.atmosphere, 'to_alipay_dict'):
                params['atmosphere'] = self.atmosphere.to_alipay_dict()
            else:
                params['atmosphere'] = self.atmosphere
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.camp_ids:
            if isinstance(self.camp_ids, list):
                for i in range(0, len(self.camp_ids)):
                    element = self.camp_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.camp_ids[i] = element.to_alipay_dict()
            if hasattr(self.camp_ids, 'to_alipay_dict'):
                params['camp_ids'] = self.camp_ids.to_alipay_dict()
            else:
                params['camp_ids'] = self.camp_ids
        if self.camp_type:
            if hasattr(self.camp_type, 'to_alipay_dict'):
                params['camp_type'] = self.camp_type.to_alipay_dict()
            else:
                params['camp_type'] = self.camp_type
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.scheme_id:
            if hasattr(self.scheme_id, 'to_alipay_dict'):
                params['scheme_id'] = self.scheme_id.to_alipay_dict()
            else:
                params['scheme_id'] = self.scheme_id
        if self.ui_type:
            if hasattr(self.ui_type, 'to_alipay_dict'):
                params['ui_type'] = self.ui_type.to_alipay_dict()
            else:
                params['ui_type'] = self.ui_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NfcPointRefreshEventTracking()
        if 'atmosphere' in d:
            o.atmosphere = d['atmosphere']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'camp_ids' in d:
            o.camp_ids = d['camp_ids']
        if 'camp_type' in d:
            o.camp_type = d['camp_type']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'scheme_id' in d:
            o.scheme_id = d['scheme_id']
        if 'ui_type' in d:
            o.ui_type = d['ui_type']
        return o



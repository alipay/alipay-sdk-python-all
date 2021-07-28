#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WaitRateAlgoItem import WaitRateAlgoItem


class AlipayOpenAppAraterWaitratealgorankQueryModel(object):

    def __init__(self):
        self._ext_info = None
        self._havana_id = None
        self._item_list = None
        self._route_uid = None
        self._session_click_item_ids = None
        self._session_expo_item_ids = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, WaitRateAlgoItem):
                    self._item_list.append(i)
                else:
                    self._item_list.append(WaitRateAlgoItem.from_alipay_dict(i))
    @property
    def route_uid(self):
        return self._route_uid

    @route_uid.setter
    def route_uid(self, value):
        self._route_uid = value
    @property
    def session_click_item_ids(self):
        return self._session_click_item_ids

    @session_click_item_ids.setter
    def session_click_item_ids(self, value):
        if isinstance(value, list):
            self._session_click_item_ids = list()
            for i in value:
                self._session_click_item_ids.append(i)
    @property
    def session_expo_item_ids(self):
        return self._session_expo_item_ids

    @session_expo_item_ids.setter
    def session_expo_item_ids(self, value):
        if isinstance(value, list):
            self._session_expo_item_ids = list()
            for i in value:
                self._session_expo_item_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.havana_id:
            if hasattr(self.havana_id, 'to_alipay_dict'):
                params['havana_id'] = self.havana_id.to_alipay_dict()
            else:
                params['havana_id'] = self.havana_id
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
        if self.route_uid:
            if hasattr(self.route_uid, 'to_alipay_dict'):
                params['route_uid'] = self.route_uid.to_alipay_dict()
            else:
                params['route_uid'] = self.route_uid
        if self.session_click_item_ids:
            if isinstance(self.session_click_item_ids, list):
                for i in range(0, len(self.session_click_item_ids)):
                    element = self.session_click_item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.session_click_item_ids[i] = element.to_alipay_dict()
            if hasattr(self.session_click_item_ids, 'to_alipay_dict'):
                params['session_click_item_ids'] = self.session_click_item_ids.to_alipay_dict()
            else:
                params['session_click_item_ids'] = self.session_click_item_ids
        if self.session_expo_item_ids:
            if isinstance(self.session_expo_item_ids, list):
                for i in range(0, len(self.session_expo_item_ids)):
                    element = self.session_expo_item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.session_expo_item_ids[i] = element.to_alipay_dict()
            if hasattr(self.session_expo_item_ids, 'to_alipay_dict'):
                params['session_expo_item_ids'] = self.session_expo_item_ids.to_alipay_dict()
            else:
                params['session_expo_item_ids'] = self.session_expo_item_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppAraterWaitratealgorankQueryModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'havana_id' in d:
            o.havana_id = d['havana_id']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'route_uid' in d:
            o.route_uid = d['route_uid']
        if 'session_click_item_ids' in d:
            o.session_click_item_ids = d['session_click_item_ids']
        if 'session_expo_item_ids' in d:
            o.session_expo_item_ids = d['session_expo_item_ids']
        return o



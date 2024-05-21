#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TipsAndUrl import TipsAndUrl


class ItemEnrollFreezeContent(object):

    def __init__(self):
        self._in_live = None
        self._item_enroll_flag = None
        self._no_edit_key_list = None
        self._no_edit_tip_list = None
        self._tips_and_urls = None

    @property
    def in_live(self):
        return self._in_live

    @in_live.setter
    def in_live(self, value):
        self._in_live = value
    @property
    def item_enroll_flag(self):
        return self._item_enroll_flag

    @item_enroll_flag.setter
    def item_enroll_flag(self, value):
        self._item_enroll_flag = value
    @property
    def no_edit_key_list(self):
        return self._no_edit_key_list

    @no_edit_key_list.setter
    def no_edit_key_list(self, value):
        if isinstance(value, list):
            self._no_edit_key_list = list()
            for i in value:
                self._no_edit_key_list.append(i)
    @property
    def no_edit_tip_list(self):
        return self._no_edit_tip_list

    @no_edit_tip_list.setter
    def no_edit_tip_list(self, value):
        if isinstance(value, list):
            self._no_edit_tip_list = list()
            for i in value:
                self._no_edit_tip_list.append(i)
    @property
    def tips_and_urls(self):
        return self._tips_and_urls

    @tips_and_urls.setter
    def tips_and_urls(self, value):
        if isinstance(value, list):
            self._tips_and_urls = list()
            for i in value:
                if isinstance(i, TipsAndUrl):
                    self._tips_and_urls.append(i)
                else:
                    self._tips_and_urls.append(TipsAndUrl.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.in_live:
            if hasattr(self.in_live, 'to_alipay_dict'):
                params['in_live'] = self.in_live.to_alipay_dict()
            else:
                params['in_live'] = self.in_live
        if self.item_enroll_flag:
            if hasattr(self.item_enroll_flag, 'to_alipay_dict'):
                params['item_enroll_flag'] = self.item_enroll_flag.to_alipay_dict()
            else:
                params['item_enroll_flag'] = self.item_enroll_flag
        if self.no_edit_key_list:
            if isinstance(self.no_edit_key_list, list):
                for i in range(0, len(self.no_edit_key_list)):
                    element = self.no_edit_key_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.no_edit_key_list[i] = element.to_alipay_dict()
            if hasattr(self.no_edit_key_list, 'to_alipay_dict'):
                params['no_edit_key_list'] = self.no_edit_key_list.to_alipay_dict()
            else:
                params['no_edit_key_list'] = self.no_edit_key_list
        if self.no_edit_tip_list:
            if isinstance(self.no_edit_tip_list, list):
                for i in range(0, len(self.no_edit_tip_list)):
                    element = self.no_edit_tip_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.no_edit_tip_list[i] = element.to_alipay_dict()
            if hasattr(self.no_edit_tip_list, 'to_alipay_dict'):
                params['no_edit_tip_list'] = self.no_edit_tip_list.to_alipay_dict()
            else:
                params['no_edit_tip_list'] = self.no_edit_tip_list
        if self.tips_and_urls:
            if isinstance(self.tips_and_urls, list):
                for i in range(0, len(self.tips_and_urls)):
                    element = self.tips_and_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tips_and_urls[i] = element.to_alipay_dict()
            if hasattr(self.tips_and_urls, 'to_alipay_dict'):
                params['tips_and_urls'] = self.tips_and_urls.to_alipay_dict()
            else:
                params['tips_and_urls'] = self.tips_and_urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemEnrollFreezeContent()
        if 'in_live' in d:
            o.in_live = d['in_live']
        if 'item_enroll_flag' in d:
            o.item_enroll_flag = d['item_enroll_flag']
        if 'no_edit_key_list' in d:
            o.no_edit_key_list = d['no_edit_key_list']
        if 'no_edit_tip_list' in d:
            o.no_edit_tip_list = d['no_edit_tip_list']
        if 'tips_and_urls' in d:
            o.tips_and_urls = d['tips_and_urls']
        return o



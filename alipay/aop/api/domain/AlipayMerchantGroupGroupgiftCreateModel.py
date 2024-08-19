#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupGiftVO import GroupGiftVO


class AlipayMerchantGroupGroupgiftCreateModel(object):

    def __init__(self):
        self._group_gifts = None
        self._group_ids = None

    @property
    def group_gifts(self):
        return self._group_gifts

    @group_gifts.setter
    def group_gifts(self, value):
        if isinstance(value, list):
            self._group_gifts = list()
            for i in value:
                if isinstance(i, GroupGiftVO):
                    self._group_gifts.append(i)
                else:
                    self._group_gifts.append(GroupGiftVO.from_alipay_dict(i))
    @property
    def group_ids(self):
        return self._group_ids

    @group_ids.setter
    def group_ids(self, value):
        if isinstance(value, list):
            self._group_ids = list()
            for i in value:
                self._group_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.group_gifts:
            if isinstance(self.group_gifts, list):
                for i in range(0, len(self.group_gifts)):
                    element = self.group_gifts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_gifts[i] = element.to_alipay_dict()
            if hasattr(self.group_gifts, 'to_alipay_dict'):
                params['group_gifts'] = self.group_gifts.to_alipay_dict()
            else:
                params['group_gifts'] = self.group_gifts
        if self.group_ids:
            if isinstance(self.group_ids, list):
                for i in range(0, len(self.group_ids)):
                    element = self.group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_ids[i] = element.to_alipay_dict()
            if hasattr(self.group_ids, 'to_alipay_dict'):
                params['group_ids'] = self.group_ids.to_alipay_dict()
            else:
                params['group_ids'] = self.group_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupGroupgiftCreateModel()
        if 'group_gifts' in d:
            o.group_gifts = d['group_gifts']
        if 'group_ids' in d:
            o.group_ids = d['group_ids']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupNoticeModifyModel(object):

    def __init__(self):
        self._group_ids = None
        self._notice = None

    @property
    def group_ids(self):
        return self._group_ids

    @group_ids.setter
    def group_ids(self, value):
        if isinstance(value, list):
            self._group_ids = list()
            for i in value:
                self._group_ids.append(i)
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupNoticeModifyModel()
        if 'group_ids' in d:
            o.group_ids = d['group_ids']
        if 'notice' in d:
            o.notice = d['notice']
        return o



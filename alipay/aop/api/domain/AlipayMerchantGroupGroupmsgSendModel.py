#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupMessageVO import GroupMessageVO


class AlipayMerchantGroupGroupmsgSendModel(object):

    def __init__(self):
        self._at_all = None
        self._biz_id = None
        self._group_ids = None
        self._msg_data = None
        self._title = None

    @property
    def at_all(self):
        return self._at_all

    @at_all.setter
    def at_all(self, value):
        self._at_all = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
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
    def msg_data(self):
        return self._msg_data

    @msg_data.setter
    def msg_data(self, value):
        if isinstance(value, GroupMessageVO):
            self._msg_data = value
        else:
            self._msg_data = GroupMessageVO.from_alipay_dict(value)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.at_all:
            if hasattr(self.at_all, 'to_alipay_dict'):
                params['at_all'] = self.at_all.to_alipay_dict()
            else:
                params['at_all'] = self.at_all
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
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
        if self.msg_data:
            if hasattr(self.msg_data, 'to_alipay_dict'):
                params['msg_data'] = self.msg_data.to_alipay_dict()
            else:
                params['msg_data'] = self.msg_data
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupGroupmsgSendModel()
        if 'at_all' in d:
            o.at_all = d['at_all']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'group_ids' in d:
            o.group_ids = d['group_ids']
        if 'msg_data' in d:
            o.msg_data = d['msg_data']
        if 'title' in d:
            o.title = d['title']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizEntityId import BizEntityId


class AlipayCircularRentRoomAgentChatModel(object):

    def __init__(self):
        self._biz_entity_ids = None
        self._biz_type = None
        self._merchant_query_condition = None
        self._open_id = None
        self._out_session_id = None
        self._query_content = None
        self._user_id = None

    @property
    def biz_entity_ids(self):
        return self._biz_entity_ids

    @biz_entity_ids.setter
    def biz_entity_ids(self, value):
        if isinstance(value, list):
            self._biz_entity_ids = list()
            for i in value:
                if isinstance(i, BizEntityId):
                    self._biz_entity_ids.append(i)
                else:
                    self._biz_entity_ids.append(BizEntityId.from_alipay_dict(i))
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def merchant_query_condition(self):
        return self._merchant_query_condition

    @merchant_query_condition.setter
    def merchant_query_condition(self, value):
        self._merchant_query_condition = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_session_id(self):
        return self._out_session_id

    @out_session_id.setter
    def out_session_id(self, value):
        self._out_session_id = value
    @property
    def query_content(self):
        return self._query_content

    @query_content.setter
    def query_content(self, value):
        self._query_content = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_entity_ids:
            if isinstance(self.biz_entity_ids, list):
                for i in range(0, len(self.biz_entity_ids)):
                    element = self.biz_entity_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_entity_ids[i] = element.to_alipay_dict()
            if hasattr(self.biz_entity_ids, 'to_alipay_dict'):
                params['biz_entity_ids'] = self.biz_entity_ids.to_alipay_dict()
            else:
                params['biz_entity_ids'] = self.biz_entity_ids
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.merchant_query_condition:
            if hasattr(self.merchant_query_condition, 'to_alipay_dict'):
                params['merchant_query_condition'] = self.merchant_query_condition.to_alipay_dict()
            else:
                params['merchant_query_condition'] = self.merchant_query_condition
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_session_id:
            if hasattr(self.out_session_id, 'to_alipay_dict'):
                params['out_session_id'] = self.out_session_id.to_alipay_dict()
            else:
                params['out_session_id'] = self.out_session_id
        if self.query_content:
            if hasattr(self.query_content, 'to_alipay_dict'):
                params['query_content'] = self.query_content.to_alipay_dict()
            else:
                params['query_content'] = self.query_content
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCircularRentRoomAgentChatModel()
        if 'biz_entity_ids' in d:
            o.biz_entity_ids = d['biz_entity_ids']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'merchant_query_condition' in d:
            o.merchant_query_condition = d['merchant_query_condition']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_session_id' in d:
            o.out_session_id = d['out_session_id']
        if 'query_content' in d:
            o.query_content = d['query_content']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudNextbuilderAgentMessageQueryModel(object):

    def __init__(self):
        self._agent_id = None
        self._conversation_id = None
        self._from_source = None
        self._order = None
        self._order_by = None
        self._outer_user_id = None
        self._page_num = None
        self._page_size = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, value):
        self._conversation_id = value
    @property
    def from_source(self):
        return self._from_source

    @from_source.setter
    def from_source(self, value):
        self._from_source = value
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
    @property
    def order_by(self):
        return self._order_by

    @order_by.setter
    def order_by(self, value):
        self._order_by = value
    @property
    def outer_user_id(self):
        return self._outer_user_id

    @outer_user_id.setter
    def outer_user_id(self, value):
        self._outer_user_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.conversation_id:
            if hasattr(self.conversation_id, 'to_alipay_dict'):
                params['conversation_id'] = self.conversation_id.to_alipay_dict()
            else:
                params['conversation_id'] = self.conversation_id
        if self.from_source:
            if hasattr(self.from_source, 'to_alipay_dict'):
                params['from_source'] = self.from_source.to_alipay_dict()
            else:
                params['from_source'] = self.from_source
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.order_by:
            if hasattr(self.order_by, 'to_alipay_dict'):
                params['order_by'] = self.order_by.to_alipay_dict()
            else:
                params['order_by'] = self.order_by
        if self.outer_user_id:
            if hasattr(self.outer_user_id, 'to_alipay_dict'):
                params['outer_user_id'] = self.outer_user_id.to_alipay_dict()
            else:
                params['outer_user_id'] = self.outer_user_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudNextbuilderAgentMessageQueryModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'from_source' in d:
            o.from_source = d['from_source']
        if 'order' in d:
            o.order = d['order']
        if 'order_by' in d:
            o.order_by = d['order_by']
        if 'outer_user_id' in d:
            o.outer_user_id = d['outer_user_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o



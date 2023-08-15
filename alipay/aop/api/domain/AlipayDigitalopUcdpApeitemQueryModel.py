#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApeRecContext import ApeRecContext


class AlipayDigitalopUcdpApeitemQueryModel(object):

    def __init__(self):
        self._context = None
        self._custom_id = None
        self._exposed_item_list = None
        self._item_id_list = None
        self._open_id = None
        self._page_num = None
        self._page_size = None
        self._project_id = None
        self._relevant_id = None
        self._session_id = None
        self._user_id = None
        self._user_id_type = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        if isinstance(value, ApeRecContext):
            self._context = value
        else:
            self._context = ApeRecContext.from_alipay_dict(value)
    @property
    def custom_id(self):
        return self._custom_id

    @custom_id.setter
    def custom_id(self, value):
        self._custom_id = value
    @property
    def exposed_item_list(self):
        return self._exposed_item_list

    @exposed_item_list.setter
    def exposed_item_list(self, value):
        if isinstance(value, list):
            self._exposed_item_list = list()
            for i in value:
                self._exposed_item_list.append(i)
    @property
    def item_id_list(self):
        return self._item_id_list

    @item_id_list.setter
    def item_id_list(self, value):
        if isinstance(value, list):
            self._item_id_list = list()
            for i in value:
                self._item_id_list.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def relevant_id(self):
        return self._relevant_id

    @relevant_id.setter
    def relevant_id(self, value):
        self._relevant_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_type(self):
        return self._user_id_type

    @user_id_type.setter
    def user_id_type(self, value):
        self._user_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.custom_id:
            if hasattr(self.custom_id, 'to_alipay_dict'):
                params['custom_id'] = self.custom_id.to_alipay_dict()
            else:
                params['custom_id'] = self.custom_id
        if self.exposed_item_list:
            if isinstance(self.exposed_item_list, list):
                for i in range(0, len(self.exposed_item_list)):
                    element = self.exposed_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exposed_item_list[i] = element.to_alipay_dict()
            if hasattr(self.exposed_item_list, 'to_alipay_dict'):
                params['exposed_item_list'] = self.exposed_item_list.to_alipay_dict()
            else:
                params['exposed_item_list'] = self.exposed_item_list
        if self.item_id_list:
            if isinstance(self.item_id_list, list):
                for i in range(0, len(self.item_id_list)):
                    element = self.item_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_id_list[i] = element.to_alipay_dict()
            if hasattr(self.item_id_list, 'to_alipay_dict'):
                params['item_id_list'] = self.item_id_list.to_alipay_dict()
            else:
                params['item_id_list'] = self.item_id_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.relevant_id:
            if hasattr(self.relevant_id, 'to_alipay_dict'):
                params['relevant_id'] = self.relevant_id.to_alipay_dict()
            else:
                params['relevant_id'] = self.relevant_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_type:
            if hasattr(self.user_id_type, 'to_alipay_dict'):
                params['user_id_type'] = self.user_id_type.to_alipay_dict()
            else:
                params['user_id_type'] = self.user_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalopUcdpApeitemQueryModel()
        if 'context' in d:
            o.context = d['context']
        if 'custom_id' in d:
            o.custom_id = d['custom_id']
        if 'exposed_item_list' in d:
            o.exposed_item_list = d['exposed_item_list']
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'relevant_id' in d:
            o.relevant_id = d['relevant_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_type' in d:
            o.user_id_type = d['user_id_type']
        return o



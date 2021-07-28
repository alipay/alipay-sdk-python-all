#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmAgentQueryModel(object):

    def __init__(self):
        self._answering_mode = None
        self._ccs_instance_id = None
        self._chat_ext_group_ids = None
        self._chat_group_ids = None
        self._chat_level_ids = None
        self._email = None
        self._hotline_group_ids = None
        self._page_num = None
        self._page_size = None
        self._real_name = None
        self._role_ids = None

    @property
    def answering_mode(self):
        return self._answering_mode

    @answering_mode.setter
    def answering_mode(self, value):
        self._answering_mode = value
    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def chat_ext_group_ids(self):
        return self._chat_ext_group_ids

    @chat_ext_group_ids.setter
    def chat_ext_group_ids(self, value):
        if isinstance(value, list):
            self._chat_ext_group_ids = list()
            for i in value:
                self._chat_ext_group_ids.append(i)
    @property
    def chat_group_ids(self):
        return self._chat_group_ids

    @chat_group_ids.setter
    def chat_group_ids(self, value):
        if isinstance(value, list):
            self._chat_group_ids = list()
            for i in value:
                self._chat_group_ids.append(i)
    @property
    def chat_level_ids(self):
        return self._chat_level_ids

    @chat_level_ids.setter
    def chat_level_ids(self, value):
        if isinstance(value, list):
            self._chat_level_ids = list()
            for i in value:
                self._chat_level_ids.append(i)
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def hotline_group_ids(self):
        return self._hotline_group_ids

    @hotline_group_ids.setter
    def hotline_group_ids(self, value):
        if isinstance(value, list):
            self._hotline_group_ids = list()
            for i in value:
                self._hotline_group_ids.append(i)
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
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def role_ids(self):
        return self._role_ids

    @role_ids.setter
    def role_ids(self, value):
        if isinstance(value, list):
            self._role_ids = list()
            for i in value:
                self._role_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.answering_mode:
            if hasattr(self.answering_mode, 'to_alipay_dict'):
                params['answering_mode'] = self.answering_mode.to_alipay_dict()
            else:
                params['answering_mode'] = self.answering_mode
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.chat_ext_group_ids:
            if isinstance(self.chat_ext_group_ids, list):
                for i in range(0, len(self.chat_ext_group_ids)):
                    element = self.chat_ext_group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.chat_ext_group_ids[i] = element.to_alipay_dict()
            if hasattr(self.chat_ext_group_ids, 'to_alipay_dict'):
                params['chat_ext_group_ids'] = self.chat_ext_group_ids.to_alipay_dict()
            else:
                params['chat_ext_group_ids'] = self.chat_ext_group_ids
        if self.chat_group_ids:
            if isinstance(self.chat_group_ids, list):
                for i in range(0, len(self.chat_group_ids)):
                    element = self.chat_group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.chat_group_ids[i] = element.to_alipay_dict()
            if hasattr(self.chat_group_ids, 'to_alipay_dict'):
                params['chat_group_ids'] = self.chat_group_ids.to_alipay_dict()
            else:
                params['chat_group_ids'] = self.chat_group_ids
        if self.chat_level_ids:
            if isinstance(self.chat_level_ids, list):
                for i in range(0, len(self.chat_level_ids)):
                    element = self.chat_level_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.chat_level_ids[i] = element.to_alipay_dict()
            if hasattr(self.chat_level_ids, 'to_alipay_dict'):
                params['chat_level_ids'] = self.chat_level_ids.to_alipay_dict()
            else:
                params['chat_level_ids'] = self.chat_level_ids
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.hotline_group_ids:
            if isinstance(self.hotline_group_ids, list):
                for i in range(0, len(self.hotline_group_ids)):
                    element = self.hotline_group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hotline_group_ids[i] = element.to_alipay_dict()
            if hasattr(self.hotline_group_ids, 'to_alipay_dict'):
                params['hotline_group_ids'] = self.hotline_group_ids.to_alipay_dict()
            else:
                params['hotline_group_ids'] = self.hotline_group_ids
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
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.role_ids:
            if isinstance(self.role_ids, list):
                for i in range(0, len(self.role_ids)):
                    element = self.role_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_ids[i] = element.to_alipay_dict()
            if hasattr(self.role_ids, 'to_alipay_dict'):
                params['role_ids'] = self.role_ids.to_alipay_dict()
            else:
                params['role_ids'] = self.role_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmAgentQueryModel()
        if 'answering_mode' in d:
            o.answering_mode = d['answering_mode']
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'chat_ext_group_ids' in d:
            o.chat_ext_group_ids = d['chat_ext_group_ids']
        if 'chat_group_ids' in d:
            o.chat_group_ids = d['chat_group_ids']
        if 'chat_level_ids' in d:
            o.chat_level_ids = d['chat_level_ids']
        if 'email' in d:
            o.email = d['email']
        if 'hotline_group_ids' in d:
            o.hotline_group_ids = d['hotline_group_ids']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'role_ids' in d:
            o.role_ids = d['role_ids']
        return o



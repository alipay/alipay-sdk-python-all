#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicMsgKeyword import PublicMsgKeyword
from alipay.aop.api.domain.PublicMsgKeyword import PublicMsgKeyword


class AlipayOpenPublicTemplateMessageAddModel(object):

    def __init__(self):
        self._keyword_list = None
        self._lib_code = None
        self._opt_list = None

    @property
    def keyword_list(self):
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, value):
        if isinstance(value, list):
            self._keyword_list = list()
            for i in value:
                if isinstance(i, PublicMsgKeyword):
                    self._keyword_list.append(i)
                else:
                    self._keyword_list.append(PublicMsgKeyword.from_alipay_dict(i))
    @property
    def lib_code(self):
        return self._lib_code

    @lib_code.setter
    def lib_code(self, value):
        self._lib_code = value
    @property
    def opt_list(self):
        return self._opt_list

    @opt_list.setter
    def opt_list(self, value):
        if isinstance(value, list):
            self._opt_list = list()
            for i in value:
                if isinstance(i, PublicMsgKeyword):
                    self._opt_list.append(i)
                else:
                    self._opt_list.append(PublicMsgKeyword.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.keyword_list:
            if isinstance(self.keyword_list, list):
                for i in range(0, len(self.keyword_list)):
                    element = self.keyword_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keyword_list[i] = element.to_alipay_dict()
            if hasattr(self.keyword_list, 'to_alipay_dict'):
                params['keyword_list'] = self.keyword_list.to_alipay_dict()
            else:
                params['keyword_list'] = self.keyword_list
        if self.lib_code:
            if hasattr(self.lib_code, 'to_alipay_dict'):
                params['lib_code'] = self.lib_code.to_alipay_dict()
            else:
                params['lib_code'] = self.lib_code
        if self.opt_list:
            if isinstance(self.opt_list, list):
                for i in range(0, len(self.opt_list)):
                    element = self.opt_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.opt_list[i] = element.to_alipay_dict()
            if hasattr(self.opt_list, 'to_alipay_dict'):
                params['opt_list'] = self.opt_list.to_alipay_dict()
            else:
                params['opt_list'] = self.opt_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicTemplateMessageAddModel()
        if 'keyword_list' in d:
            o.keyword_list = d['keyword_list']
        if 'lib_code' in d:
            o.lib_code = d['lib_code']
        if 'opt_list' in d:
            o.opt_list = d['opt_list']
        return o



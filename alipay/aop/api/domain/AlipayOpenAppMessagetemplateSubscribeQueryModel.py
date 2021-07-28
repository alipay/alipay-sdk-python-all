#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppMessagetemplateSubscribeQueryModel(object):

    def __init__(self):
        self._template_id_list = None
        self._user_id = None

    @property
    def template_id_list(self):
        return self._template_id_list

    @template_id_list.setter
    def template_id_list(self, value):
        if isinstance(value, list):
            self._template_id_list = list()
            for i in value:
                self._template_id_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.template_id_list:
            if isinstance(self.template_id_list, list):
                for i in range(0, len(self.template_id_list)):
                    element = self.template_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_id_list[i] = element.to_alipay_dict()
            if hasattr(self.template_id_list, 'to_alipay_dict'):
                params['template_id_list'] = self.template_id_list.to_alipay_dict()
            else:
                params['template_id_list'] = self.template_id_list
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
        o = AlipayOpenAppMessagetemplateSubscribeQueryModel()
        if 'template_id_list' in d:
            o.template_id_list = d['template_id_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



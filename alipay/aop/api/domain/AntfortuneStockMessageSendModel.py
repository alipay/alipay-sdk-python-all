#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Kv import Kv


class AntfortuneStockMessageSendModel(object):

    def __init__(self):
        self._agreement_no = None
        self._category = None
        self._msg_id = None
        self._param = None
        self._sub_category = None
        self._template = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        if isinstance(value, list):
            self._param = list()
            for i in value:
                if isinstance(i, Kv):
                    self._param.append(i)
                else:
                    self._param.append(Kv.from_alipay_dict(i))
    @property
    def sub_category(self):
        return self._sub_category

    @sub_category.setter
    def sub_category(self, value):
        self._sub_category = value
    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        self._template = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.param:
            if isinstance(self.param, list):
                for i in range(0, len(self.param)):
                    element = self.param[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.param[i] = element.to_alipay_dict()
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        if self.sub_category:
            if hasattr(self.sub_category, 'to_alipay_dict'):
                params['sub_category'] = self.sub_category.to_alipay_dict()
            else:
                params['sub_category'] = self.sub_category
        if self.template:
            if hasattr(self.template, 'to_alipay_dict'):
                params['template'] = self.template.to_alipay_dict()
            else:
                params['template'] = self.template
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockMessageSendModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'category' in d:
            o.category = d['category']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'param' in d:
            o.param = d['param']
        if 'sub_category' in d:
            o.sub_category = d['sub_category']
        if 'template' in d:
            o.template = d['template']
        return o



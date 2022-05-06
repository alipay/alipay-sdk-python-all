#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MsgContent import MsgContent
from alipay.aop.api.domain.MsgDynamicData import MsgDynamicData


class AlipayEcoMycarSystemTemplatemessageSendModel(object):

    def __init__(self):
        self._msg_content = None
        self._msg_dynamic_datas = None
        self._msg_id = None
        self._msg_subject_id = None
        self._msg_type = None
        self._params = None
        self._user_id = None

    @property
    def msg_content(self):
        return self._msg_content

    @msg_content.setter
    def msg_content(self, value):
        if isinstance(value, MsgContent):
            self._msg_content = value
        else:
            self._msg_content = MsgContent.from_alipay_dict(value)
    @property
    def msg_dynamic_datas(self):
        return self._msg_dynamic_datas

    @msg_dynamic_datas.setter
    def msg_dynamic_datas(self, value):
        if isinstance(value, list):
            self._msg_dynamic_datas = list()
            for i in value:
                if isinstance(i, MsgDynamicData):
                    self._msg_dynamic_datas.append(i)
                else:
                    self._msg_dynamic_datas.append(MsgDynamicData.from_alipay_dict(i))
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def msg_subject_id(self):
        return self._msg_subject_id

    @msg_subject_id.setter
    def msg_subject_id(self, value):
        self._msg_subject_id = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg_content:
            if hasattr(self.msg_content, 'to_alipay_dict'):
                params['msg_content'] = self.msg_content.to_alipay_dict()
            else:
                params['msg_content'] = self.msg_content
        if self.msg_dynamic_datas:
            if isinstance(self.msg_dynamic_datas, list):
                for i in range(0, len(self.msg_dynamic_datas)):
                    element = self.msg_dynamic_datas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.msg_dynamic_datas[i] = element.to_alipay_dict()
            if hasattr(self.msg_dynamic_datas, 'to_alipay_dict'):
                params['msg_dynamic_datas'] = self.msg_dynamic_datas.to_alipay_dict()
            else:
                params['msg_dynamic_datas'] = self.msg_dynamic_datas
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.msg_subject_id:
            if hasattr(self.msg_subject_id, 'to_alipay_dict'):
                params['msg_subject_id'] = self.msg_subject_id.to_alipay_dict()
            else:
                params['msg_subject_id'] = self.msg_subject_id
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
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
        o = AlipayEcoMycarSystemTemplatemessageSendModel()
        if 'msg_content' in d:
            o.msg_content = d['msg_content']
        if 'msg_dynamic_datas' in d:
            o.msg_dynamic_datas = d['msg_dynamic_datas']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'msg_subject_id' in d:
            o.msg_subject_id = d['msg_subject_id']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'params' in d:
            o.params = d['params']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



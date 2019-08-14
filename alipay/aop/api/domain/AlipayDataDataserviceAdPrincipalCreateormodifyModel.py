#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OuterAttachment import OuterAttachment


class AlipayDataDataserviceAdPrincipalCreateormodifyModel(object):

    def __init__(self):
        self._alipay_pid = None
        self._attachment_list = None
        self._biz_token = None
        self._principal_id = None
        self._trade_id = None
        self._user_id = None

    @property
    def alipay_pid(self):
        return self._alipay_pid

    @alipay_pid.setter
    def alipay_pid(self, value):
        self._alipay_pid = value
    @property
    def attachment_list(self):
        return self._attachment_list

    @attachment_list.setter
    def attachment_list(self, value):
        if isinstance(value, list):
            self._attachment_list = list()
            for i in value:
                if isinstance(i, OuterAttachment):
                    self._attachment_list.append(i)
                else:
                    self._attachment_list.append(OuterAttachment.from_alipay_dict(i))
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pid:
            if hasattr(self.alipay_pid, 'to_alipay_dict'):
                params['alipay_pid'] = self.alipay_pid.to_alipay_dict()
            else:
                params['alipay_pid'] = self.alipay_pid
        if self.attachment_list:
            if isinstance(self.attachment_list, list):
                for i in range(0, len(self.attachment_list)):
                    element = self.attachment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachment_list[i] = element.to_alipay_dict()
            if hasattr(self.attachment_list, 'to_alipay_dict'):
                params['attachment_list'] = self.attachment_list.to_alipay_dict()
            else:
                params['attachment_list'] = self.attachment_list
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
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
        o = AlipayDataDataserviceAdPrincipalCreateormodifyModel()
        if 'alipay_pid' in d:
            o.alipay_pid = d['alipay_pid']
        if 'attachment_list' in d:
            o.attachment_list = d['attachment_list']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



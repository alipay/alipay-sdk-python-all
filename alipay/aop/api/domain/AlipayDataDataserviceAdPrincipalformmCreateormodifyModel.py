#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlimamaPrincipalExtendInfo import AlimamaPrincipalExtendInfo


class AlipayDataDataserviceAdPrincipalformmCreateormodifyModel(object):

    def __init__(self):
        self._alipay_oid = None
        self._biz_token = None
        self._extend_info = None
        self._first_trade_id = None
        self._principal_oid = None
        self._principal_tag = None
        self._second_trade_id = None

    @property
    def alipay_oid(self):
        return self._alipay_oid

    @alipay_oid.setter
    def alipay_oid(self, value):
        self._alipay_oid = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        if isinstance(value, AlimamaPrincipalExtendInfo):
            self._extend_info = value
        else:
            self._extend_info = AlimamaPrincipalExtendInfo.from_alipay_dict(value)
    @property
    def first_trade_id(self):
        return self._first_trade_id

    @first_trade_id.setter
    def first_trade_id(self, value):
        self._first_trade_id = value
    @property
    def principal_oid(self):
        return self._principal_oid

    @principal_oid.setter
    def principal_oid(self, value):
        self._principal_oid = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def second_trade_id(self):
        return self._second_trade_id

    @second_trade_id.setter
    def second_trade_id(self, value):
        self._second_trade_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_oid:
            if hasattr(self.alipay_oid, 'to_alipay_dict'):
                params['alipay_oid'] = self.alipay_oid.to_alipay_dict()
            else:
                params['alipay_oid'] = self.alipay_oid
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.first_trade_id:
            if hasattr(self.first_trade_id, 'to_alipay_dict'):
                params['first_trade_id'] = self.first_trade_id.to_alipay_dict()
            else:
                params['first_trade_id'] = self.first_trade_id
        if self.principal_oid:
            if hasattr(self.principal_oid, 'to_alipay_dict'):
                params['principal_oid'] = self.principal_oid.to_alipay_dict()
            else:
                params['principal_oid'] = self.principal_oid
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.second_trade_id:
            if hasattr(self.second_trade_id, 'to_alipay_dict'):
                params['second_trade_id'] = self.second_trade_id.to_alipay_dict()
            else:
                params['second_trade_id'] = self.second_trade_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdPrincipalformmCreateormodifyModel()
        if 'alipay_oid' in d:
            o.alipay_oid = d['alipay_oid']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'first_trade_id' in d:
            o.first_trade_id = d['first_trade_id']
        if 'principal_oid' in d:
            o.principal_oid = d['principal_oid']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'second_trade_id' in d:
            o.second_trade_id = d['second_trade_id']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlimamaPrincipalExtendInfo import AlimamaPrincipalExtendInfo


class OpenPrincipalQueryForMMResponse(object):

    def __init__(self):
        self._extend_info = None
        self._first_trade_id = None
        self._principal_id = None
        self._principal_name = None
        self._principal_oid = None
        self._principal_tag = None
        self._second_trade_id = None
        self._status = None
        self._status_name = None

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
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_name(self):
        return self._principal_name

    @principal_name.setter
    def principal_name(self, value):
        self._principal_name = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_name(self):
        return self._status_name

    @status_name.setter
    def status_name(self, value):
        self._status_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_name:
            if hasattr(self.principal_name, 'to_alipay_dict'):
                params['principal_name'] = self.principal_name.to_alipay_dict()
            else:
                params['principal_name'] = self.principal_name
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_name:
            if hasattr(self.status_name, 'to_alipay_dict'):
                params['status_name'] = self.status_name.to_alipay_dict()
            else:
                params['status_name'] = self.status_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenPrincipalQueryForMMResponse()
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'first_trade_id' in d:
            o.first_trade_id = d['first_trade_id']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_name' in d:
            o.principal_name = d['principal_name']
        if 'principal_oid' in d:
            o.principal_oid = d['principal_oid']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'second_trade_id' in d:
            o.second_trade_id = d['second_trade_id']
        if 'status' in d:
            o.status = d['status']
        if 'status_name' in d:
            o.status_name = d['status_name']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityIsvCreateModel(object):

    def __init__(self):
        self._bill_link_url = None
        self._billkey_query_mobile = None
        self._isv_app_id = None
        self._memo = None
        self._name = None
        self._pid = None
        self._rake_back_acct = None
        self._rake_back_acct_type = None
        self._related_bd = None
        self._scale = None
        self._type = None

    @property
    def bill_link_url(self):
        return self._bill_link_url

    @bill_link_url.setter
    def bill_link_url(self, value):
        self._bill_link_url = value
    @property
    def billkey_query_mobile(self):
        return self._billkey_query_mobile

    @billkey_query_mobile.setter
    def billkey_query_mobile(self, value):
        self._billkey_query_mobile = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def rake_back_acct(self):
        return self._rake_back_acct

    @rake_back_acct.setter
    def rake_back_acct(self, value):
        self._rake_back_acct = value
    @property
    def rake_back_acct_type(self):
        return self._rake_back_acct_type

    @rake_back_acct_type.setter
    def rake_back_acct_type(self, value):
        self._rake_back_acct_type = value
    @property
    def related_bd(self):
        return self._related_bd

    @related_bd.setter
    def related_bd(self, value):
        self._related_bd = value
    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_link_url:
            if hasattr(self.bill_link_url, 'to_alipay_dict'):
                params['bill_link_url'] = self.bill_link_url.to_alipay_dict()
            else:
                params['bill_link_url'] = self.bill_link_url
        if self.billkey_query_mobile:
            if hasattr(self.billkey_query_mobile, 'to_alipay_dict'):
                params['billkey_query_mobile'] = self.billkey_query_mobile.to_alipay_dict()
            else:
                params['billkey_query_mobile'] = self.billkey_query_mobile
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.rake_back_acct:
            if hasattr(self.rake_back_acct, 'to_alipay_dict'):
                params['rake_back_acct'] = self.rake_back_acct.to_alipay_dict()
            else:
                params['rake_back_acct'] = self.rake_back_acct
        if self.rake_back_acct_type:
            if hasattr(self.rake_back_acct_type, 'to_alipay_dict'):
                params['rake_back_acct_type'] = self.rake_back_acct_type.to_alipay_dict()
            else:
                params['rake_back_acct_type'] = self.rake_back_acct_type
        if self.related_bd:
            if hasattr(self.related_bd, 'to_alipay_dict'):
                params['related_bd'] = self.related_bd.to_alipay_dict()
            else:
                params['related_bd'] = self.related_bd
        if self.scale:
            if hasattr(self.scale, 'to_alipay_dict'):
                params['scale'] = self.scale.to_alipay_dict()
            else:
                params['scale'] = self.scale
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityIsvCreateModel()
        if 'bill_link_url' in d:
            o.bill_link_url = d['bill_link_url']
        if 'billkey_query_mobile' in d:
            o.billkey_query_mobile = d['billkey_query_mobile']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'name' in d:
            o.name = d['name']
        if 'pid' in d:
            o.pid = d['pid']
        if 'rake_back_acct' in d:
            o.rake_back_acct = d['rake_back_acct']
        if 'rake_back_acct_type' in d:
            o.rake_back_acct_type = d['rake_back_acct_type']
        if 'related_bd' in d:
            o.related_bd = d['related_bd']
        if 'scale' in d:
            o.scale = d['scale']
        if 'type' in d:
            o.type = d['type']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CorpEntity import CorpEntity
from alipay.aop.api.domain.CorpEntity import CorpEntity
from alipay.aop.api.domain.NotaryFileVO import NotaryFileVO


class AlipayBossProdAntlegalchainMultipartyApplyModel(object):

    def __init__(self):
        self._apply_buc_user_no = None
        self._biz_code = None
        self._biz_name = None
        self._biz_unique_id = None
        self._corp_entity_multi_list = None
        self._init_corp_entity = None
        self._notary_file_list = None
        self._request_app_name = None
        self._request_time_stamp = None
        self._request_token = None
        self._sign_order_type = None
        self._submit_time = None

    @property
    def apply_buc_user_no(self):
        return self._apply_buc_user_no

    @apply_buc_user_no.setter
    def apply_buc_user_no(self, value):
        self._apply_buc_user_no = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_name(self):
        return self._biz_name

    @biz_name.setter
    def biz_name(self, value):
        self._biz_name = value
    @property
    def biz_unique_id(self):
        return self._biz_unique_id

    @biz_unique_id.setter
    def biz_unique_id(self, value):
        self._biz_unique_id = value
    @property
    def corp_entity_multi_list(self):
        return self._corp_entity_multi_list

    @corp_entity_multi_list.setter
    def corp_entity_multi_list(self, value):
        if isinstance(value, list):
            self._corp_entity_multi_list = list()
            for i in value:
                if isinstance(i, CorpEntity):
                    self._corp_entity_multi_list.append(i)
                else:
                    self._corp_entity_multi_list.append(CorpEntity.from_alipay_dict(i))
    @property
    def init_corp_entity(self):
        return self._init_corp_entity

    @init_corp_entity.setter
    def init_corp_entity(self, value):
        if isinstance(value, CorpEntity):
            self._init_corp_entity = value
        else:
            self._init_corp_entity = CorpEntity.from_alipay_dict(value)
    @property
    def notary_file_list(self):
        return self._notary_file_list

    @notary_file_list.setter
    def notary_file_list(self, value):
        if isinstance(value, list):
            self._notary_file_list = list()
            for i in value:
                if isinstance(i, NotaryFileVO):
                    self._notary_file_list.append(i)
                else:
                    self._notary_file_list.append(NotaryFileVO.from_alipay_dict(i))
    @property
    def request_app_name(self):
        return self._request_app_name

    @request_app_name.setter
    def request_app_name(self, value):
        self._request_app_name = value
    @property
    def request_time_stamp(self):
        return self._request_time_stamp

    @request_time_stamp.setter
    def request_time_stamp(self, value):
        self._request_time_stamp = value
    @property
    def request_token(self):
        return self._request_token

    @request_token.setter
    def request_token(self, value):
        self._request_token = value
    @property
    def sign_order_type(self):
        return self._sign_order_type

    @sign_order_type.setter
    def sign_order_type(self, value):
        self._sign_order_type = value
    @property
    def submit_time(self):
        return self._submit_time

    @submit_time.setter
    def submit_time(self, value):
        self._submit_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_buc_user_no:
            if hasattr(self.apply_buc_user_no, 'to_alipay_dict'):
                params['apply_buc_user_no'] = self.apply_buc_user_no.to_alipay_dict()
            else:
                params['apply_buc_user_no'] = self.apply_buc_user_no
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_name:
            if hasattr(self.biz_name, 'to_alipay_dict'):
                params['biz_name'] = self.biz_name.to_alipay_dict()
            else:
                params['biz_name'] = self.biz_name
        if self.biz_unique_id:
            if hasattr(self.biz_unique_id, 'to_alipay_dict'):
                params['biz_unique_id'] = self.biz_unique_id.to_alipay_dict()
            else:
                params['biz_unique_id'] = self.biz_unique_id
        if self.corp_entity_multi_list:
            if isinstance(self.corp_entity_multi_list, list):
                for i in range(0, len(self.corp_entity_multi_list)):
                    element = self.corp_entity_multi_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.corp_entity_multi_list[i] = element.to_alipay_dict()
            if hasattr(self.corp_entity_multi_list, 'to_alipay_dict'):
                params['corp_entity_multi_list'] = self.corp_entity_multi_list.to_alipay_dict()
            else:
                params['corp_entity_multi_list'] = self.corp_entity_multi_list
        if self.init_corp_entity:
            if hasattr(self.init_corp_entity, 'to_alipay_dict'):
                params['init_corp_entity'] = self.init_corp_entity.to_alipay_dict()
            else:
                params['init_corp_entity'] = self.init_corp_entity
        if self.notary_file_list:
            if isinstance(self.notary_file_list, list):
                for i in range(0, len(self.notary_file_list)):
                    element = self.notary_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.notary_file_list[i] = element.to_alipay_dict()
            if hasattr(self.notary_file_list, 'to_alipay_dict'):
                params['notary_file_list'] = self.notary_file_list.to_alipay_dict()
            else:
                params['notary_file_list'] = self.notary_file_list
        if self.request_app_name:
            if hasattr(self.request_app_name, 'to_alipay_dict'):
                params['request_app_name'] = self.request_app_name.to_alipay_dict()
            else:
                params['request_app_name'] = self.request_app_name
        if self.request_time_stamp:
            if hasattr(self.request_time_stamp, 'to_alipay_dict'):
                params['request_time_stamp'] = self.request_time_stamp.to_alipay_dict()
            else:
                params['request_time_stamp'] = self.request_time_stamp
        if self.request_token:
            if hasattr(self.request_token, 'to_alipay_dict'):
                params['request_token'] = self.request_token.to_alipay_dict()
            else:
                params['request_token'] = self.request_token
        if self.sign_order_type:
            if hasattr(self.sign_order_type, 'to_alipay_dict'):
                params['sign_order_type'] = self.sign_order_type.to_alipay_dict()
            else:
                params['sign_order_type'] = self.sign_order_type
        if self.submit_time:
            if hasattr(self.submit_time, 'to_alipay_dict'):
                params['submit_time'] = self.submit_time.to_alipay_dict()
            else:
                params['submit_time'] = self.submit_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlegalchainMultipartyApplyModel()
        if 'apply_buc_user_no' in d:
            o.apply_buc_user_no = d['apply_buc_user_no']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_name' in d:
            o.biz_name = d['biz_name']
        if 'biz_unique_id' in d:
            o.biz_unique_id = d['biz_unique_id']
        if 'corp_entity_multi_list' in d:
            o.corp_entity_multi_list = d['corp_entity_multi_list']
        if 'init_corp_entity' in d:
            o.init_corp_entity = d['init_corp_entity']
        if 'notary_file_list' in d:
            o.notary_file_list = d['notary_file_list']
        if 'request_app_name' in d:
            o.request_app_name = d['request_app_name']
        if 'request_time_stamp' in d:
            o.request_time_stamp = d['request_time_stamp']
        if 'request_token' in d:
            o.request_token = d['request_token']
        if 'sign_order_type' in d:
            o.sign_order_type = d['sign_order_type']
        if 'submit_time' in d:
            o.submit_time = d['submit_time']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntlawSignOperator import AntlawSignOperator
from alipay.aop.api.domain.SealPageInfo import SealPageInfo
from alipay.aop.api.domain.AntlawSignOperator import AntlawSignOperator
from alipay.aop.api.domain.SealRequestInfo import SealRequestInfo


class AlipayBossProdElecsealOrderApplyModel(object):

    def __init__(self):
        self._app_name = None
        self._app_version = None
        self._business_unique_id = None
        self._file_oss_key = None
        self._first_party = None
        self._hash_value = None
        self._seal_page_info_list = None
        self._seal_request_mode = None
        self._second_parties = None
        self._unified_page_index_list = None
        self._unified_seal_request_info = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def business_unique_id(self):
        return self._business_unique_id

    @business_unique_id.setter
    def business_unique_id(self, value):
        self._business_unique_id = value
    @property
    def file_oss_key(self):
        return self._file_oss_key

    @file_oss_key.setter
    def file_oss_key(self, value):
        self._file_oss_key = value
    @property
    def first_party(self):
        return self._first_party

    @first_party.setter
    def first_party(self, value):
        if isinstance(value, AntlawSignOperator):
            self._first_party = value
        else:
            self._first_party = AntlawSignOperator.from_alipay_dict(value)
    @property
    def hash_value(self):
        return self._hash_value

    @hash_value.setter
    def hash_value(self, value):
        self._hash_value = value
    @property
    def seal_page_info_list(self):
        return self._seal_page_info_list

    @seal_page_info_list.setter
    def seal_page_info_list(self, value):
        if isinstance(value, list):
            self._seal_page_info_list = list()
            for i in value:
                if isinstance(i, SealPageInfo):
                    self._seal_page_info_list.append(i)
                else:
                    self._seal_page_info_list.append(SealPageInfo.from_alipay_dict(i))
    @property
    def seal_request_mode(self):
        return self._seal_request_mode

    @seal_request_mode.setter
    def seal_request_mode(self, value):
        self._seal_request_mode = value
    @property
    def second_parties(self):
        return self._second_parties

    @second_parties.setter
    def second_parties(self, value):
        if isinstance(value, list):
            self._second_parties = list()
            for i in value:
                if isinstance(i, AntlawSignOperator):
                    self._second_parties.append(i)
                else:
                    self._second_parties.append(AntlawSignOperator.from_alipay_dict(i))
    @property
    def unified_page_index_list(self):
        return self._unified_page_index_list

    @unified_page_index_list.setter
    def unified_page_index_list(self, value):
        if isinstance(value, list):
            self._unified_page_index_list = list()
            for i in value:
                self._unified_page_index_list.append(i)
    @property
    def unified_seal_request_info(self):
        return self._unified_seal_request_info

    @unified_seal_request_info.setter
    def unified_seal_request_info(self, value):
        if isinstance(value, SealRequestInfo):
            self._unified_seal_request_info = value
        else:
            self._unified_seal_request_info = SealRequestInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.business_unique_id:
            if hasattr(self.business_unique_id, 'to_alipay_dict'):
                params['business_unique_id'] = self.business_unique_id.to_alipay_dict()
            else:
                params['business_unique_id'] = self.business_unique_id
        if self.file_oss_key:
            if hasattr(self.file_oss_key, 'to_alipay_dict'):
                params['file_oss_key'] = self.file_oss_key.to_alipay_dict()
            else:
                params['file_oss_key'] = self.file_oss_key
        if self.first_party:
            if hasattr(self.first_party, 'to_alipay_dict'):
                params['first_party'] = self.first_party.to_alipay_dict()
            else:
                params['first_party'] = self.first_party
        if self.hash_value:
            if hasattr(self.hash_value, 'to_alipay_dict'):
                params['hash_value'] = self.hash_value.to_alipay_dict()
            else:
                params['hash_value'] = self.hash_value
        if self.seal_page_info_list:
            if isinstance(self.seal_page_info_list, list):
                for i in range(0, len(self.seal_page_info_list)):
                    element = self.seal_page_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.seal_page_info_list[i] = element.to_alipay_dict()
            if hasattr(self.seal_page_info_list, 'to_alipay_dict'):
                params['seal_page_info_list'] = self.seal_page_info_list.to_alipay_dict()
            else:
                params['seal_page_info_list'] = self.seal_page_info_list
        if self.seal_request_mode:
            if hasattr(self.seal_request_mode, 'to_alipay_dict'):
                params['seal_request_mode'] = self.seal_request_mode.to_alipay_dict()
            else:
                params['seal_request_mode'] = self.seal_request_mode
        if self.second_parties:
            if isinstance(self.second_parties, list):
                for i in range(0, len(self.second_parties)):
                    element = self.second_parties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.second_parties[i] = element.to_alipay_dict()
            if hasattr(self.second_parties, 'to_alipay_dict'):
                params['second_parties'] = self.second_parties.to_alipay_dict()
            else:
                params['second_parties'] = self.second_parties
        if self.unified_page_index_list:
            if isinstance(self.unified_page_index_list, list):
                for i in range(0, len(self.unified_page_index_list)):
                    element = self.unified_page_index_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.unified_page_index_list[i] = element.to_alipay_dict()
            if hasattr(self.unified_page_index_list, 'to_alipay_dict'):
                params['unified_page_index_list'] = self.unified_page_index_list.to_alipay_dict()
            else:
                params['unified_page_index_list'] = self.unified_page_index_list
        if self.unified_seal_request_info:
            if hasattr(self.unified_seal_request_info, 'to_alipay_dict'):
                params['unified_seal_request_info'] = self.unified_seal_request_info.to_alipay_dict()
            else:
                params['unified_seal_request_info'] = self.unified_seal_request_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdElecsealOrderApplyModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'business_unique_id' in d:
            o.business_unique_id = d['business_unique_id']
        if 'file_oss_key' in d:
            o.file_oss_key = d['file_oss_key']
        if 'first_party' in d:
            o.first_party = d['first_party']
        if 'hash_value' in d:
            o.hash_value = d['hash_value']
        if 'seal_page_info_list' in d:
            o.seal_page_info_list = d['seal_page_info_list']
        if 'seal_request_mode' in d:
            o.seal_request_mode = d['seal_request_mode']
        if 'second_parties' in d:
            o.second_parties = d['second_parties']
        if 'unified_page_index_list' in d:
            o.unified_page_index_list = d['unified_page_index_list']
        if 'unified_seal_request_info' in d:
            o.unified_seal_request_info = d['unified_seal_request_info']
        return o



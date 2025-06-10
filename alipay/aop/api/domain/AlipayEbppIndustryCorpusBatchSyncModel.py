#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DocDTO import DocDTO
from alipay.aop.api.domain.CommonQaDTO import CommonQaDTO
from alipay.aop.api.domain.ServiceItemDTO import ServiceItemDTO
from alipay.aop.api.domain.GovOrgServiceDTO import GovOrgServiceDTO


class AlipayEbppIndustryCorpusBatchSyncModel(object):

    def __init__(self):
        self._bot_id = None
        self._corpus_type = None
        self._doc_list = None
        self._faq_list = None
        self._item_list = None
        self._service_list = None

    @property
    def bot_id(self):
        return self._bot_id

    @bot_id.setter
    def bot_id(self, value):
        self._bot_id = value
    @property
    def corpus_type(self):
        return self._corpus_type

    @corpus_type.setter
    def corpus_type(self, value):
        self._corpus_type = value
    @property
    def doc_list(self):
        return self._doc_list

    @doc_list.setter
    def doc_list(self, value):
        if isinstance(value, list):
            self._doc_list = list()
            for i in value:
                if isinstance(i, DocDTO):
                    self._doc_list.append(i)
                else:
                    self._doc_list.append(DocDTO.from_alipay_dict(i))
    @property
    def faq_list(self):
        return self._faq_list

    @faq_list.setter
    def faq_list(self, value):
        if isinstance(value, list):
            self._faq_list = list()
            for i in value:
                if isinstance(i, CommonQaDTO):
                    self._faq_list.append(i)
                else:
                    self._faq_list.append(CommonQaDTO.from_alipay_dict(i))
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ServiceItemDTO):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ServiceItemDTO.from_alipay_dict(i))
    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                if isinstance(i, GovOrgServiceDTO):
                    self._service_list.append(i)
                else:
                    self._service_list.append(GovOrgServiceDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.bot_id:
            if hasattr(self.bot_id, 'to_alipay_dict'):
                params['bot_id'] = self.bot_id.to_alipay_dict()
            else:
                params['bot_id'] = self.bot_id
        if self.corpus_type:
            if hasattr(self.corpus_type, 'to_alipay_dict'):
                params['corpus_type'] = self.corpus_type.to_alipay_dict()
            else:
                params['corpus_type'] = self.corpus_type
        if self.doc_list:
            if isinstance(self.doc_list, list):
                for i in range(0, len(self.doc_list)):
                    element = self.doc_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.doc_list[i] = element.to_alipay_dict()
            if hasattr(self.doc_list, 'to_alipay_dict'):
                params['doc_list'] = self.doc_list.to_alipay_dict()
            else:
                params['doc_list'] = self.doc_list
        if self.faq_list:
            if isinstance(self.faq_list, list):
                for i in range(0, len(self.faq_list)):
                    element = self.faq_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.faq_list[i] = element.to_alipay_dict()
            if hasattr(self.faq_list, 'to_alipay_dict'):
                params['faq_list'] = self.faq_list.to_alipay_dict()
            else:
                params['faq_list'] = self.faq_list
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        if self.service_list:
            if isinstance(self.service_list, list):
                for i in range(0, len(self.service_list)):
                    element = self.service_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_list[i] = element.to_alipay_dict()
            if hasattr(self.service_list, 'to_alipay_dict'):
                params['service_list'] = self.service_list.to_alipay_dict()
            else:
                params['service_list'] = self.service_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCorpusBatchSyncModel()
        if 'bot_id' in d:
            o.bot_id = d['bot_id']
        if 'corpus_type' in d:
            o.corpus_type = d['corpus_type']
        if 'doc_list' in d:
            o.doc_list = d['doc_list']
        if 'faq_list' in d:
            o.faq_list = d['faq_list']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'service_list' in d:
            o.service_list = d['service_list']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateRightsContentDTO import TemplateRightsContentDTO


class TemplateOpenCardConfDTO(object):

    def __init__(self):
        self._card_rights = None
        self._conf = None
        self._open_card_source_type = None
        self._open_card_url = None
        self._source_app_id = None

    @property
    def card_rights(self):
        return self._card_rights

    @card_rights.setter
    def card_rights(self, value):
        if isinstance(value, list):
            self._card_rights = list()
            for i in value:
                if isinstance(i, TemplateRightsContentDTO):
                    self._card_rights.append(i)
                else:
                    self._card_rights.append(TemplateRightsContentDTO.from_alipay_dict(i))
    @property
    def conf(self):
        return self._conf

    @conf.setter
    def conf(self, value):
        self._conf = value
    @property
    def open_card_source_type(self):
        return self._open_card_source_type

    @open_card_source_type.setter
    def open_card_source_type(self, value):
        self._open_card_source_type = value
    @property
    def open_card_url(self):
        return self._open_card_url

    @open_card_url.setter
    def open_card_url(self, value):
        self._open_card_url = value
    @property
    def source_app_id(self):
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, value):
        self._source_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_rights:
            if isinstance(self.card_rights, list):
                for i in range(0, len(self.card_rights)):
                    element = self.card_rights[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_rights[i] = element.to_alipay_dict()
            if hasattr(self.card_rights, 'to_alipay_dict'):
                params['card_rights'] = self.card_rights.to_alipay_dict()
            else:
                params['card_rights'] = self.card_rights
        if self.conf:
            if hasattr(self.conf, 'to_alipay_dict'):
                params['conf'] = self.conf.to_alipay_dict()
            else:
                params['conf'] = self.conf
        if self.open_card_source_type:
            if hasattr(self.open_card_source_type, 'to_alipay_dict'):
                params['open_card_source_type'] = self.open_card_source_type.to_alipay_dict()
            else:
                params['open_card_source_type'] = self.open_card_source_type
        if self.open_card_url:
            if hasattr(self.open_card_url, 'to_alipay_dict'):
                params['open_card_url'] = self.open_card_url.to_alipay_dict()
            else:
                params['open_card_url'] = self.open_card_url
        if self.source_app_id:
            if hasattr(self.source_app_id, 'to_alipay_dict'):
                params['source_app_id'] = self.source_app_id.to_alipay_dict()
            else:
                params['source_app_id'] = self.source_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateOpenCardConfDTO()
        if 'card_rights' in d:
            o.card_rights = d['card_rights']
        if 'conf' in d:
            o.conf = d['conf']
        if 'open_card_source_type' in d:
            o.open_card_source_type = d['open_card_source_type']
        if 'open_card_url' in d:
            o.open_card_url = d['open_card_url']
        if 'source_app_id' in d:
            o.source_app_id = d['source_app_id']
        return o



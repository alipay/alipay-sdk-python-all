#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QualificationConsultInfo import QualificationConsultInfo


class AlipayMarketingQualificationConsultModel(object):

    def __init__(self):
        self._biz_context = None
        self._open_id = None
        self._qual_consult_infos = None
        self._user_id = None

    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        self._biz_context = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def qual_consult_infos(self):
        return self._qual_consult_infos

    @qual_consult_infos.setter
    def qual_consult_infos(self, value):
        if isinstance(value, list):
            self._qual_consult_infos = list()
            for i in value:
                if isinstance(i, QualificationConsultInfo):
                    self._qual_consult_infos.append(i)
                else:
                    self._qual_consult_infos.append(QualificationConsultInfo.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_context:
            if hasattr(self.biz_context, 'to_alipay_dict'):
                params['biz_context'] = self.biz_context.to_alipay_dict()
            else:
                params['biz_context'] = self.biz_context
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.qual_consult_infos:
            if isinstance(self.qual_consult_infos, list):
                for i in range(0, len(self.qual_consult_infos)):
                    element = self.qual_consult_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qual_consult_infos[i] = element.to_alipay_dict()
            if hasattr(self.qual_consult_infos, 'to_alipay_dict'):
                params['qual_consult_infos'] = self.qual_consult_infos.to_alipay_dict()
            else:
                params['qual_consult_infos'] = self.qual_consult_infos
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
        o = AlipayMarketingQualificationConsultModel()
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'qual_consult_infos' in d:
            o.qual_consult_infos = d['qual_consult_infos']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



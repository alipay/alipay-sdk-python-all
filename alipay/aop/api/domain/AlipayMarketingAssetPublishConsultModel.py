#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublishConsultInfo import PublishConsultInfo


class AlipayMarketingAssetPublishConsultModel(object):

    def __init__(self):
        self._biz_context = None
        self._entity_id_type = None
        self._open_id = None
        self._publish_consult_infos = None
        self._user_id = None

    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        self._biz_context = value
    @property
    def entity_id_type(self):
        return self._entity_id_type

    @entity_id_type.setter
    def entity_id_type(self, value):
        self._entity_id_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def publish_consult_infos(self):
        return self._publish_consult_infos

    @publish_consult_infos.setter
    def publish_consult_infos(self, value):
        if isinstance(value, list):
            self._publish_consult_infos = list()
            for i in value:
                if isinstance(i, PublishConsultInfo):
                    self._publish_consult_infos.append(i)
                else:
                    self._publish_consult_infos.append(PublishConsultInfo.from_alipay_dict(i))
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
        if self.entity_id_type:
            if hasattr(self.entity_id_type, 'to_alipay_dict'):
                params['entity_id_type'] = self.entity_id_type.to_alipay_dict()
            else:
                params['entity_id_type'] = self.entity_id_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.publish_consult_infos:
            if isinstance(self.publish_consult_infos, list):
                for i in range(0, len(self.publish_consult_infos)):
                    element = self.publish_consult_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.publish_consult_infos[i] = element.to_alipay_dict()
            if hasattr(self.publish_consult_infos, 'to_alipay_dict'):
                params['publish_consult_infos'] = self.publish_consult_infos.to_alipay_dict()
            else:
                params['publish_consult_infos'] = self.publish_consult_infos
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
        o = AlipayMarketingAssetPublishConsultModel()
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'entity_id_type' in d:
            o.entity_id_type = d['entity_id_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'publish_consult_infos' in d:
            o.publish_consult_infos = d['publish_consult_infos']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



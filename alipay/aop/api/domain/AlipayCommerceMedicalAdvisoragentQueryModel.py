#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Entity import Entity


class AlipayCommerceMedicalAdvisoragentQueryModel(object):

    def __init__(self):
        self._biz_info_entity = None
        self._chat_id = None
        self._out_open_id = None
        self._out_user_id = None
        self._session_id = None
        self._skill = None

    @property
    def biz_info_entity(self):
        return self._biz_info_entity

    @biz_info_entity.setter
    def biz_info_entity(self, value):
        if isinstance(value, Entity):
            self._biz_info_entity = value
        else:
            self._biz_info_entity = Entity.from_alipay_dict(value)
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def out_open_id(self):
        return self._out_open_id

    @out_open_id.setter
    def out_open_id(self, value):
        self._out_open_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, value):
        self._skill = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info_entity:
            if hasattr(self.biz_info_entity, 'to_alipay_dict'):
                params['biz_info_entity'] = self.biz_info_entity.to_alipay_dict()
            else:
                params['biz_info_entity'] = self.biz_info_entity
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.out_open_id:
            if hasattr(self.out_open_id, 'to_alipay_dict'):
                params['out_open_id'] = self.out_open_id.to_alipay_dict()
            else:
                params['out_open_id'] = self.out_open_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.skill:
            if hasattr(self.skill, 'to_alipay_dict'):
                params['skill'] = self.skill.to_alipay_dict()
            else:
                params['skill'] = self.skill
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAdvisoragentQueryModel()
        if 'biz_info_entity' in d:
            o.biz_info_entity = d['biz_info_entity']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'out_open_id' in d:
            o.out_open_id = d['out_open_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'skill' in d:
            o.skill = d['skill']
        return o



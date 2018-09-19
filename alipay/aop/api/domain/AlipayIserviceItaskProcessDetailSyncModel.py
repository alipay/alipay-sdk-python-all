#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtendFieldInfo import ExtendFieldInfo


class AlipayIserviceItaskProcessDetailSyncModel(object):

    def __init__(self):
        self._app_name = None
        self._exapp_name = None
        self._exsystem_operator_id = None
        self._exsystem_operator_name = None
        self._exsystem_ticket_id = None
        self._exsystem_ticket_state = None
        self._extend_field_infos = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def exapp_name(self):
        return self._exapp_name

    @exapp_name.setter
    def exapp_name(self, value):
        self._exapp_name = value
    @property
    def exsystem_operator_id(self):
        return self._exsystem_operator_id

    @exsystem_operator_id.setter
    def exsystem_operator_id(self, value):
        self._exsystem_operator_id = value
    @property
    def exsystem_operator_name(self):
        return self._exsystem_operator_name

    @exsystem_operator_name.setter
    def exsystem_operator_name(self, value):
        self._exsystem_operator_name = value
    @property
    def exsystem_ticket_id(self):
        return self._exsystem_ticket_id

    @exsystem_ticket_id.setter
    def exsystem_ticket_id(self, value):
        self._exsystem_ticket_id = value
    @property
    def exsystem_ticket_state(self):
        return self._exsystem_ticket_state

    @exsystem_ticket_state.setter
    def exsystem_ticket_state(self, value):
        self._exsystem_ticket_state = value
    @property
    def extend_field_infos(self):
        return self._extend_field_infos

    @extend_field_infos.setter
    def extend_field_infos(self, value):
        if isinstance(value, list):
            self._extend_field_infos = list()
            for i in value:
                if isinstance(i, ExtendFieldInfo):
                    self._extend_field_infos.append(i)
                else:
                    self._extend_field_infos.append(ExtendFieldInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.exapp_name:
            if hasattr(self.exapp_name, 'to_alipay_dict'):
                params['exapp_name'] = self.exapp_name.to_alipay_dict()
            else:
                params['exapp_name'] = self.exapp_name
        if self.exsystem_operator_id:
            if hasattr(self.exsystem_operator_id, 'to_alipay_dict'):
                params['exsystem_operator_id'] = self.exsystem_operator_id.to_alipay_dict()
            else:
                params['exsystem_operator_id'] = self.exsystem_operator_id
        if self.exsystem_operator_name:
            if hasattr(self.exsystem_operator_name, 'to_alipay_dict'):
                params['exsystem_operator_name'] = self.exsystem_operator_name.to_alipay_dict()
            else:
                params['exsystem_operator_name'] = self.exsystem_operator_name
        if self.exsystem_ticket_id:
            if hasattr(self.exsystem_ticket_id, 'to_alipay_dict'):
                params['exsystem_ticket_id'] = self.exsystem_ticket_id.to_alipay_dict()
            else:
                params['exsystem_ticket_id'] = self.exsystem_ticket_id
        if self.exsystem_ticket_state:
            if hasattr(self.exsystem_ticket_state, 'to_alipay_dict'):
                params['exsystem_ticket_state'] = self.exsystem_ticket_state.to_alipay_dict()
            else:
                params['exsystem_ticket_state'] = self.exsystem_ticket_state
        if self.extend_field_infos:
            if isinstance(self.extend_field_infos, list):
                for i in range(0, len(self.extend_field_infos)):
                    element = self.extend_field_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_field_infos[i] = element.to_alipay_dict()
            if hasattr(self.extend_field_infos, 'to_alipay_dict'):
                params['extend_field_infos'] = self.extend_field_infos.to_alipay_dict()
            else:
                params['extend_field_infos'] = self.extend_field_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceItaskProcessDetailSyncModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'exapp_name' in d:
            o.exapp_name = d['exapp_name']
        if 'exsystem_operator_id' in d:
            o.exsystem_operator_id = d['exsystem_operator_id']
        if 'exsystem_operator_name' in d:
            o.exsystem_operator_name = d['exsystem_operator_name']
        if 'exsystem_ticket_id' in d:
            o.exsystem_ticket_id = d['exsystem_ticket_id']
        if 'exsystem_ticket_state' in d:
            o.exsystem_ticket_state = d['exsystem_ticket_state']
        if 'extend_field_infos' in d:
            o.extend_field_infos = d['extend_field_infos']
        return o



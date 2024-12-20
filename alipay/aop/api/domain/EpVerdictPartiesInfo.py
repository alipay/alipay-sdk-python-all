#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpVerdictPartiesInfo(object):

    def __init__(self):
        self._judgment_result = None
        self._legal_representative = None
        self._name = None
        self._other_roles = None
        self._roles = None
        self._type = None

    @property
    def judgment_result(self):
        return self._judgment_result

    @judgment_result.setter
    def judgment_result(self, value):
        self._judgment_result = value
    @property
    def legal_representative(self):
        return self._legal_representative

    @legal_representative.setter
    def legal_representative(self, value):
        if isinstance(value, list):
            self._legal_representative = list()
            for i in value:
                self._legal_representative.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def other_roles(self):
        return self._other_roles

    @other_roles.setter
    def other_roles(self, value):
        if isinstance(value, list):
            self._other_roles = list()
            for i in value:
                self._other_roles.append(i)
    @property
    def roles(self):
        return self._roles

    @roles.setter
    def roles(self, value):
        if isinstance(value, list):
            self._roles = list()
            for i in value:
                self._roles.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.judgment_result:
            if hasattr(self.judgment_result, 'to_alipay_dict'):
                params['judgment_result'] = self.judgment_result.to_alipay_dict()
            else:
                params['judgment_result'] = self.judgment_result
        if self.legal_representative:
            if isinstance(self.legal_representative, list):
                for i in range(0, len(self.legal_representative)):
                    element = self.legal_representative[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.legal_representative[i] = element.to_alipay_dict()
            if hasattr(self.legal_representative, 'to_alipay_dict'):
                params['legal_representative'] = self.legal_representative.to_alipay_dict()
            else:
                params['legal_representative'] = self.legal_representative
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.other_roles:
            if isinstance(self.other_roles, list):
                for i in range(0, len(self.other_roles)):
                    element = self.other_roles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_roles[i] = element.to_alipay_dict()
            if hasattr(self.other_roles, 'to_alipay_dict'):
                params['other_roles'] = self.other_roles.to_alipay_dict()
            else:
                params['other_roles'] = self.other_roles
        if self.roles:
            if isinstance(self.roles, list):
                for i in range(0, len(self.roles)):
                    element = self.roles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.roles[i] = element.to_alipay_dict()
            if hasattr(self.roles, 'to_alipay_dict'):
                params['roles'] = self.roles.to_alipay_dict()
            else:
                params['roles'] = self.roles
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
        o = EpVerdictPartiesInfo()
        if 'judgment_result' in d:
            o.judgment_result = d['judgment_result']
        if 'legal_representative' in d:
            o.legal_representative = d['legal_representative']
        if 'name' in d:
            o.name = d['name']
        if 'other_roles' in d:
            o.other_roles = d['other_roles']
        if 'roles' in d:
            o.roles = d['roles']
        if 'type' in d:
            o.type = d['type']
        return o


